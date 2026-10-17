-- ASTRA AI Relational Database Schema (PostgreSQL / T-SQL Compatible)
-- Owner: Komandan Muhamad Daffa Cahya (zordanjimbak0-art)

CREATE TABLE IF NOT EXISTS astra_game_catalog (
    game_id VARCHAR(64) PRIMARY KEY,
    steam_app_id INTEGER NOT NULL,
    title VARCHAR(180) NOT NULL,
    genre VARCHAR(64) NOT NULL,
    executable_path VARCHAR(512) NOT NULL,
    has_astra_mod_menu BOOLEAN DEFAULT FALSE,
    lzx_compressed BOOLEAN DEFAULT TRUE,
    vram_profile_mb INTEGER DEFAULT 2048,
    cover_hd_path VARCHAR(255),
    last_played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS astra_savegame_vault_log (
    backup_id SERIAL PRIMARY KEY,
    game_id VARCHAR(64) NOT NULL,
    source_path VARCHAR(512) NOT NULL,
    git_commit_hash VARCHAR(64) NOT NULL,
    file_size_bytes BIGINT NOT NULL,
    synced_to_github BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cetak_cup_production_batches (
    batch_code VARCHAR(32) PRIMARY KEY,
    client_brand VARCHAR(120) NOT NULL,
    substrate_type VARCHAR(32) CHECK (substrate_type IN ('PP_INJECTION', 'PET_CLEAR', 'IVORY_310GSM')),
    order_quantity INTEGER NOT NULL,
    mesh_screen VARCHAR(16) DEFAULT 'T-120',
    ink_viscosity_cps NUMERIC(6,2) DEFAULT 3800.00,
    defect_rate_percent NUMERIC(5,2) DEFAULT 0.45,
    supervisor_name VARCHAR(64) DEFAULT 'Pak Rahmadi',
    production_date DATE DEFAULT CURRENT_DATE
);

-- ============================================================================
-- [SQL SUBSYSTEM #01] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_01 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_01', 4015530 + 01, 'Astra Registered Game Module #01', 'Action RPG / Simulation', 'D:/Game/Games/Module_01/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #02] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_02 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_02', 4015530 + 02, 'Astra Registered Game Module #02', 'Action RPG / Simulation', 'D:/Game/Games/Module_02/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #03] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_03 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_03', 4015530 + 03, 'Astra Registered Game Module #03', 'Action RPG / Simulation', 'D:/Game/Games/Module_03/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #04] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_04 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_04', 4015530 + 04, 'Astra Registered Game Module #04', 'Action RPG / Simulation', 'D:/Game/Games/Module_04/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #05] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_05 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_05', 4015530 + 05, 'Astra Registered Game Module #05', 'Action RPG / Simulation', 'D:/Game/Games/Module_05/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #06] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_06 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_06', 4015530 + 06, 'Astra Registered Game Module #06', 'Action RPG / Simulation', 'D:/Game/Games/Module_06/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #07] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_07 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_07', 4015530 + 07, 'Astra Registered Game Module #07', 'Action RPG / Simulation', 'D:/Game/Games/Module_07/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #08] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_08 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_08', 4015530 + 08, 'Astra Registered Game Module #08', 'Action RPG / Simulation', 'D:/Game/Games/Module_08/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #09] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_09 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_09', 4015530 + 09, 'Astra Registered Game Module #09', 'Action RPG / Simulation', 'D:/Game/Games/Module_09/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #10] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_10 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_10', 4015530 + 10, 'Astra Registered Game Module #10', 'Action RPG / Simulation', 'D:/Game/Games/Module_10/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #11] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_11 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_11', 4015530 + 11, 'Astra Registered Game Module #11', 'Action RPG / Simulation', 'D:/Game/Games/Module_11/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #12] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_12 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_12', 4015530 + 12, 'Astra Registered Game Module #12', 'Action RPG / Simulation', 'D:/Game/Games/Module_12/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #13] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_13 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_13', 4015530 + 13, 'Astra Registered Game Module #13', 'Action RPG / Simulation', 'D:/Game/Games/Module_13/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #14] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_14 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_14', 4015530 + 14, 'Astra Registered Game Module #14', 'Action RPG / Simulation', 'D:/Game/Games/Module_14/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #15] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_15 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_15', 4015530 + 15, 'Astra Registered Game Module #15', 'Action RPG / Simulation', 'D:/Game/Games/Module_15/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #16] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_16 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_16', 4015530 + 16, 'Astra Registered Game Module #16', 'Action RPG / Simulation', 'D:/Game/Games/Module_16/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #17] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_17 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_17', 4015530 + 17, 'Astra Registered Game Module #17', 'Action RPG / Simulation', 'D:/Game/Games/Module_17/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #18] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_18 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_18', 4015530 + 18, 'Astra Registered Game Module #18', 'Action RPG / Simulation', 'D:/Game/Games/Module_18/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #19] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_19 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_19', 4015530 + 19, 'Astra Registered Game Module #19', 'Action RPG / Simulation', 'D:/Game/Games/Module_19/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #20] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_20 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_20', 4015530 + 20, 'Astra Registered Game Module #20', 'Action RPG / Simulation', 'D:/Game/Games/Module_20/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #21] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_21 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_21', 4015530 + 21, 'Astra Registered Game Module #21', 'Action RPG / Simulation', 'D:/Game/Games/Module_21/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #22] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_22 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_22', 4015530 + 22, 'Astra Registered Game Module #22', 'Action RPG / Simulation', 'D:/Game/Games/Module_22/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #23] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_23 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_23', 4015530 + 23, 'Astra Registered Game Module #23', 'Action RPG / Simulation', 'D:/Game/Games/Module_23/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #24] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_24 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_24', 4015530 + 24, 'Astra Registered Game Module #24', 'Action RPG / Simulation', 'D:/Game/Games/Module_24/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #25] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_25 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_25', 4015530 + 25, 'Astra Registered Game Module #25', 'Action RPG / Simulation', 'D:/Game/Games/Module_25/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #26] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_26 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_26', 4015530 + 26, 'Astra Registered Game Module #26', 'Action RPG / Simulation', 'D:/Game/Games/Module_26/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #27] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_27 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_27', 4015530 + 27, 'Astra Registered Game Module #27', 'Action RPG / Simulation', 'D:/Game/Games/Module_27/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #28] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_28 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_28', 4015530 + 28, 'Astra Registered Game Module #28', 'Action RPG / Simulation', 'D:/Game/Games/Module_28/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #29] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_29 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_29', 4015530 + 29, 'Astra Registered Game Module #29', 'Action RPG / Simulation', 'D:/Game/Games/Module_29/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #30] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_30 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_30', 4015530 + 30, 'Astra Registered Game Module #30', 'Action RPG / Simulation', 'D:/Game/Games/Module_30/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #31] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_31 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_31', 4015530 + 31, 'Astra Registered Game Module #31', 'Action RPG / Simulation', 'D:/Game/Games/Module_31/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #32] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_32 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_32', 4015530 + 32, 'Astra Registered Game Module #32', 'Action RPG / Simulation', 'D:/Game/Games/Module_32/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #33] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_33 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_33', 4015530 + 33, 'Astra Registered Game Module #33', 'Action RPG / Simulation', 'D:/Game/Games/Module_33/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #34] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_34 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_34', 4015530 + 34, 'Astra Registered Game Module #34', 'Action RPG / Simulation', 'D:/Game/Games/Module_34/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #35] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_35 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_35', 4015530 + 35, 'Astra Registered Game Module #35', 'Action RPG / Simulation', 'D:/Game/Games/Module_35/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #36] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_36 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_36', 4015530 + 36, 'Astra Registered Game Module #36', 'Action RPG / Simulation', 'D:/Game/Games/Module_36/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #37] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_37 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_37', 4015530 + 37, 'Astra Registered Game Module #37', 'Action RPG / Simulation', 'D:/Game/Games/Module_37/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #38] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_38 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_38', 4015530 + 38, 'Astra Registered Game Module #38', 'Action RPG / Simulation', 'D:/Game/Games/Module_38/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #39] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_39 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_39', 4015530 + 39, 'Astra Registered Game Module #39', 'Action RPG / Simulation', 'D:/Game/Games/Module_39/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #40] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_40 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_40', 4015530 + 40, 'Astra Registered Game Module #40', 'Action RPG / Simulation', 'D:/Game/Games/Module_40/Game.exe', TRUE, 2048);

-- ============================================================================
-- [SQL SUBSYSTEM #41] Analytical DMAIC Quality & Game Telemetry Aggregation View
-- Purpose: Computes Pareto defect ratios and hardware frame-time percentiles across sessions.
-- Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
-- ============================================================================
CREATE VIEW vw_astra_telemetry_summary_41 AS
SELECT
    g.genre AS game_category,
    COUNT(g.game_id) AS total_installed_games,
    SUM(CASE WHEN g.has_astra_mod_menu = TRUE THEN 1 ELSE 0 END) AS modded_games_count,
    AVG(g.vram_profile_mb) AS avg_vram_allocation_mb
FROM astra_game_catalog g
GROUP BY g.genre;

INSERT INTO astra_game_catalog (game_id, steam_app_id, title, genre, executable_path, has_astra_mod_menu, vram_profile_mb)
VALUES ('GAME_ENTRY_41', 4015530 + 41, 'Astra Registered Game Module #41', 'Action RPG / Simulation', 'D:/Game/Games/Module_41/Game.exe', TRUE, 2048);
