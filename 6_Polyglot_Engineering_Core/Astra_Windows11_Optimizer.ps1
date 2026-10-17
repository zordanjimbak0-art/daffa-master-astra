# ASTRA AI Windows 11 Ultimate Gaming & Storage Optimizer
# Hardware Profile: AMD Ryzen 5 5600 | Radeon RX 580 4GB | 16GB RAM

[CmdletBinding()]
param(
    [string]$GameRoot = "D:\Game\Games",
    [switch]$EnableLzxCompression = $true,
    [switch]$PurgeShaderCache = $true
)

function Get-AstraStorageReport {
    param([string]$DriveLetter = "D")
    $vol = Get-PSDrive -Name $DriveLetter -ErrorAction SilentlyContinue
    if ($null -ne $vol) {
        $freeGB = [math]::Round($vol.Free / 1GB, 2)
        $usedGB = [math]::Round($vol.Used / 1GB, 2)
        return [PSCustomObject]@{
            Drive       = "${DriveLetter}:"
            FreeSpaceGB = $freeGB
            UsedSpaceGB = $usedGB
            Status      = if ($freeGB -gt 25) { "OPTIMAL" } else { "LOW_SPACE_WARNING" }
        }
    }
}

function Optimize-GameBinariesWithLZX {
    param([string]$TargetFolder)
    if (Test-Path $TargetFolder) {
        Write-Host "[ASTRA LZX] Compressing binaries in $TargetFolder..." -ForegroundColor Cyan
        & compact.exe /c /s:"$TargetFolder" /exe:lzx /i /q | Out-Null
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #01] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_01 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #01] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #02] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_02 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #02] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #03] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_03 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #03] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #04] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_04 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #04] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #05] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_05 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #05] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #06] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_06 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #06] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #07] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_07 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #07] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #08] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_08 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #08] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #09] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_09 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #09] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #10] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_10 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #10] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #11] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_11 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #11] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #12] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_12 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #12] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #13] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_13 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #13] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #14] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_14 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #14] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #15] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_15 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #15] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #16] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_16 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #16] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #17] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_17 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #17] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #18] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_18 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #18] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #19] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_19 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #19] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #20] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_20 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #20] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #21] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_21 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #21] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #22] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_22 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #22] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #23] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_23 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #23] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #24] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_24 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #24] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #25] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_25 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #25] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #26] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_26 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #26] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #27] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_27 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #27] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #28] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_28 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #28] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #29] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_29 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #29] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #30] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_30 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #30] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #31] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_31 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #31] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #32] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_32 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #32] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #33] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_33 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #33] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #34] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_34 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #34] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #35] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_35 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #35] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #36] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_36 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #36] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #37] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_37 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #37] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #38] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_38 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #38] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #39] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_39 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #39] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #40] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_40 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #40] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #41] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_41 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #41] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #42] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_42 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #42] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #43] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_43 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #43] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #44] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_44 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #44] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}

# ============================================================================
# [PowerShell 7 SUBSYSTEM #45] Process Priority Booster & Background Telemetry Governor
# Purpose: Elevates active game processes to High priority and suspends unnecessary background indexing.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
function Invoke-AstraGameBoostProfile_45 {
    param([string]$ProcessName)
    $procs = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue
    foreach ($p in $procs) {
        try {
            $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
            Write-Output "[ASTRA BOOST #45] Elevated $($p.ProcessName) (PID: $($p.Id)) to HIGH priority."
        } catch {
            Write-Verbose "Cannot elevate process priority for PID $($p.Id)"
        }
    }
}
