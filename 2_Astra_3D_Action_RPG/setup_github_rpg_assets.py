import os
import shutil
import subprocess
import urllib.request
import json

BASE_DIR = r"D:\Game\DAFFA_GAMES\rpg_3d"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
TEX_DIR = os.path.join(ASSETS_DIR, "textures")
MOD_DIR = os.path.join(ASSETS_DIR, "models")
GITHUB_REPO_DIR = os.path.join(BASE_DIR, "github_rpg_repo")

os.makedirs(TEX_DIR, exist_ok=True)
os.makedirs(MOD_DIR, exist_ok=True)
os.makedirs(GITHUB_REPO_DIR, exist_ok=True)

print("=== [1/4] DOWNLOADING REAL GITHUB PBR TEXTURES & 3D GLB ASSETS ===")

# Verified raw GitHub URLs from mrdoob/three.js & KhronosGroup/glTF-Sample-Assets
GITHUB_TEXTURES = {
    "dungeon_stone_diffuse.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/brick_diffuse.jpg",
    "dungeon_stone_bump.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/brick_bump.jpg",
    "dungeon_stone_roughness.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/brick_roughness.jpg",
    "floor_paving_diffuse.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/floors/FloorsCheckerboard_S_Diffuse.jpg",
    "floor_paving_normal.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/floors/FloorsCheckerboard_S_Normal.jpg",
    "wood_chest_diffuse.gif": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/crate.gif",
    "wood_hardwood_diffuse.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/hardwood2_diffuse.jpg",
    "wood_hardwood_bump.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/hardwood2_bump.jpg",
    "wood_hardwood_roughness.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/hardwood2_roughness.jpg",
    "water_normal.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/waternormals.jpg",
    "lava_cloud.png": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/lava/cloud.png",
    "lava_tile.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/lava/lavatile.jpg",
    "terrain_grass.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/terrain/grasslight-big.jpg",
    "stone_normal.jpg": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/normal/ninja/normal.jpg",
}

GITHUB_MODELS = {
    "Soldier.glb": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/models/gltf/Soldier.glb",
    "RobotExpressive.glb": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/models/gltf/RobotExpressive/RobotExpressive.glb",
    "DamagedHelmet.glb": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "Horse.glb": "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/models/gltf/Horse.glb",
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

downloaded_textures = []
for filename, url in GITHUB_TEXTURES.items():
    dest = os.path.join(TEX_DIR, filename)
    if not os.path.exists(dest) or os.path.getsize(dest) < 100:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp, open(dest, "wb") as f:
                f.write(resp.read())
            print(f"  [OK] Texture: {filename} ({os.path.getsize(dest):,} bytes)")
            downloaded_textures.append(filename)
        except Exception as e:
            print(f"  [WARN] Failed {filename}: {e}")
    else:
        print(f"  [CACHED] Texture: {filename} ({os.path.getsize(dest):,} bytes)")
        downloaded_textures.append(filename)

downloaded_models = []
for filename, url in GITHUB_MODELS.items():
    dest = os.path.join(MOD_DIR, filename)
    if not os.path.exists(dest) or os.path.getsize(dest) < 1000:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=25) as resp, open(dest, "wb") as f:
                f.write(resp.read())
            print(f"  [OK] 3D Model: {filename} ({os.path.getsize(dest):,} bytes)")
            downloaded_models.append(filename)
        except Exception as e:
            print(f"  [WARN] Failed {filename}: {e}")
    else:
        print(f"  [CACHED] 3D Model: {filename} ({os.path.getsize(dest):,} bytes)")
        downloaded_models.append(filename)

# Also copy any local 3D GLB models from D:\Game\DAFFA_GAMES\models_3d if present
local_models_dir = r"D:\Game\DAFFA_GAMES\models_3d"
if os.path.exists(local_models_dir):
    for f in os.listdir(local_models_dir):
        if f.lower().endswith((".glb", ".gltf")):
            src = os.path.join(local_models_dir, f)
            dst = os.path.join(MOD_DIR, f)
            if not os.path.exists(dst):
                shutil.copy2(src, dst)
                print(f"  [LOCAL GLB COPIED] {f} ({os.path.getsize(dst):,} bytes)")
            if f not in downloaded_models:
                downloaded_models.append(f)

print("\n=== [2/4] CLONING OPEN-SOURCE GITHUB 3D RPG REPOSITORY (Quick_3D_RPG) ===")
quick_rpg_dir = os.path.join(GITHUB_REPO_DIR, "Quick_3D_RPG")
if not os.path.exists(quick_rpg_dir):
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", "https://github.com/simondevyoutube/Quick_3D_RPG.git", quick_rpg_dir],
            check=True,
            timeout=45
        )
        print(f"  [OK] Cloned simondevyoutube/Quick_3D_RPG to {quick_rpg_dir}")
    except Exception as e:
        print(f"  [WARN] git clone Quick_3D_RPG skipped/failed: {e}")
else:
    print(f"  [CACHED] GitHub RPG Repo already at {quick_rpg_dir}")

# Copy any textures/icons from Quick_3D_RPG/resources into assets if available
rpg_res_dir = os.path.join(quick_rpg_dir, "resources")
if os.path.exists(rpg_res_dir):
    print(f"  [INFO] Found Quick_3D_RPG resources folder: {os.listdir(rpg_res_dir)[:10]}")

print("\n=== [3/4] INTEGRATING GITHUB PBR TEXTURES & 3D GLB MODELS INTO index.html ===")
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove any old githubAssetBlock if re-running
if "// === GITHUB REAL PBR TEXTURES & 3D GLB MODELS INTEGRATION ===" in html:
    start_idx = html.index("// === GITHUB REAL PBR TEXTURES & 3D GLB MODELS INTEGRATION ===")
    end_marker = "// === END GITHUB REAL PBR TEXTURES & 3D GLB MODELS INTEGRATION ==="
    if end_marker in html:
        end_idx = html.index(end_marker) + len(end_marker)
        html = html[:start_idx] + html[end_idx:]

github_integration_js = """
        // === GITHUB REAL PBR TEXTURES & 3D GLB MODELS INTEGRATION ===
        const githubTexLoader = new THREE.TextureLoader();
        const githubTextures = {};

        function loadGitHubTexture(key, url, repeatX = 1, repeatY = 1, isSRGB = true) {
            const tex = githubTexLoader.load(url, (t) => {
                t.wrapS = THREE.RepeatWrapping;
                t.wrapT = THREE.RepeatWrapping;
                t.repeat.set(repeatX, repeatY);
                if (isSRGB) t.encoding = THREE.sRGBEncoding;
                t.needsUpdate = true;
            });
            tex.wrapS = THREE.RepeatWrapping;
            tex.wrapT = THREE.RepeatWrapping;
            tex.repeat.set(repeatX, repeatY);
            if (isSRGB) tex.encoding = THREE.sRGBEncoding;
            githubTextures[key] = tex;
            return tex;
        }

        // Load real GitHub PBR textures from local /assets/textures/
        const ghFloorDiff = loadGitHubTexture('floorDiff', 'assets/textures/floor_paving_diffuse.jpg', 28, 28, true);
        const ghFloorNorm = loadGitHubTexture('floorNorm', 'assets/textures/floor_paving_normal.jpg', 28, 28, false);
        const ghWallDiff  = loadGitHubTexture('wallDiff', 'assets/textures/dungeon_stone_diffuse.jpg', 2, 4, true);
        const ghWallBump  = loadGitHubTexture('wallBump', 'assets/textures/dungeon_stone_bump.jpg', 2, 4, false);
        const ghWallRough = loadGitHubTexture('wallRough', 'assets/textures/dungeon_stone_roughness.jpg', 2, 4, false);
        const ghWoodDiff  = loadGitHubTexture('woodDiff', 'assets/textures/wood_hardwood_diffuse.jpg', 2, 2, true);
        const ghWoodBump  = loadGitHubTexture('woodBump', 'assets/textures/wood_hardwood_bump.jpg', 2, 2, false);
        const ghCrateDiff = loadGitHubTexture('crateDiff', 'assets/textures/wood_chest_diffuse.gif', 1, 1, true);
        const ghLavaDiff  = loadGitHubTexture('lavaDiff', 'assets/textures/lava_tile.jpg', 4, 4, true);
        const ghGrassDiff = loadGitHubTexture('grassDiff', 'assets/textures/terrain_grass.jpg', 24, 24, true);

        let githubTextureMode = 0; // 0 = GitHub Stone Dungeon PBR, 1 = GitHub Ancient Brick & Lava PBR, 2 = GitHub Emerald Courtyard Grass PBR, 3 = Procedural Dark Fantasy
        const githubTextureModeNames = [
            "GITHUB PBR:ROYAL CITADEL PAVING",
            "GITHUB PBR: CRIMSON BRICK & LAVA",
            "GITHUB PBR: ELDERWOOD COURTYARD",
            "PROCEDURAL: ASTRA CUSTOM SHADER"
        ];

        function applyGitHubPBRTextures(mode) {
            githubTextureMode = mode % 4;
            if (typeof floor !== 'undefined' && floor.material) {
                if (githubTextureMode === 0) {
                    floor.material.map = ghFloorDiff;
                    floor.material.normalMap = ghFloorNorm;
                    floor.material.normalScale = new THREE.Vector2(0.85, 0.85);
                    floor.material.color.setHex(0xd8e2f0);
                    floor.material.roughness = 0.55;
                } else if (githubTextureMode === 1) {
                    ghWallDiff.repeat.set(24, 24);
                    floor.material.map = ghWallDiff;
                    floor.material.bumpMap = ghWallBump;
                    floor.material.bumpScale = 0.15;
                    floor.material.color.setHex(0xffb899);
                    floor.material.roughness = 0.65;
                } else if (githubTextureMode === 2) {
                    floor.material.map = ghGrassDiff;
                    floor.material.normalMap = ghFloorNorm;
                    floor.material.color.setHex(0xb8f5c8);
                    floor.material.roughness = 0.75;
                } else {
                    floor.material.map = stoneTex;
                    floor.material.bumpMap = stoneBump;
                    floor.material.color.setHex(0x8a9bb8);
                    floor.material.roughness = 0.65;
                }
                floor.material.needsUpdate = true;
            }

            // Apply GitHub brick/stone PBR to dungeon pillars & walls
            if (typeof pillarMat !== 'undefined') {
                pillarMat.map = (githubTextureMode === 3) ? wallBrickTex : ghWallDiff;
                pillarMat.bumpMap = (githubTextureMode === 3) ? stoneBump : ghWallBump;
                pillarMat.roughnessMap = (githubTextureMode === 3) ? null : ghWallRough;
                pillarMat.color.setHex(0xc8d4e8);
                pillarMat.needsUpdate = true;
            }

            // Apply GitHub wood/crate texture to loot chests
            if (typeof chests !== 'undefined') {
                chests.forEach(c => {
                    if (c.mesh) {
                        c.mesh.traverse(child => {
                            if (child.isMesh && child.material && child.material.color) {
                                // Apply hardwood/crate texture to wooden chest body
                                if (child.material.metalness < 0.5) {
                                    child.material.map = ghWoodDiff;
                                    child.material.bumpMap = ghWoodBump;
                                    child.material.bumpScale = 0.05;
                                    child.material.needsUpdate = true;
                                }
                            }
                        });
                    }
                });
            }
        }

        // Apply GitHub PBR textures immediately by default!
        applyGitHubPBRTextures(0);

        // Load Real 3D .GLB Models from GitHub (/assets/models/)
        const githubModelsGroup = new THREE.Group();
        scene.add(githubModelsGroup);
        const githubAnimMixers = [];
        const loadedGitHubAssets = [];

        if (typeof THREE.GLTFLoader !== 'undefined') {
            const gltfLoader = new THREE.GLTFLoader();

            // 1. Royal Vanguard Knight (Soldier.glb from Three.js GitHub) - Allied Companion near Elder Vaelin
            gltfLoader.load('assets/models/Soldier.glb', (gltf) => {
                const soldier = gltf.scene;
                soldier.scale.set(1.65, 1.65, 1.65);
                soldier.position.set(-4.5, 0, -5.5);
                soldier.rotation.y = Math.PI * 0.25;
                soldier.traverse(c => {
                    if (c.isMesh) {
                        c.castShadow = true;
                        c.receiveShadow = true;
                    }
                });
                githubModelsGroup.add(soldier);
                loadedGitHubAssets.push('Soldier.glb');
                if (gltf.animations && gltf.animations.length > 0) {
                    const mixer = new THREE.AnimationMixer(soldier);
                    const idleAction = mixer.clipAction(gltf.animations[0]);
                    idleAction.play();
                    githubAnimMixers.push(mixer);
                }
            }, undefined, (err) => console.warn('Soldier.glb load note:', err));

            // 2. Ancient Dwemer Automaton Guardian (RobotExpressive.glb from GitHub) - Near Blacksmith Forge
            gltfLoader.load('assets/models/RobotExpressive.glb', (gltf) => {
                const robot = gltf.scene;
                robot.scale.set(0.65, 0.65, 0.65);
                robot.position.set(8.5, 0, -4.5);
                robot.rotation.y = -Math.PI * 0.35;
                robot.traverse(c => {
                    if (c.isMesh) {
                        c.castShadow = true;
                        c.receiveShadow = true;
                    }
                });
                githubModelsGroup.add(robot);
                loadedGitHubAssets.push('RobotExpressive.glb');
                if (gltf.animations && gltf.animations.length > 0) {
                    const mixer = new THREE.AnimationMixer(robot);
                    const idleClip = gltf.animations.find(a => a.name.toLowerCase().includes('idle')) || gltf.animations[0];
                    if (idleClip) mixer.clipAction(idleClip).play();
                    githubAnimMixers.push(mixer);
                }
            }, undefined, (err) => console.warn('RobotExpressive.glb load note:', err));

            // 3. Relic of the Fallen Star (DamagedHelmet.glb from Khronos GitHub) - Floating Legendary Artifact on Altar
            gltfLoader.load('assets/models/DamagedHelmet.glb', (gltf) => {
                const helmet = gltf.scene;
                helmet.scale.set(1.1, 1.1, 1.1);
                helmet.position.set(0, 2.4, -10.0);
                helmet.traverse(c => {
                    if (c.isMesh) {
                        c.castShadow = true;
                        c.receiveShadow = true;
                        if (c.material) {
                            c.material.emissiveIntensity = 1.4;
                        }
                    }
                });
                githubModelsGroup.add(helmet);
                window.githubRelicHelmet = helmet;
                loadedGitHubAssets.push('DamagedHelmet.glb');
            }, undefined, (err) => console.warn('DamagedHelmet.glb load note:', err));

            // 4. Spectral War Steed (Horse.glb from GitHub) - Mount near Sanctuary Gate
            gltfLoader.load('assets/models/Horse.glb', (gltf) => {
                const horse = gltf.scene;
                horse.scale.set(0.014, 0.014, 0.014);
                horse.position.set(-8.5, 0, -3.5);
                horse.rotation.y = Math.PI * 0.35;
                horse.traverse(c => {
                    if (c.isMesh) {
                        c.castShadow = true;
                        c.receiveShadow = true;
                    }
                });
                githubModelsGroup.add(horse);
                loadedGitHubAssets.push('Horse.glb');
            }, undefined, (err) => console.warn('Horse.glb load note:', err));
        }

        // Add Key 'G' to cycle GitHub PBR Texture Packs live in-game
        window.addEventListener('keydown', (e) => {
            if (e.code === 'KeyG' && typeof gameActive !== 'undefined' && gameActive) {
                applyGitHubPBRTextures(githubTextureMode + 1);
                if (typeof showBanner === 'function') {
                    showBanner(githubTextureModeNames[githubTextureMode], '#38bdf8');
                }
            }
        });
        // === END GITHUB REAL PBR TEXTURES & 3D GLB MODELS INTEGRATION ===
"""

# Insert right before `const clock = new THREE.Clock();` so all scene/floor/camera/chests are already initialized
target_anchor = "const clock = new THREE.Clock();"
if target_anchor in html:
    html = html.replace(target_anchor, github_integration_js + "\n        " + target_anchor, 1)
    print("  [OK] Injected GitHub PBR Textures & GLB Models loader before clock initialization.")
else:
    print("  [ERROR] Could not find `const clock = new THREE.Clock();` anchor!")

# Also update the animation loop so githubAnimMixers and floating DamagedHelmet relic animate smoothly
anim_hook = "const dt = Math.min(clock.getDelta(), 0.1);"
anim_addition = """const dt = Math.min(clock.getDelta(), 0.1);
            if (typeof githubAnimMixers !== 'undefined') {
                for (let m of githubAnimMixers) m.update(dt);
            }
            if (window.githubRelicHelmet) {
                window.githubRelicHelmet.rotation.y += dt * 0.9;
                window.githubRelicHelmet.position.y = 2.4 + Math.sin(performance.now() * 0.003) * 0.25;
            }"""

if "for (let m of githubAnimMixers) m.update(dt);" not in html and anim_hook in html:
    html = html.replace(anim_hook, anim_addition, 1)
    print("  [OK] Hooked GitHub GLB AnimationMixers & Relic rotation into main render loop.")

# Add [G] Texture Pack hint to HUD controls bar if not already there
if "[G] GitHub PBR" not in html and "[V] Camera" in html:
    html = html.replace("[V] Camera", "[V] Camera | [G] GitHub PBR")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("\n=== [4/4] SYNTAX & HTTP ASSET VERIFICATION ===")
js_blocks = []
parts = html.split("<script>")
for p in parts[1:]:
    code = p.split("</script>")[0]
    js_blocks.append(code)

temp_js = os.path.join(BASE_DIR, "_verify_gh.js")
with open(temp_js, "w", encoding="utf-8") as f:
    f.write("\n".join(js_blocks))

res = subprocess.run(["node", "--check", temp_js], capture_output=True, text=True)
if os.path.exists(temp_js):
    os.remove(temp_js)

if res.returncode == 0:
    print("  [OK] node --check PASSED (Zero JS Syntax Errors!)")
else:
    print("  [FAIL] node --check error:\n", res.stderr)
    raise SystemExit(1)

# Verify HTTP 200 on localhost:9998 for index.html and downloaded assets
for check_path in ["/", "/assets/textures/floor_paving_diffuse.jpg", "/assets/textures/dungeon_stone_diffuse.jpg", "/assets/models/Soldier.glb", "/assets/models/DamagedHelmet.glb"]:
    url = f"http://127.0.0.1:9998{check_path}"
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            print(f"  [HTTP {r.status}] {url}")
    except Exception as e:
        print(f"  [HTTP WARN] {url} -> {e}")

print("\n=== ALL DONE! ===")
