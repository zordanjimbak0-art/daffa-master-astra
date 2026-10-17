-- ASTRA AI Cheat Engine Automated Lua Trainer Engine
-- Target: Unity Mono & Native x64 Games (Komandan Muhamad Daffa Cahya)

AstraTrainer = {
    Version = "6.0.0-ULTRA",
    ActiveRecords = {},
    ProcessAttached = false
}

function AstraTrainer:AttachGameProcess(exeName)
    local pid = getProcessIDFromProcessName(exeName)
    if pid ~= nil and pid > 0 then
        openProcess(pid)
        self.ProcessAttached = true
        print(string.format("[ASTRA LUA] Attached to %s (PID: %d)", exeName, pid))
        return true
    end
    return false
end

function AstraTrainer:ScanAOBSignature(signature, protectionFlags)
    local ms = createMemScan()
    local foundList = createFoundList(ms)
    ms.firstScan(
        soExactValue, vtByteArray, rtRounded,
        signature, "", 0, 0x7fffffffffffffff,
        protectionFlags or "+W-C",
        fsmNotAligned, "1", true, false, false, false
    )
    ms.waitTillDone()
    foundList.initialize()
    local results = {}
    for i = 0, foundList.Count - 1 do
        table.insert(results, foundList.Address[i])
    end
    foundList.destroy()
    ms.destroy()
    return results
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #01] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_01(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_01, 2048, %s)
        label(returnhere_01)
        newmem_01:
        mov [rax+18], #%d
        jmp returnhere_01
        %s:
        jmp newmem_01
        returnhere_01:
        [DISABLE]
        dealloc(newmem_01)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #02] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_02(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_02, 2048, %s)
        label(returnhere_02)
        newmem_02:
        mov [rax+18], #%d
        jmp returnhere_02
        %s:
        jmp newmem_02
        returnhere_02:
        [DISABLE]
        dealloc(newmem_02)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #03] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_03(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_03, 2048, %s)
        label(returnhere_03)
        newmem_03:
        mov [rax+18], #%d
        jmp returnhere_03
        %s:
        jmp newmem_03
        returnhere_03:
        [DISABLE]
        dealloc(newmem_03)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #04] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_04(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_04, 2048, %s)
        label(returnhere_04)
        newmem_04:
        mov [rax+18], #%d
        jmp returnhere_04
        %s:
        jmp newmem_04
        returnhere_04:
        [DISABLE]
        dealloc(newmem_04)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #05] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_05(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_05, 2048, %s)
        label(returnhere_05)
        newmem_05:
        mov [rax+18], #%d
        jmp returnhere_05
        %s:
        jmp newmem_05
        returnhere_05:
        [DISABLE]
        dealloc(newmem_05)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #06] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_06(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_06, 2048, %s)
        label(returnhere_06)
        newmem_06:
        mov [rax+18], #%d
        jmp returnhere_06
        %s:
        jmp newmem_06
        returnhere_06:
        [DISABLE]
        dealloc(newmem_06)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #07] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_07(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_07, 2048, %s)
        label(returnhere_07)
        newmem_07:
        mov [rax+18], #%d
        jmp returnhere_07
        %s:
        jmp newmem_07
        returnhere_07:
        [DISABLE]
        dealloc(newmem_07)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #08] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_08(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_08, 2048, %s)
        label(returnhere_08)
        newmem_08:
        mov [rax+18], #%d
        jmp returnhere_08
        %s:
        jmp newmem_08
        returnhere_08:
        [DISABLE]
        dealloc(newmem_08)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #09] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_09(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_09, 2048, %s)
        label(returnhere_09)
        newmem_09:
        mov [rax+18], #%d
        jmp returnhere_09
        %s:
        jmp newmem_09
        returnhere_09:
        [DISABLE]
        dealloc(newmem_09)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #10] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_10(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_10, 2048, %s)
        label(returnhere_10)
        newmem_10:
        mov [rax+18], #%d
        jmp returnhere_10
        %s:
        jmp newmem_10
        returnhere_10:
        [DISABLE]
        dealloc(newmem_10)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #11] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_11(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_11, 2048, %s)
        label(returnhere_11)
        newmem_11:
        mov [rax+18], #%d
        jmp returnhere_11
        %s:
        jmp newmem_11
        returnhere_11:
        [DISABLE]
        dealloc(newmem_11)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #12] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_12(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_12, 2048, %s)
        label(returnhere_12)
        newmem_12:
        mov [rax+18], #%d
        jmp returnhere_12
        %s:
        jmp newmem_12
        returnhere_12:
        [DISABLE]
        dealloc(newmem_12)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #13] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_13(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_13, 2048, %s)
        label(returnhere_13)
        newmem_13:
        mov [rax+18], #%d
        jmp returnhere_13
        %s:
        jmp newmem_13
        returnhere_13:
        [DISABLE]
        dealloc(newmem_13)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #14] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_14(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_14, 2048, %s)
        label(returnhere_14)
        newmem_14:
        mov [rax+18], #%d
        jmp returnhere_14
        %s:
        jmp newmem_14
        returnhere_14:
        [DISABLE]
        dealloc(newmem_14)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #15] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_15(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_15, 2048, %s)
        label(returnhere_15)
        newmem_15:
        mov [rax+18], #%d
        jmp returnhere_15
        %s:
        jmp newmem_15
        returnhere_15:
        [DISABLE]
        dealloc(newmem_15)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #16] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_16(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_16, 2048, %s)
        label(returnhere_16)
        newmem_16:
        mov [rax+18], #%d
        jmp returnhere_16
        %s:
        jmp newmem_16
        returnhere_16:
        [DISABLE]
        dealloc(newmem_16)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #17] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_17(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_17, 2048, %s)
        label(returnhere_17)
        newmem_17:
        mov [rax+18], #%d
        jmp returnhere_17
        %s:
        jmp newmem_17
        returnhere_17:
        [DISABLE]
        dealloc(newmem_17)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #18] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_18(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_18, 2048, %s)
        label(returnhere_18)
        newmem_18:
        mov [rax+18], #%d
        jmp returnhere_18
        %s:
        jmp newmem_18
        returnhere_18:
        [DISABLE]
        dealloc(newmem_18)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #19] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_19(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_19, 2048, %s)
        label(returnhere_19)
        newmem_19:
        mov [rax+18], #%d
        jmp returnhere_19
        %s:
        jmp newmem_19
        returnhere_19:
        [DISABLE]
        dealloc(newmem_19)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #20] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_20(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_20, 2048, %s)
        label(returnhere_20)
        newmem_20:
        mov [rax+18], #%d
        jmp returnhere_20
        %s:
        jmp newmem_20
        returnhere_20:
        [DISABLE]
        dealloc(newmem_20)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #21] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_21(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_21, 2048, %s)
        label(returnhere_21)
        newmem_21:
        mov [rax+18], #%d
        jmp returnhere_21
        %s:
        jmp newmem_21
        returnhere_21:
        [DISABLE]
        dealloc(newmem_21)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #22] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_22(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_22, 2048, %s)
        label(returnhere_22)
        newmem_22:
        mov [rax+18], #%d
        jmp returnhere_22
        %s:
        jmp newmem_22
        returnhere_22:
        [DISABLE]
        dealloc(newmem_22)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #23] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_23(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_23, 2048, %s)
        label(returnhere_23)
        newmem_23:
        mov [rax+18], #%d
        jmp returnhere_23
        %s:
        jmp newmem_23
        returnhere_23:
        [DISABLE]
        dealloc(newmem_23)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #24] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_24(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_24, 2048, %s)
        label(returnhere_24)
        newmem_24:
        mov [rax+18], #%d
        jmp returnhere_24
        %s:
        jmp newmem_24
        returnhere_24:
        [DISABLE]
        dealloc(newmem_24)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #25] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_25(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_25, 2048, %s)
        label(returnhere_25)
        newmem_25:
        mov [rax+18], #%d
        jmp returnhere_25
        %s:
        jmp newmem_25
        returnhere_25:
        [DISABLE]
        dealloc(newmem_25)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #26] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_26(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_26, 2048, %s)
        label(returnhere_26)
        newmem_26:
        mov [rax+18], #%d
        jmp returnhere_26
        %s:
        jmp newmem_26
        returnhere_26:
        [DISABLE]
        dealloc(newmem_26)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #27] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_27(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_27, 2048, %s)
        label(returnhere_27)
        newmem_27:
        mov [rax+18], #%d
        jmp returnhere_27
        %s:
        jmp newmem_27
        returnhere_27:
        [DISABLE]
        dealloc(newmem_27)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #28] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_28(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_28, 2048, %s)
        label(returnhere_28)
        newmem_28:
        mov [rax+18], #%d
        jmp returnhere_28
        %s:
        jmp newmem_28
        returnhere_28:
        [DISABLE]
        dealloc(newmem_28)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #29] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_29(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_29, 2048, %s)
        label(returnhere_29)
        newmem_29:
        mov [rax+18], #%d
        jmp returnhere_29
        %s:
        jmp newmem_29
        returnhere_29:
        [DISABLE]
        dealloc(newmem_29)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #30] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_30(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_30, 2048, %s)
        label(returnhere_30)
        newmem_30:
        mov [rax+18], #%d
        jmp returnhere_30
        %s:
        jmp newmem_30
        returnhere_30:
        [DISABLE]
        dealloc(newmem_30)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #31] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_31(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_31, 2048, %s)
        label(returnhere_31)
        newmem_31:
        mov [rax+18], #%d
        jmp returnhere_31
        %s:
        jmp newmem_31
        returnhere_31:
        [DISABLE]
        dealloc(newmem_31)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #32] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_32(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_32, 2048, %s)
        label(returnhere_32)
        newmem_32:
        mov [rax+18], #%d
        jmp returnhere_32
        %s:
        jmp newmem_32
        returnhere_32:
        [DISABLE]
        dealloc(newmem_32)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #33] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_33(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_33, 2048, %s)
        label(returnhere_33)
        newmem_33:
        mov [rax+18], #%d
        jmp returnhere_33
        %s:
        jmp newmem_33
        returnhere_33:
        [DISABLE]
        dealloc(newmem_33)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #34] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_34(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_34, 2048, %s)
        label(returnhere_34)
        newmem_34:
        mov [rax+18], #%d
        jmp returnhere_34
        %s:
        jmp newmem_34
        returnhere_34:
        [DISABLE]
        dealloc(newmem_34)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #35] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_35(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_35, 2048, %s)
        label(returnhere_35)
        newmem_35:
        mov [rax+18], #%d
        jmp returnhere_35
        %s:
        jmp newmem_35
        returnhere_35:
        [DISABLE]
        dealloc(newmem_35)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #36] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_36(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_36, 2048, %s)
        label(returnhere_36)
        newmem_36:
        mov [rax+18], #%d
        jmp returnhere_36
        %s:
        jmp newmem_36
        returnhere_36:
        [DISABLE]
        dealloc(newmem_36)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #37] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_37(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_37, 2048, %s)
        label(returnhere_37)
        newmem_37:
        mov [rax+18], #%d
        jmp returnhere_37
        %s:
        jmp newmem_37
        returnhere_37:
        [DISABLE]
        dealloc(newmem_37)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #38] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_38(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_38, 2048, %s)
        label(returnhere_38)
        newmem_38:
        mov [rax+18], #%d
        jmp returnhere_38
        %s:
        jmp newmem_38
        returnhere_38:
        [DISABLE]
        dealloc(newmem_38)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #39] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_39(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_39, 2048, %s)
        label(returnhere_39)
        newmem_39:
        mov [rax+18], #%d
        jmp returnhere_39
        %s:
        jmp newmem_39
        returnhere_39:
        [DISABLE]
        dealloc(newmem_39)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #40] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_40(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_40, 2048, %s)
        label(returnhere_40)
        newmem_40:
        mov [rax+18], #%d
        jmp returnhere_40
        %s:
        jmp newmem_40
        returnhere_40:
        [DISABLE]
        dealloc(newmem_40)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #41] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_41(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_41, 2048, %s)
        label(returnhere_41)
        newmem_41:
        mov [rax+18], #%d
        jmp returnhere_41
        %s:
        jmp newmem_41
        returnhere_41:
        [DISABLE]
        dealloc(newmem_41)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #42] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_42(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_42, 2048, %s)
        label(returnhere_42)
        newmem_42:
        mov [rax+18], #%d
        jmp returnhere_42
        %s:
        jmp newmem_42
        returnhere_42:
        [DISABLE]
        dealloc(newmem_42)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #43] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_43(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_43, 2048, %s)
        label(returnhere_43)
        newmem_43:
        mov [rax+18], #%d
        jmp returnhere_43
        %s:
        jmp newmem_43
        returnhere_43:
        [DISABLE]
        dealloc(newmem_43)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #44] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_44(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_44, 2048, %s)
        label(returnhere_44)
        newmem_44:
        mov [rax+18], #%d
        jmp returnhere_44
        %s:
        jmp newmem_44
        returnhere_44:
        [DISABLE]
        dealloc(newmem_44)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #45] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_45(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_45, 2048, %s)
        label(returnhere_45)
        newmem_45:
        mov [rax+18], #%d
        jmp returnhere_45
        %s:
        jmp newmem_45
        returnhere_45:
        [DISABLE]
        dealloc(newmem_45)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #46] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_46(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_46, 2048, %s)
        label(returnhere_46)
        newmem_46:
        mov [rax+18], #%d
        jmp returnhere_46
        %s:
        jmp newmem_46
        returnhere_46:
        [DISABLE]
        dealloc(newmem_46)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #47] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_47(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_47, 2048, %s)
        label(returnhere_47)
        newmem_47:
        mov [rax+18], #%d
        jmp returnhere_47
        %s:
        jmp newmem_47
        returnhere_47:
        [DISABLE]
        dealloc(newmem_47)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end

-- ============================================================================
-- [Lua 5.4 SUBSYSTEM #48] Auto-Assemble Code Cave Generator & Hotkey Poller
-- Purpose: Allocates executable trampolines and binds 60% keyboard Alt+Num combos.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
function AstraTrainer:InjectInfiniteResourceCave_48(targetSymbol, injectValue)
    local script = string.format([[
        [ENABLE]
        alloc(newmem_48, 2048, %s)
        label(returnhere_48)
        newmem_48:
        mov [rax+18], #%d
        jmp returnhere_48
        %s:
        jmp newmem_48
        returnhere_48:
        [DISABLE]
        dealloc(newmem_48)
    ]], targetSymbol, injectValue, targetSymbol)
    return autoAssemble(script)
end
