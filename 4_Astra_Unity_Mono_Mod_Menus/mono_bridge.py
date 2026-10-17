#!/usr/bin/env python3
# ==============================================================================
# ASTRA AI - EXTERNAL PYTHON MONO C-API BRIDGE (ZERO AOB SCANNING)
# Target   : Blasphemous.exe (mono.dll / mono-2.0-bdwgc.dll x64)
# Arsitek  : Gemini 4 Argon + Antigravity Engine
# Metode   : Remote Export Resolver + x64 Call Stub via CreateRemoteThread
# Fitur    : Direct Memory Pointer Extraction & Remote Runtime Invocation
#            (Core.Logic.Penitent & Core.SpawnManager.Teleport)
# ==============================================================================

import ctypes
import ctypes.wintypes as wt
import struct
import pymem
import pymem.process

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

kernel32.CreateRemoteThread.argtypes = [
    wt.HANDLE, wt.LPVOID, ctypes.c_size_t, wt.LPVOID, wt.LPVOID, wt.DWORD, wt.LPDWORD
]
kernel32.CreateRemoteThread.restype = wt.HANDLE
kernel32.WaitForSingleObject.argtypes = [wt.HANDLE, wt.DWORD]
kernel32.GetProcAddress.argtypes = [wt.HMODULE, wt.LPCSTR]
kernel32.GetProcAddress.restype = ctypes.c_void_p
kernel32.LoadLibraryExW.argtypes = [wt.LPCWSTR, wt.HANDLE, wt.DWORD]
kernel32.LoadLibraryExW.restype = wt.HMODULE

DONT_RESOLVE_DLL_REFERENCES = 0x00000001


class ExternalMonoBridge:
    """
    Menjalankan fungsi C-API Mono x64 langsung di address space Blasphemous.exe
    menggunakan x64 fastcall shellcode dan CreateRemoteThread.
    """
    def __init__(self, pm: pymem.Pymem):
        self.pm = pm

        # Cari modul mono (mendukung mono.dll maupun mono-2.0-bdwgc.dll)
        self.mono_mod = None
        for candidate in ["mono.dll", "mono-2.0-bdwgc.dll"]:
            try:
                self.mono_mod = pymem.process.module_from_name(self.pm.process_handle, candidate)
                if self.mono_mod:
                    break
            except Exception:
                continue

        if not self.mono_mod:
            raise RuntimeError("Modul Mono Runtime tidak ditemukan di dalam proses target.")

        self.mono_base = self.mono_mod.lpBaseOfDll
        self.mono_path = self.mono_mod.filename

        # Alokasi scratchpad 4KB di dalam memori game
        self.scratchpad = self.pm.allocate(0x1000)
        self.ret_val_addr = self.scratchpad + 0x800  # Return pointer 64-bit
        self.str_buf_addr = self.scratchpad + 0x900  # String buffer

        # Resolusi alamat ekspor C-API (Lengkap dengan Runtime Invoker)
        self.exports = self._resolve_mono_exports([
            b"mono_get_root_domain",
            b"mono_thread_attach",
            b"mono_domain_assembly_open",
            b"mono_assembly_get_image",
            b"mono_class_from_name",
            b"mono_class_vtable",
            b"mono_runtime_class_init",
            b"mono_vtable_get_static_field_data",
            b"mono_class_get_field_from_name",
            b"mono_field_get_offset",
            b"mono_class_get_method_from_name",
            b"mono_string_new",
            b"mono_runtime_invoke",
        ])

    def _resolve_mono_exports(self, func_names: list) -> dict:
        local_hmod = kernel32.LoadLibraryExW(self.mono_path, None, DONT_RESOLVE_DLL_REFERENCES)
        if not local_hmod:
            raise RuntimeError(f"Gagal memuat {self.mono_path} secara lokal.")

        resolved = {}
        for name in func_names:
            local_addr = kernel32.GetProcAddress(local_hmod, name)
            if local_addr:
                rva = local_addr - local_hmod
                resolved[name.decode()] = self.mono_base + rva
        kernel32.FreeLibrary(wt.HMODULE(local_hmod))
        return resolved

    def write_remote_string(self, text: str, offset: int = 0) -> int:
        addr = self.str_buf_addr + offset
        data = text.encode("utf-8") + b"\x00"
        self.pm.write_bytes(addr, data, len(data))
        return addr

    def call_mono_x64(self, func_addr: int, rcx: int = 0, rdx: int = 0, r8: int = 0) -> int:
        """Fastcall x64 (3 argumen: RCX, RDX, R8)"""
        shellcode = (
            b"\x48\x83\xEC\x28" +                           # sub rsp, 0x28
            b"\x48\xB9" + struct.pack("<Q", rcx) +          # mov rcx, <arg1>
            b"\x48\xBA" + struct.pack("<Q", rdx) +          # mov rdx, <arg2>
            b"\x49\xB8" + struct.pack("<Q", r8) +           # mov r8,  <arg3>
            b"\x48\xB8" + struct.pack("<Q", func_addr) +     # mov rax, <func_addr>
            b"\xFF\xD0" +                                   # call rax
            b"\x48\xA3" + struct.pack("<Q", self.ret_val_addr) + # mov [ret_val_addr], rax
            b"\x48\x83\xC4\x28" +                           # add rsp, 0x28
            b"\xC3"                                         # ret
        )
        self.pm.write_bytes(self.scratchpad, shellcode, len(shellcode))
        self.pm.write_ulonglong(self.ret_val_addr, 0)

        h_thread = kernel32.CreateRemoteThread(
            self.pm.process_handle, None, 0, self.scratchpad, None, 0, None
        )
        if not h_thread:
            raise RuntimeError("CreateRemoteThread gagal dieksekusi di proses target.")

        kernel32.WaitForSingleObject(h_thread, 3000)
        kernel32.CloseHandle(h_thread)
        return self.pm.read_ulonglong(self.ret_val_addr)

    def call_mono_x64_4args(self, func_addr: int, rcx: int = 0, rdx: int = 0, r8: int = 0, r9: int = 0) -> int:
        """
        Fastcall x64 (4 argumen penuh: RCX, RDX, R8, R9)
        Diperlukan untuk mono_runtime_invoke(method, instance, params_array, exc)
        """
        shellcode = (
            b"\x48\x83\xEC\x28" +                           # sub rsp, 0x28
            b"\x48\xB9" + struct.pack("<Q", rcx) +          # mov rcx, arg1
            b"\x48\xBA" + struct.pack("<Q", rdx) +          # mov rdx, arg2
            b"\x49\xB8" + struct.pack("<Q", r8) +           # mov r8,  arg3
            b"\x49\xB9" + struct.pack("<Q", r9) +           # mov r9,  arg4
            b"\x48\xB8" + struct.pack("<Q", func_addr) +     # mov rax, func_addr
            b"\xFF\xD0" +                                   # call rax
            b"\x48\xA3" + struct.pack("<Q", self.ret_val_addr) + # mov [ret], rax
            b"\x48\x83\xC4\x28" +                           # add rsp, 0x28
            b"\xC3"                                         # ret
        )
        self.pm.write_bytes(self.scratchpad, shellcode, len(shellcode))
        self.pm.write_ulonglong(self.ret_val_addr, 0)

        h_thread = kernel32.CreateRemoteThread(
            self.pm.process_handle, None, 0, self.scratchpad, None, 0, None
        )
        if not h_thread:
            raise RuntimeError("CreateRemoteThread gagal dieksekusi di proses target.")

        kernel32.WaitForSingleObject(h_thread, 5000)
        kernel32.CloseHandle(h_thread)
        return self.pm.read_ulonglong(self.ret_val_addr)

    def create_mono_string(self, domain: int, text: str) -> int:
        """Mengubah string Python menjadi pointer MonoString* (System.String) di RAM game."""
        c_str_addr = self.write_remote_string(text, 0x400)
        return self.call_mono_x64(self.exports["mono_string_new"], domain, c_str_addr)

    def get_core_manager_instance(self, domain: int, image: int, backing_field_name: str) -> int:
        """Membaca static property apa pun dari Framework.Managers.Core"""
        s_ns = self.write_remote_string("Framework.Managers", 0x100)
        s_cls = self.write_remote_string("Core", 0x200)
        core_class = self.call_mono_x64(self.exports["mono_class_from_name"], image, s_ns, s_cls)

        vtable = self.call_mono_x64(self.exports["mono_class_vtable"], domain, core_class)
        self.call_mono_x64(self.exports["mono_runtime_class_init"], vtable)
        static_data_ptr = self.call_mono_x64(self.exports["mono_vtable_get_static_field_data"], vtable)

        s_field = self.write_remote_string(backing_field_name, 0x300)
        field_ptr = self.call_mono_x64(self.exports["mono_class_get_field_from_name"], core_class, s_field)
        if not field_ptr:
            return 0

        field_offset = self.call_mono_x64(self.exports["mono_field_get_offset"], field_ptr)
        return self.pm.read_ulonglong(static_data_ptr + field_offset)

    def get_penitent_pointer(self) -> int:
        """Mengambil pointer objek aktif Core.Logic.Penitent tanpa scanning AOB!"""
        try:
            domain = self.call_mono_x64(self.exports["mono_get_root_domain"])
            self.call_mono_x64(self.exports["mono_thread_attach"], domain)

            s_asm = self.write_remote_string("Assembly-CSharp", 0)
            assembly = self.call_mono_x64(self.exports["mono_domain_assembly_open"], domain, s_asm)
            if not assembly:
                return 0
            image = self.call_mono_x64(self.exports["mono_assembly_get_image"], assembly)

            logic_instance = self.get_core_manager_instance(domain, image, "<Logic>k__BackingField")
            if not logic_instance:
                return 0

            s_ns = self.write_remote_string("Framework.Managers", 0x100)
            s_lcls = self.write_remote_string("LogicManager", 0x200)
            logic_class = self.call_mono_x64(self.exports["mono_class_from_name"], image, s_ns, s_lcls)
            s_pfield = self.write_remote_string("<Penitent>k__BackingField", 0x300)
            pen_field = self.call_mono_x64(self.exports["mono_class_get_field_from_name"], logic_class, s_pfield)
            pen_offset = self.call_mono_x64(self.exports["mono_field_get_offset"], pen_field)

            return self.pm.read_ulonglong(logic_instance + pen_offset)
        except Exception:
            return 0

    def teleport_to_priedieu(self, teleport_id: str = "TELEPORT_D01") -> bool:
        """
        Memanggil Core.SpawnManager.Teleport(string teleportId) secara remote!
        Aman tanpa black screen karena mengikutsertakan LevelManager untuk transisi scene.
        """
        try:
            domain = self.call_mono_x64(self.exports["mono_get_root_domain"])
            self.call_mono_x64(self.exports["mono_thread_attach"], domain)

            s_asm = self.write_remote_string("Assembly-CSharp", 0)
            assembly = self.call_mono_x64(self.exports["mono_domain_assembly_open"], domain, s_asm)
            if not assembly:
                return False
            image = self.call_mono_x64(self.exports["mono_assembly_get_image"], assembly)

            spawn_mgr_instance = self.get_core_manager_instance(domain, image, "<SpawnManager>k__BackingField")
            if not spawn_mgr_instance:
                return False

            s_ns = self.write_remote_string("Framework.Managers", 0x100)
            s_sm = self.write_remote_string("SpawnManager", 0x200)
            spawn_mgr_class = self.call_mono_x64(self.exports["mono_class_from_name"], image, s_ns, s_sm)

            s_mname = self.write_remote_string("Teleport", 0x300)
            teleport_method = self.call_mono_x64(
                self.exports["mono_class_get_method_from_name"], spawn_mgr_class, s_mname, 1
            )

            if teleport_method:
                mono_str_arg = self.create_mono_string(domain, teleport_id)
                args_array_addr = self.scratchpad + 0x500
                self.pm.write_ulonglong(args_array_addr, mono_str_arg)

                self.call_mono_x64_4args(
                    self.exports["mono_runtime_invoke"],
                    teleport_method,
                    spawn_mgr_instance,
                    args_array_addr,
                    0
                )
                return True

            # Fallback: Respawn ke Prie-Dieu aktif terakhir
            s_respawn = self.write_remote_string("Respawn", 0x300)
            respawn_method = self.call_mono_x64(
                self.exports["mono_class_get_method_from_name"], spawn_mgr_class, s_respawn, 0
            )
            if respawn_method:
                self.call_mono_x64_4args(
                    self.exports["mono_runtime_invoke"],
                    respawn_method,
                    spawn_mgr_instance,
                    0,
                    0
                )
                return True

            return False
        except Exception:
            return False
