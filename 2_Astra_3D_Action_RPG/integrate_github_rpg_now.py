import os
import shutil
import subprocess
import urllib.request

BASE_DIR = r"D:\Game\DAFFA_GAMES\rpg_3d"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
TEX_DIR = os.path.join(ASSETS_DIR, "textures")
MOD_DIR = os.path.join(ASSETS_DIR, "models")
ICONS_DIR = os.path.join(ASSETS_DIR, "icons")
QUICK_RPG_RES = os.path.join(BASE_DIR, "github_rpg_repo", "Quick_3D_RPG", "resources")

os.makedirs(ICONS_DIR, exist_ok=True)

# 1. Copy textures and weapon/skill icons from cloned Quick_3D_RPG into assets/
copied_rpg_files = []
if os.path.exists(QUICK_RPG_RES):
    for root, dirs, files in os.walk(QUICK_RPG_RES):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            src = os.path.join(root, f)
            if ext in (".png", ".jpg", ".jpeg"):
                rel_folder = os.path.basename(root).lower()
                if "icon" in rel_folder or "weapon" in rel_folder:
                    dst = os.path.join(ICONS_DIR, f)
                else:
                    dst = os.path.join(TEX_DIR, f"rpg_{f}")
                if not os.path.exists(dst):
                    shutil.copy2(src, dst)
                copied_rpg_files.append(f)
            elif ext in (".glb", ".gltf"):
                dst = os.path.join(MOD_DIR, f)
                if not os.path.exists(dst):
                    shutil.copy2(src, dst)
                copied_rpg_files.append(f)

print(f"[OK] Copied {len(copied_rpg_files)} RPG textures/icons/assets from Quick_3D_RPG repository.")

# 2. Inject GitHub PBR Textures & 3D GLB Models into index.html using exact variable names
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Clean up any previous injection if present
start_tag = "// === GITHUB REAL PBR TEXTURES & 3D GLB MODELS INTEGRATION ==="
end_tag = "// === END GITHUB REAL PBR TEXTURES & 3D GLB MODELS INTEGRATION ==="
if start_tag in html and end_tag in html:
    s = html.index(start_tag)
    e = html.index(end_tag) + len(end_tag)
    html = html[:s] + html[e:]

github_js = """
    // === GITHUB REAL PBR TEXTURES & 3D GLB MODELS INTEGRATION ===
    const githubTexLoader = new THREE.TextureLoader();

    function loadGitHubTex(url, repX = 1, repY = 1, srgb = true) {
        const t = githubTexLoader.load(url, (tex) => {
            tex.wrapS = THREE.RepeatWrapping;
            tex.wrapT = THREE.RepeatWrapping;
            tex.repeat.set(repX, repY);
            if (srgb) tex.encoding = THREE.sRGBEncoding;
            tex.needsUpdate = true;
        });
        t.wrapS = THREE.RepeatWrapping;
        t.wrapT = THREE.RepeatWrapping;
        t.repeat.set(repX, repY);
        if (srgb) t.encoding = THREE.sRGBEncoding;
        return t;
    }

    const ghFloorDiff = loadGitHubTex('assets/textures/floor_paving_diffuse.jpg', 32, 32, true);
    const ghFloorNorm = loadGitHubTex('assets/textures/floor_paving_normal.jpg', 32, 32, false);
    const ghWallDiff  = loadGitHubTex('assets/textures/dungeon_stone_diffuse.jpg', 18, 3, true);
    const ghWallBump  = loadGitHubTex('assets/textures/dungeon_stone_bump.jpg', 18, 3, false);
    const ghWallRough = loadGitHubTex('assets/textures/dungeon_stone_roughness.jpg', 18, 3, false);
    const ghPillarDiff = loadGitHubTex('assets/textures/dungeon_stone_diffuse.jpg', 2, 4, true);
    const ghPillarBump = loadGitHubTex('assets/textures/dungeon_stone_bump.jpg', 2, 4, false);
    const ghWoodDiff  = loadGitHubTex('assets/textures/wood_hardwood_diffuse.jpg', 2, 2, true);
    const ghWoodBump  = loadGitHubTex('assets/textures/wood_hardwood_bump.jpg', 2, 2, false);
    const ghLavaDiff  = loadGitHubTex('assets/textures/lava_tile.jpg', 28, 28, true);
    const ghGrassDiff = loadGitHubTex('assets/textures/terrain_grass.jpg', 28, 28, true);

    let githubTextureMode = 0;
    const githubTextureModeNames = [
        "GITHUB PBR: ROYAL CITADEL PAVING",
        "GITHUB PBR: ELDERWOOD COURTYARD GRASS",
        "GITHUB PBR: CRIMSON BRICK & LAVA",
        "PROCEDURAL: OBSIDIAN RUNIC CRYPT"
    ];

    function applyGitHubPBRTextures(mode) {
        githubTextureMode = mode % 4;
        if (typeof floorMat !== 'undefined') {
            if (githubTextureMode === 0) {
                floorMat.map = ghFloorDiff;
                floorMat.normalMap = ghFloorNorm;
                floorMat.normalScale = new THREE.Vector2(0.85, 0.85);
                floorMat.bumpMap = null;
                floorMat.color.setHex(0xe2e8f0);
                floorMat.roughness = 0.55;
                floorMat.metalness = 0.15;
            } else if (githubTextureMode === 1) {
                floorMat.map = ghGrassDiff;
                floorMat.normalMap = ghFloorNorm;
                floorMat.normalScale = new THREE.Vector2(0.4, 0.4);
                floorMat.bumpMap = null;
                floorMat.color.setHex(0xd9f99d);
                floorMat.roughness = 0.75;
                floorMat.metalness = 0.05;
            } else if (githubTextureMode === 2) {
                floorMat.map = ghLavaDiff;
                floorMat.normalMap = null;
                floorMat.bumpMap = ghWallBump;
                floorMat.bumpScale = 0.12;
                floorMat.color.setHex(0xffedd5);
                floorMat.roughness = 0.6;
                floorMat.metalness = 0.2;
            } else {
                floorMat.map = floorTex;
                floorMat.normalMap = null;
                floorMat.bumpMap = floorBump;
                floorMat.bumpScale = 0.08;
                floorMat.color.setHex(0xffffff);
                floorMat.roughness = 0.75;
                floorMat.metalness = 0.25;
            }
            floorMat.needsUpdate = true;
        }

        if (typeof wallMat !== 'undefined') {
            wallMat.map = (githubTextureMode === 3) ? wallTex : ghWallDiff;
            wallMat.bumpMap = (githubTextureMode === 3) ? null : ghWallBump;
            wallMat.bumpScale = 0.12;
            wallMat.roughnessMap = (githubTextureMode === 3) ? null : ghWallRough;
            wallMat.color.setHex(0xe2e8f0);
            wallMat.needsUpdate = true;
        }

        if (typeof colMat !== 'undefined') {
            colMat.map = (githubTextureMode === 3) ? pillarTex : ghPillarDiff;
            colMat.bumpMap = (githubTextureMode === 3) ? null : ghPillarBump;
            colMat.bumpScale = 0.1;
            colMat.color.setHex(0xe2e8f0);
            colMat.needsUpdate = true;
        }

        if (typeof chests !== 'undefined') {
            chests.forEach(c => {
                if (c.group) {
                    c.group.traverse(child => {
                        if (child.isMesh && child.material && child.material.metalness < 0.5) {
                            child.material.map = ghWoodDiff;
                            child.material.bumpMap = ghWoodBump;
                            child.material.bumpScale = 0.05;
                            child.material.color.setHex(0xfef3c7);
                            child.material.needsUpdate = true;
                        }
                    });
                }
            });
        }
    }

    // Apply GitHub PBR Textures immediately on startup
    applyGitHubPBRTextures(0);

    // Load Real 3D .GLB Assets from GitHub into the Sanctuary Arena (near Player Spawn z=50)
    const githubModelsGroup = new THREE.Group();
    scene.add(githubModelsGroup);
    const githubAnimMixers = [];

    if (typeof THREE.GLTFLoader !== 'undefined') {
        const gltfLoader = new THREE.GLTFLoader();

        // 1. Royal Vanguard Guard (Soldier.glb) - Standing guard at (4.5, 0, 44) in front of player spawn
        gltfLoader.load('assets/models/Soldier.glb', (gltf) => {
            const soldier = gltf.scene;
            soldier.scale.set(2.2, 2.2, 2.2);
            soldier.position.set(4.5, 0, 43.5);
            soldier.rotation.y = Math.PI * 0.15;
            soldier.traverse(c => {
                if (c.isMesh) {
                    c.castShadow = true;
                    c.receiveShadow = true;
                }
            });
            githubModelsGroup.add(soldier);
            if (gltf.animations && gltf.animations.length > 0) {
                const mixer = new THREE.AnimationMixer(soldier);
                mixer.clipAction(gltf.animations[0]).play();
                githubAnimMixers.push(mixer);
            }
        });

        // 2. Ancient Dwemer Automaton (RobotExpressive.glb) - Next to Blacksmith Forge at (-5.5, 0, 43.5)
        gltfLoader.load('assets/models/RobotExpressive.glb', (gltf) => {
            const robot = gltf.scene;
            robot.scale.set(0.85, 0.85, 0.85);
            robot.position.set(-5.5, 0, 43.5);
            robot.rotation.y = Math.PI * 0.15;
            robot.traverse(c => {
                if (c.isMesh) {
                    c.castShadow = true;
                    c.receiveShadow = true;
                }
            });
            githubModelsGroup.add(robot);
            if (gltf.animations && gltf.animations.length > 0) {
                const mixer = new THREE.AnimationMixer(robot);
                const idleClip = gltf.animations.find(a => a.name.toLowerCase().includes('idle')) || gltf.animations[0];
                if (idleClip) mixer.clipAction(idleClip).play();
                githubAnimMixers.push(mixer);
            }
        });

        // 3. Relic of the Fallen Star (DamagedHelmet.glb from Khronos GitHub) - Floating at Sanctuary Pedestal (0, 2.8, 41)
        gltfLoader.load('assets/models/DamagedHelmet.glb', (gltf) => {
            const helmet = gltf.scene;
            helmet.scale.set(1.35, 1.35, 1.35);
            helmet.position.set(0, 2.8, 41.0);
            helmet.traverse(c => {
                if (c.isMesh) {
                    c.castShadow = true;
                    c.receiveShadow = true;
                }
            });
            githubModelsGroup.add(helmet);
            window.githubRelicHelmet = helmet;
        });

        // 4. Royal War Steed (Horse.glb from GitHub) - Near Campfire at (9.5, 0, 46.5)
        gltfLoader.load('assets/models/Horse.glb', (gltf) => {
            const horse = gltf.scene;
            horse.scale.set(0.018, 0.018, 0.018);
            horse.position.set(9.5, 0, 46.5);
            horse.rotation.y = -Math.PI * 0.25;
            horse.traverse(c => {
                if (c.isMesh) {
                    c.castShadow = true;
                    c.receiveShadow = true;
                }
            });
            githubModelsGroup.add(horse);
        });
    }

    // Bind Key 'G' to cycle GitHub PBR Texture Themes live
    window.addEventListener('keydown', (e) => {
        if (e.code === 'KeyG' && RPG.state === 'PLAYING') {
            applyGitHubPBRTextures(githubTextureMode + 1);
            showAlert(githubTextureModeNames[githubTextureMode], '#38bdf8');
        }
    });
    // === END GITHUB REAL PBR TEXTURES & 3D GLB MODELS INTEGRATION ===
"""

anchor = "const animClock = new THREE.Clock();"
assert anchor in html, "Could not find animClock anchor!"
html = html.replace(anchor, github_js + "\n    " + anchor, 1)

# Hook animation mixer & floating relic update into renderLoop()
delta_anchor = "const dt = Math.min(rawDelta, 0.05);"
delta_replacement = """const dt = Math.min(rawDelta, 0.05);
        if (typeof githubAnimMixers !== 'undefined') {
            for (let m of githubAnimMixers) m.update(dt);
        }
        if (window.githubRelicHelmet) {
            window.githubRelicHelmet.rotation.y += dt * 0.95;
            window.githubRelicHelmet.position.y = 2.8 + Math.sin(performance.now() * 0.003) * 0.25;
        }"""

if "for (let m of githubAnimMixers)" not in html:
    html = html.replace(delta_anchor, delta_replacement, 1)

# Add [G] Texture Pack hint in controls bar
if "[G] GitHub PBR" not in html and "[V] Kamera (1ST/3RD)" in html:
    html = html.replace("[V] Kamera (1ST/3RD)", "[V] Kamera (1ST/3RD) &bull; [G] GitHub PBR Texture")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("[OK] Injected GitHub PBR Textures & 3D GLB Models into index.html!")

# Verify syntax with node --check
js_blocks = [p.split("</script>")[0] for p in html.split("<script>")[1:]]
tmp_js = os.path.join(BASE_DIR, "_check_final.js")
with open(tmp_js, "w", encoding="utf-8") as f:
    f.write("\n".join(js_blocks))

res = subprocess.run(["node", "--check", tmp_js], capture_output=True, text=True)
if os.path.exists(tmp_js):
    os.remove(tmp_js)

if res.returncode != 0:
    print("[FAIL] JS Syntax Error:", res.stderr)
    raise SystemExit(1)

print("[OK] node --check PASSED (Zero JS Syntax Errors!)")
