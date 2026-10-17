#!/usr/bin/env python3
"""
ASTRA AI â€” Portable Executable (PE64), Unity Mono DLL & Entropy Security Auditor
Author: Komandan Muhamad Daffa Cahya (zordanjimbak0-art)
"""
import os
import json
import sys
import math
import struct
from collections import Counter

def calculate_shannon_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = Counter(data)
    length = len(data)
    return -sum((c / length) * math.log2(c / length) for c in counts.values())

def inspect_pe_binary(file_path: str) -> dict:
    with open(file_path, "rb") as f:
        raw = f.read(4096)
        full_sample = f.read(256 * 1024)
    if len(raw) < 64 or raw[:2] != b"MZ":
        return {"file": file_path, "valid_pe": False}
    pe_offset = struct.unpack("<I", raw[0x3C:0x40])[0]
    machine = struct.unpack("<H", raw[pe_offset + 4:pe_offset + 6])[0] if pe_offset + 6 <= len(raw) else 0
    arch = "x64 (AMD64)" if machine == 0x8664 else ("x86 (i386)" if machine == 0x014C else hex(machine))
    entropy = calculate_shannon_entropy(raw + full_sample)
    return {
        "file": os.path.basename(file_path),
        "valid_pe": True,
        "architecture": arch,
        "entropy_bits": round(entropy, 3),
        "packed_or_encrypted_suspect": entropy > 7.2
    }

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else sys.executable
    print(json.dumps(inspect_pe_binary(target), indent=2))

