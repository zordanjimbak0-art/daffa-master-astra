extends CharacterBody3D
class_name AstraFirstPersonHero

signal health_changed(current_hp: float, max_hp: float)
signal stamina_changed(current_sp: float, max_sp: float)
signal combo_executed(combo_step: int, damage_dealt: float)

@export_group("Movement Parameters")
@export var walk_speed: float = 6.5
@export var sprint_speed: float = 11.0
@export var jump_velocity: float = 5.8
@export var dash_impulse: float = 16.5

@export_group("Combat Frame Data")
@export var base_sword_damage: float = 45.0
@export var critical_multiplier: float = 2.0
@export var parry_window_seconds: float = 0.22
@export var iframe_duration: float = 0.35

var current_hp: float = 1000.0
var max_hp: float = 1000.0
var current_stamina: float = 100.0
var combo_index: int = 0
var is_parrying: bool = false
var invulnerable_timer: float = 0.0

func _physics_process(delta: float) -> void:
    if invulnerable_timer > 0.0:
        invulnerable_timer = max(0.0, invulnerable_timer - delta)
    if not is_on_floor():
        velocity.y -= 14.8 * delta
    move_and_slide()

func execute_melee_combo() -> float:
    combo_index = (combo_index % 3) + 1
    var mult: float = 1.0 + (float(combo_index) * 0.35)
    var total_dmg: float = base_sword_damage * mult
    emit_signal("combo_executed", combo_index, total_dmg)
    return total_dmg

# ============================================================================
# [GDScript 2.0 SUBSYSTEM #01] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_01:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_01(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #02] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_02:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_02(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #03] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_03:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_03(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #04] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_04:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_04(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #05] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_05:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_05(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #06] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_06:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_06(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #07] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_07:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_07(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #08] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_08:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_08(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #09] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_09:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_09(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #10] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_10:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_10(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #11] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_11:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_11(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #12] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_12:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_12(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #13] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_13:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_13(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #14] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_14:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_14(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #15] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_15:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_15(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #16] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_16:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_16(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #17] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_17:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_17(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #18] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_18:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_18(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #19] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_19:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_19(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #20] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_20:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_20(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #21] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_21:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_21(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #22] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_22:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_22(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #23] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_23:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_23(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #24] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_24:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_24(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #25] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_25:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_25(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #26] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_26:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_26(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #27] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_27:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_27(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #28] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_28:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_28(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #29] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_29:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_29(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #30] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_30:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_30(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #31] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_31:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_31(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #32] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_32:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_32(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #33] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_33:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_33(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #34] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_34:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_34(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #35] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_35:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_35(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #36] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_36:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_36(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"


# ============================================================================
# [GDScript 2.0 SUBSYSTEM #37] Boss AI Finite State Machine (FSM) & Aggro Threat Evaluator
# Purpose: Controls multi-phase boss attack patterns, poise stagger thresholds, and AOE telegraphs.
# Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
# ============================================================================
class BossStateController_37:
    var boss_hp: float = 5000.0
    var poise_meter: float = 120.0
    var current_phase: int = 1

    func evaluate_boss_decision_37(dist_to_player: float, player_parrying: bool) -> String:
        if boss_hp < 2500.0 and current_phase == 1:
            current_phase = 2
            return "PHASE_2_ENRAGE_NOVA"
        if poise_meter <= 0.0:
            poise_meter = 120.0
            return "STAGGERED_VULNERABLE"
        if dist_to_player <= 3.2:
            return "HEAVY_CLEAVE_COMBO" if not player_parrying else "FEINT_BACKSTEP"
        elif dist_to_player <= 14.0:
            return "LEAP_SLAM_STRIKE"
        return "CAST_VOID_PROJECTILE"

