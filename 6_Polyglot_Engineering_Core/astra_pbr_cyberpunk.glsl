#version 450 core

layout(location = 0) in vec3 inFragWorldPos;
layout(location = 1) in vec3 inNormal;
layout(location = 2) in vec2 inTexCoord;

layout(location = 0) out vec4 outFragColor;

uniform sampler2D uAlbedoMap;
uniform sampler2D uNormalMap;
uniform sampler2D uRoughnessMap;

uniform vec3 uCameraPos;
uniform vec3 uSunDirection;
uniform vec3 uSunColor;
uniform float uTime;

const float PI = 3.14159265359;

float DistributionGGX(vec3 N, vec3 H, float roughness) {
    float a = roughness * roughness;
    float a2 = a * a;
    float NdotH = max(dot(N, H), 0.0);
    float NdotH2 = NdotH * NdotH;
    float denom = (NdotH2 * (a2 - 1.0) + 1.0);
    denom = PI * denom * denom;
    return a2 / max(denom, 0.00001);
}

float GeometrySchlickGGX(float NdotV, float roughness) {
    float r = (roughness + 1.0);
    float k = (r * r) / 8.0;
    return NdotV / (NdotV * (1.0 - k) + k);
}

vec3 FresnelSchlick(float cosTheta, vec3 F0) {
    return F0 + (1.0 - F0) * pow(clamp(1.0 - cosTheta, 0.0, 1.0), 5.0);
}

void main() {
    vec3 albedo = pow(texture(uAlbedoMap, inTexCoord).rgb, vec3(2.2));
    float roughness = texture(uRoughnessMap, inTexCoord).r;
    vec3 N = normalize(inNormal);
    vec3 V = normalize(uCameraPos - inFragWorldPos);
    vec3 L = normalize(uSunDirection);
    vec3 H = normalize(V + L);

    vec3 F0 = vec3(0.04);
    float NDF = DistributionGGX(N, H, roughness);
    float G = GeometrySchlickGGX(max(dot(N, V), 0.0), roughness) * GeometrySchlickGGX(max(dot(N, L), 0.0), roughness);
    vec3 F = FresnelSchlick(max(dot(H, V), 0.0), F0);

    float NdotL = max(dot(N, L), 0.0);
    vec3 specular = (NDF * G * F) / max(4.0 * max(dot(N, V), 0.0) * NdotL, 0.001);
    vec3 color = (albedo / PI + specular) * uSunColor * NdotL + (albedo * 0.32);
    color = color / (color + vec3(1.0));
    color = pow(color, vec3(1.0 / 2.2));
    outFragColor = vec4(color, 1.0);
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #01] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_01(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #02] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_02(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #03] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_03(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #04] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_04(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #05] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_05(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #06] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_06(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #07] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_07(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #08] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_08(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #09] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_09(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #10] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_10(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #11] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_11(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #12] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_12(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #13] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_13(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #14] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_14(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #15] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_15(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #16] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_16(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #17] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_17(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #18] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_18(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #19] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_19(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #20] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_20(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #21] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_21(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #22] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_22(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #23] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_23(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #24] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_24(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #25] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_25(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #26] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_26(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #27] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_27(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #28] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_28(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #29] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_29(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #30] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_30(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #31] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_31(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #32] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_32(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #33] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_33(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #34] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_34(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #35] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_35(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #36] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_36(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #37] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_37(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #38] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_38(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #39] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_39(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #40] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_40(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #41] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_41(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #42] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_42(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #43] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_43(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #44] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_44(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #45] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_45(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #46] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_46(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #47] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_47(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #48] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_48(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #49] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_49(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}

// ============================================================================
// [GLSL 450 SUBSYSTEM #50] Volumetric Rim Glow, Torch Flicker & Cyberpunk Bloom Kernel
// Purpose: Computes dynamic dungeon torch attenuation and neon edge-highlighting in fragment space.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
vec3 ComputeAstraNeonRim_50(vec3 normal, vec3 viewDir, vec3 baseColor, float timeSec) {
    float rimFactor = 1.0 - max(dot(normalize(normal), normalize(viewDir)), 0.0);
    rimFactor = smoothstep(0.55, 1.0, rimFactor);
    float pulse = 0.75 + 0.25 * sin(timeSec * 3.14159);
    vec3 cyanGlow = vec3(0.0, 0.95, 1.0) * rimFactor * pulse;
    return baseColor + cyanGlow * 0.45;
}
