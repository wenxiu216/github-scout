📊 开源日报 — 2026-11-25
共发现 5 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  xcl-dev/xcl
    ⭐ 8052 stars  |  🍴 1087 forks  |  💻 Rust  |  📅 2026-11-20
    🔗 https://github.com/xcl-dev/xcl
    📡 来源: 🚀 两周800+星
    🏷️ d3d12, gdk, rdna2, xbox
    📝 Xbox Series compatibility layer for Windows - runs console game code natively, reimplements the console system libraries and recompiles RDNA2 shaders to DXIL

    README 摘要:
    Games ·
      Highlights ·
      How it works ·
      Quick start ·
      What works ·
      Controls ·
      Building and usage ·
      Tests ·
      Contributing
    
    # XCL – Xbox Series X|S → Windows compatibility layer
    
    XCL is a compatibility layer that runs Xbox Series X|S (GDK) games you own on a Windows PC - in the spirit of Wine/Proton. There is no CPU emulation: the game's x64 code runs natively, and XCL provides its own, independently written implementations of the console system libraries the PC does not have (`kernelx.dll`, XGameRuntime, `d3d12_xs.dll`, …). The console's GPU code (RDNA2 machine code) is recompiled into PC shaders (HLSL → DXIL).
    
    > [!IMPORTANT]
    > XCL works only on unpacked game files you already own. It does not download, decrypt or unpack game packages (XVC / MSIXVC) and contains nothing for circumventing DRM. The repository holds no code, headers or binaries from the console SDK, no keys and no game data; the Windows components XCL relies on (XGameRuntime, XAudio2, D3D12, DXC) come from your own system or the public Windows SDK and are not distributed with XCL.
    
    ## Games
    
      
    
    | Game | State | What works | Limits |
    |---|---|---|---|
    | **Minecraft Preview**`Microsoft.MinecraftBeta` 1.18.3064.0 | ✅&nbsp;playable | fully playable | – |
    | **Unicorn Overlord**`SEGAofAmericaInc.Pa253b0c1Y` 1.0.0.6 | ✅&nbsp;playable | fully playable | – |
    | **Fortnite**`436609B6.FortniteClient` 2.0.1461.7919 | ✅&nbsp;works | works fully, as far as the game allows without its online services | the game itself is online-only (multiplayer servers) |
    | **XDefiant**`Ubisoft.XDefiant-Game` 1.0.0.186 | ✅&nbsp;works | works fully, as far as the game allows without its servers | the game's own servers have been shut down |
    | **A newer retail game** | 🚧&nbsp;**≈&nbsp;60&nbsp;%**estimate | starts in ~4 s, runs at a steady 30 fps without a crash, shows its menus and goes on past the first one to its settings; fits a 32 GB machine (~15 GB committed in the menus). With the NVIDIA integration branch (#2057) it goes on into its 3D world: **~5 fps there** on an RTX 5090 (14 fps on average over a whole 5-minute run, its menus and loading included) | not playable yet: the picture of the world is incomplete (its minimap and other mesh pipelines are refused), and it does not keep running there for long |
    
    ## Highlights
    
      
        
          
          No CPU emulation – the game's x64 code runs natively, in the spirit of Wine / Proton.
        
        
          
          100 % of a retail game's shaders t

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  fxceless/victory-fork
    ⭐ 2514 stars  |  🍴 662 forks  |  💻 Rust  |  📅 2026-11-24
    🔗 https://github.com/fxceless/victory-fork
    📡 来源: 🚀 5天300+星
    📝 Work-in-progress fork of VIctory: getting an Xbox Series title to render and run on a Windows PC. No game files.

    README 摘要:
    # VIctory fork (work in progress)
    
    A work-in-progress fork of VIctory, a
    compatibility layer that runs an Xbox Series title natively on Windows from
    files the user supplies. This fork follows upstream
    `main` and adds fixes aimed at one goal: getting the game's world to render
    correctly and playably on one particular PC.
    
    **This repository contains no game files, code or assets.** You need your own
    copy of the game. It is not affiliated with or endorsed by the game's
    developer or publisher.
    
    ## Credits
    
    - **VIctory** by Marvisak and its
      contributors is the base of everything here: the loader, the runtime
      services, the Direct3D 12 back end and the shader recompiler. Licensed
      GPL-3.0-or-later; so is this fork. Upstream's history is kept intact below
      the single commit that carries this fork's changes.
    - **XCL** by ivall and its contributors
      (GPL-2.0-only) was used as a reference for how the same title behaves under
      another layer. Fixes inspired by it were written anew in VIctory's code.
    - The guard over every view of a memory page is code by **myokex**
      (victory-amd, commit `c6dc4d8`), which
      adapts pull request #115 here by Spexivus, its correction by joroyt and a part of
      VIctory #1122 by tightfall. The read-beside fix for kernel reads into title
      memory is by **Joshua Odom** (commit `10ea38e` of the same fork family). Both
      are carried here unchanged apart from one merge conflict.
    - This fork's changes were developed with Claude Code.
    
    ## Status of this fork (2026-11-25)
    
    **Not playable yet: 2.5 to 4 frames per second, and shadowed areas are black.**
    Tested on one machine: Windows 11, Intel i7-14700KF, NVIDIA RTX 4070 12 GB,
    32 GB RAM. The Series X profile is used throughout.
    
    | Stage | State in this fork |
    |-------|--------------------|
    | Boot, menus, start screen | works, 30 fps (as upstream) |
    | Opening cutscene | plays from start to finish, in order, lit: title cards, credits cards, night and dusk shots |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  Indigo-0167/universal-game-mod-manager
    ⭐ 1181 stars  |  🍴 0 forks  |  💻 Rust  |  📅 2026-11-23
    🔗 https://github.com/Indigo-0167/universal-game-mod-manager
    📡 来源: 🚀 5天300+星
    🏷️ automation, desktop, epic-games, game-development, game-engine, game-mods, game-tools, gaming, gog, itch
    📝 Free Windows game mod manager to discover, install, update and manage universal Unity and Unreal Engine mods.

    README 摘要:
    **Universal Game Mod Manager is a free, open-source Windows desktop application for discovering, installing, updating, and managing universal PC game mods.** Designed for gamers and VR enthusiasts, it makes cross-game modding accessible through a simple graphical interface, with no command line required.
    
    ## ⬇️ Installation
    
    **Download the Windows application**
    
    1. Open the repository's Releases page.
    2. Download the latest release archive **`Universal Game Mod Manager 4.0.3.zip`**.
    3. Extract the archive into a folder of your choice.
    4. Keep **`Universal Game Mod Manager 4.0.3.exe`** and `libvlc.dll` together in that folder.
    5. Double-click **`Universal Game Mod Manager 4.0.3.exe`** to launch the application.
    
    ## ✨ Features
    
    - 🎮 **Automatic Game Discovery** — Find installed PC games across supported game launchers without manually searching through installation directories.
    - 🧩 **Universal Mod Installation** — Discover and install compatible mods designed to work across multiple games using the same underlying engine.
    - 🔍 **Game Engine Detection** — Identify whether a game uses Unity, Unreal Engine, or another supported technology and detect relevant engine information.
    - 🚀 **Unreal Engine Mod Support** — Manage universal Unreal Engine modifications and compatible tools for supported games.
    - 🔄 **One-Click Mod Updates** — Check for newer mod releases and conveniently update installed components.
    - 📚 **Centralized Mod Library** — Keep track of supported games, installed modifications, and available versions from one desktop application.
    - 🖥️ **Multi-Store Game Detection** — Discover games from supported PC gaming platforms, including Steam, GOG, Epic Games, itch.io, and Xbox.
    
    ## 🖼️ Overview
    
    ### A smarter approach to PC game modding
    
    Traditional mod managers often focus on individual games. Universal modding tools take a different approach: one modification can potentially support multiple games built on the same engine.
    
    This application helps bridge that gap by identifying games, detecting their technical characteristics, and making relevant universal modifications easier to manage.
    
    ### Supported game discovery
    
    The application can inspect locally available game library information to identify games from supported providers.
    
    | Game platform | Installed games | Owned games |
    |---|---|---|
    | Steam | Automatic detection | Library detection |
    | GOG | Automatic detection | Library detection |
    | Epic Games | Automatic detection | Library d

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  ⚠️风险  Zettrox/ztrx
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 1176 stars  |  🍴 212 forks  |  💻 Rust  |  📅 2026-11-25
    🔗 https://github.com/Zettrox/ztrx
    📡 来源: 🚀 5天300+星
    📝 Run the Xbox Series build of the game natively on Windows PCs with NVIDIA GPUs

    README 摘要:
    # ztrx
    
    **ztrx** runs the Xbox Series build of the game natively on Windows PCs with
    NVIDIA graphics cards, from game files you supply yourself.
    
    **This repository contains no game files or assets.** You need your own copy
    of the game. Not affiliated with or endorsed by its developer or publisher.
    
    ## Status (2026-11-25)
    
    Tested on Windows 11 with an **NVIDIA GeForce RTX 3050** (8 GB):
    
    | | |
    |---|---|
    | Boot, first-boot screens, intro, opening credits | works |
    | Prologue | playable from the cell to the boat chase: cell, cafeteria, robbery, police chase (wanted level, minimap), boat, binoculars |
    | Stability | 1 h 30 min+ in one session without a crash |
    | Frame rate | 1-3 fps in the world (the first run is slower while shaders translate; they are cached after that) |
    | Known problems | anything in shadow is black and bright scenes overexpose (the game's ray-traced lighting does not run yet); some blocky artifacts; boats sit low in the water |
    
    ## Requirements
    
    - Windows 10/11 x64, a CPU with AVX2
    - A Direct3D 12 GPU with shader model 6.6 and mesh shaders (NVIDIA RTX 20 series or newer)
    - Rust (the version in `rust-toolchain.toml`)
    - Several GB of free Windows commit memory (raise the paging file if `crashes.log` reports error 1455)
    
    ## Build
    
    ```powershell
    cargo build --release -p victory
    ```
    
    ## Play
    
    ```powershell
    powershell -ExecutionPolicy Bypass -File scripts\play.ps1 -Game "\"
    ```
    
    `scripts\play.ps1` keeps the shader cache and saves in folders you choose

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  Umbra9179/clipboard-history-manager-windows
    ⭐ 1156 stars  |  🍴 0 forks  |  💻 C#  |  📅 2026-11-23
    🔗 https://github.com/Umbra9179/clipboard-history-manager-windows
    📡 来源: 🚀 5天300+星
    🏷️ clipboard, clipboard-history, clipboard-manager, desktop-app, desktop-application, dotnet, fluent, open-source, productivity, utility
    📝 Free open-source Windows clipboard manager with searchable history, image previews, tags, editing and backup.

    README 摘要:
    **Windows Clipboard History Manager is a free, open-source clipboard manager designed to make copying, finding, editing, and reusing information effortless.** Keep a searchable history of copied text, images, files, and links in a modern Windows desktop application without using the command line.
    
    Stop losing important snippets and repeatedly copying the same information. Keep everything organized and accessible from one convenient clipboard history.
    
    ## ⬇️ Installation
    
    **Download the Windows application**
    
    1. Open the repository's Releases page.
    2. Download the latest release archive **`Windows Clipboard History Manager 4.2.1.zip`**.
    3. Extract the archive into a folder of your choice.
    4. Keep **`Windows Clipboard History Manager 4.2.1.exe`** and `libvlc.dll` together in that folder.
    5. Double-click **`Windows Clipboard History Manager 4.2.1.exe`** to launch the application.
    
    ## ✨ Features
    
    - 📋 **Unlimited Clipboard History** — Automatically maintain an extensive clipboard history so previously copied information remains available when you need it.
    - 🔎 **Instant Clipboard Search** — Search through saved clipboard entries and quickly locate text, links, images, and other copied content.
    - 🖼️ **Multiple Clipboard Formats** — Preserve formatted text, HTML, rich text, bitmap images, PNG images, and file references.
    - ✏️ **Edit Clipboard Entries** — Modify saved text and clipboard content before copying it again or sharing it with another application.
    - 🏷️ **Tags and Organization** — Add custom tags and organize clipboard entries into convenient groups for easier retrieval.
    - 🪟 **Application Filtering** — Control which source applications contribute clipboard entries and keep unwanted content out of your history.
    - 🖱️ **Drag and Drop Support** — Move supported clipboard items directly into compatible desktop applications.
    - 📌 **Always-Accessible Window** — Pin the clipboard manager window to keep your saved content accessible while multitasking.
    - ☑️ **Multiple Selection** — Select and manage several clipboard entries together for more efficient organization.
    - 🔗 **Link and Content Previews** — Recognize useful information at a glance with previews of supported clipboard data.
    - 💾 **Clipboard Backup** — Create backups of saved clipboard information to help protect your collected snippets.
    - 🎨 **Modern Windows Interface** — Work with a clean desktop interface built around the Windows application experience.
    
    ## 🖼️ Overview
    
    Explore the clipboard
