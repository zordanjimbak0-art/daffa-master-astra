import re

HTML_PATH = r"D:\Game\DAFFA_GAMES\rpg_3d\index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Extract the misplaced 2.5 FIRST-PERSON block from before Scene Setup
fps_block_pattern = r"    // =========================================================================\n    // 2\.5 FIRST-PERSON COMBAT SYSTEM & VIEWMODEL \(HANDS & WEAPONS\)\n    // =========================================================================.*?    // =========================================================================\n    // 3\. THREE\.JS SCENE SETUP & LIGHTING"

fps_new_block = """    // =========================================================================
    // 5.8 FIRST-PERSON COMBAT SYSTEM & VIEWMODEL (HANDS, WEAPONS & LANTERN)
    // =========================================================================
    let cameraMode = 'FIRST_PERSON'; // 'FIRST_PERSON' (Default) or 'THIRD_PERSON'
    let pitch = 0; // Up/down look (-85 deg to +85 deg)
    let yaw = 0;   // Left/right look
    let isPointerLocked = false;
    let walkTimer = 0;

    // First Person Viewmodel Group + Bright Knight Lantern attached directly to Camera
    const fpsViewmodelGroup = new THREE.Group();
    camera.add(fpsViewmodelGroup);

    const fpsLanternLight = new THREE.PointLight(0xe0f2fe, 3.2, 65, 1.1);
    fpsLanternLight.position.set(0, 0.4, 0.2);
    camera.add(fpsLanternLight);

    scene.add(camera);

    // FPS Right Arm & Weapon (Runeblade / War-Axe)
    const fpsRightArm = new THREE.Group();
    fpsRightArm.position.set(0.62, -0.52, -1.05);

    // Viewmodel Forearm (Obsidian Armor + Silver Trim)
    const armFore = new THREE.Mesh(new THREE.CylinderGeometry(0.18, 0.22, 1.3, 10), obsidianArmorMat);
    armFore.rotation.x = Math.PI / 3.2;
    armFore.rotation.z = -Math.PI / 8;
    armFore.position.set(0, -0.3, 0.4);
    fpsRightArm.add(armFore);

    // Viewmodel Runeblade Sword
    const fpsSword = swordGroup.clone();
    fpsSword.scale.set(0.85, 0.85, 0.85);
    fpsSword.position.set(0.15, -0.1, -0.3);
    fpsSword.rotation.x = Math.PI / 6;
    fpsSword.rotation.y = -Math.PI / 10;
    fpsRightArm.add(fpsSword);

    // Viewmodel Infernal War-Axe
    const fpsAxe = axeGroup.clone();
    fpsAxe.scale.set(0.85, 0.85, 0.85);
    fpsAxe.position.set(0.15, -0.1, -0.3);
    fpsAxe.rotation.x = Math.PI / 6;
    fpsAxe.rotation.y = -Math.PI / 10;
    fpsAxe.visible = false;
    fpsRightArm.add(fpsAxe);

    fpsViewmodelGroup.add(fpsRightArm);

    // FPS Left Arm & Dragon Shield
    const fpsLeftArm = new THREE.Group();
    fpsLeftArm.position.set(-0.72, -0.62, -1.0);

    const shieldFore = new THREE.Mesh(new THREE.CylinderGeometry(0.18, 0.22, 1.3, 10), obsidianArmorMat);
    shieldFore.rotation.x = Math.PI / 3.2;
    shieldFore.rotation.z = Math.PI / 8;
    shieldFore.position.set(0, -0.3, 0.4);
    fpsLeftArm.add(shieldFore);

    const fpsShield = shieldMesh.clone();
    fpsShield.scale.set(0.8, 0.8, 0.8);
    fpsShield.position.set(0.2, 0.1, -0.2);
    fpsLeftArm.add(fpsShield);

    fpsViewmodelGroup.add(fpsLeftArm);

    // Pointer Lock Listeners
    function requestFpsPointerLock() {
        if (RPG.state === 'PLAYING') {
            document.body.requestPointerLock();
        }
    }
    renderer.domElement.addEventListener('click', requestFpsPointerLock);

    document.addEventListener('pointerlockchange', () => {
        isPointerLocked = (document.pointerLockElement === document.body || document.pointerLockElement === renderer.domElement);
    });

    window.addEventListener('mousemove', (e) => {
        if (isPointerLocked && cameraMode === 'FIRST_PERSON') {
            const sensitivity = 0.0022;
            yaw -= e.movementX * sensitivity;
            pitch -= e.movementY * sensitivity;
            // Clamp pitch looking up/down
            pitch = Math.max(-Math.PI / 2.25, Math.min(Math.PI / 2.25, pitch));
        }
    });

    function toggleCameraMode() {
        if (cameraMode === 'FIRST_PERSON') {
            cameraMode = 'THIRD_PERSON';
            fpsViewmodelGroup.visible = false;
            playerGroup.visible = true;
            document.getElementById('crosshair-container').style.display = 'none';
            document.getElementById('cam-tag').innerText = '3RD';
            document.getElementById('cam-tag').style.color = '#fbbf24';
            showAlert('KAMERA: THIRD-PERSON MODE', '#fbbf24');
        } else {
            cameraMode = 'FIRST_PERSON';
            fpsViewmodelGroup.visible = true;
            playerGroup.visible = false;
            document.getElementById('crosshair-container').style.display = 'flex';
            document.getElementById('cam-tag').innerText = '1ST';
            document.getElementById('cam-tag').style.color = '#38bdf8';
            showAlert('KAMERA: FIRST-PERSON FPS MODE (KLIK UNTUK KUNCI MOUSE)', '#38bdf8');
            requestFpsPointerLock();
        }
    }
"""

# Remove misplaced block
c, count = re.subn(
    fps_block_pattern,
    "    // =========================================================================\n    // 3. THREE.JS SCENE SETUP & LIGHTING",
    c,
    count=1,
    flags=re.DOTALL
)
print(f"Removed misplaced FPS block: {count}")

# Insert FPS block right before // 6. FRIENDLY NPC: ELDER VAELIN
c = c.replace(
    "    // =========================================================================\n    // 6. FRIENDLY NPC: ELDER VAELIN",
    fps_new_block + "\n    // =========================================================================\n    // 6. FRIENDLY NPC: ELDER VAELIN",
    1
)

# 2. Upgrade Scene Lighting, Exposure, Fog & Sky Background so it is bright and crystal clear
c = c.replace(
    """    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x06080c);
    scene.fog = new THREE.FogExp2(0x06080c, 0.015);""",
    """    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x162032);
    scene.fog = new THREE.FogExp2(0x162032, 0.0045);""",
    1
)

c = c.replace(
    "renderer.toneMappingExposure = 1.1;",
    "renderer.toneMappingExposure = 1.5;",
    1
)

c = c.replace(
    """    // Lights
    const ambientLight = new THREE.AmbientLight(0x1e293b, 1.2);
    scene.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0x94a3b8, 1.4);""",
    """    // High-Visibility Vivid PBR Lights
    const hemiLight = new THREE.HemisphereLight(0xbae6fd, 0x334155, 2.4);
    scene.add(hemiLight);

    const ambientLight = new THREE.AmbientLight(0x64748b, 2.2);
    scene.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xf8fafc, 2.6);""",
    1
)

# 3. Brighten Stone Floor & Wall Textures for vivid visibility
c = c.replace(
    "ctx.fillStyle = `rgb(${25 + shade}, ${33 + shade}, ${46 + shade})`;",
    "ctx.fillStyle = `rgb(${52 + shade}, ${64 + shade}, ${86 + shade})`;",
    1
)
c = c.replace(
    "ctx.fillStyle = `rgb(${22 + shade}, ${28 + shade}, ${42 + shade})`;",
    "ctx.fillStyle = `rgb(${46 + shade}, ${58 + shade}, ${82 + shade})`;",
    1
)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(c)

print("[SUCCESS] Fixed Temporal Dead Zone (TDZ) order and boosted 3D lighting & textures!")
