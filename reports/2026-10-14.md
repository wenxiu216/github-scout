📊 开源日报 — 2026-10-14
共发现 5 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  xtool-org/xtool
    ⭐ 9709 stars  |  🍴 410 forks  |  💻 Swift  |  📅 2024-11-17
    🔗 https://github.com/xtool-org/xtool
    📡 来源: trending-daily
    🏷️ ios, linux, swift, swift-package-manager, windows, xcode
    📝 Cross-platform Xcode replacement. Build and deploy iOS apps with SwiftPM on Linux, Windows, macOS.

    README 摘要:
    # xtool
    
    Cross-platform Xcode replacement. Build and deploy iOS apps with SwiftPM on Linux, Windows, and macOS.
    
    ## Overview
    
    xtool is a cross-platform (Linux/WSL/macOS) tool that replicates Xcode functionality with open standards.
    
    ✅ Build a SwiftPM package into an iOS app
    
    ✅ Sign and install iOS apps
    
    ✅ Interact with Apple Developer Services programmatically
    
    ## Getting Started
    
    1. Follow the guide to install `xtool`
        - Installation (Linux/Windows)
        - Installation (macOS)
    2. Create and run your first xtool-powered app by following the tutorial!
    
    ## Examples
    
    ### Screenshot
    
    ### Command line interface
    
    ```bash
    $ xtool --help
    OVERVIEW: Cross-platform Xcode replacement
    
    USAGE: xtool 
    
    OPTIONS:
      -h, --help              Show help information.
    
    CONFIGURATION SUBCOMMANDS:
      setup                   Set up xtool for iOS development
      auth                    Manage Apple Developer Services authentication
      sdk                     Manage the Darwin Swift SDK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  storytold/designcraft
    ⭐ 3752 stars  |  🍴 2527 forks  |  💻 Rust  |  📅 2026-10-01
    🔗 https://github.com/storytold/designcraft
    📡 来源: 🚀 两周800+星
    🏷️ art, layout, print, rust
    📝 DesignCraft: An open-source page and layout design editor written by scratch in pure Rust

    README 摘要:
    DesignCraft
    
      Page layout and publishing; an open-source, clean-room reimplementation of Adobe InDesign, rebuilt in pure Rust.
    
      A fast, open-source, clean-room take on the Adobe InDesign workflow. It runs natively on macOS,
      Windows and Linux, and in the browser via WebAssembly.
      By the ArtCraft team.
    
      
      
      
      
    
      
    
      DesignCraft on getartcraft.com ·
      ArtCraft ·
      All Crafting Apps
    
      
      Quarterly, Spring Issue: threaded three-column body text, a wrapped pull quote and parent-page folios, all set by DesignCraft's own paragraph composer.
    
    > [!NOTE]
    > **ArtCraft is a community of artists from all walks of life.** Digital, generative, music,
    > games &mdash; if you make things, you're one of us. **Come say hi on Discord.**
    
      The sample magazine ·
      Why DesignCraft ·
      Quick start ·
      Web ·
      Architecture ·
      Downloads ·
      The Crafting Apps ·
      License and credits
    
    ## The sample magazine
    
    Every page below was laid out by DesignCraft from code (`crates/engine/src/sample.rs`) and exported
    by its own renderer. Try it yourself with `File → New → Sample Document`, or start the app with
    `--sample`.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  Arekejoker/qwen21-nsfw-pose-skill
    ⭐ 984 stars  |  🍴 221 forks  |  💻 Python  |  📅 2026-10-13
    🔗 https://github.com/Arekejoker/qwen21-nsfw-pose-skill
    📡 来源: 🚀 5天300+星
    🏷️ agent-skill, comfyui, image-generation, openclaw, pose-control, qwen-image
    📝 Qwen-Image 2.1 NSFW/姿势出图 skill：作者级提示词配方 + NSFW LoRA + 136 姿势 VNCCS 人偶控制；适用 Claude Code / Codex / Cursor / OpenClaw

    README 摘要:
    # qwen21-nsfw-pose
    
    **Qwen-Image 2.1 本地 NSFW / 姿势出图完整配方** — 作者级提示词结构 + NSFW LoRA + 136 个 3D 姿势库 + VNCCS 人偶精确姿势控制。
    
    基于 ComfyUI + `qwen_image_2.1_int8_convrot` 底模（与 Civitai 作者同款底模），复刻并验证过 Civitai 作者样图（2026-10-12）。
    
    - 适用：Claude Code / Codex / Cursor / OpenClaw（agent 技能）+ 人类手动使用
    - 内容：可跟跑的作者案例、强制配方、姿势大胆度阶梯（L0–L3）、完整依赖与安装指南
    
    ---
    
    ## 效果展示
    
    ### 本配方输出：同一海边场景的三级对照（L0 → L1 → L2）
    
    | L0 · 全着装，无 LoRA（提示词即全部） | L1 · 湿身泳装 + LoRA@1.0 | L2 · 极低机位 + 湿身蹲姿 + LoRA@1.0 |
    | --- | --- | --- |
    |  |  |  |
    
    三张图同场景递进：L0 只有提示词；L1 加 LoRA + 显式皮肤/水珠描写；L2 再加低机位与开合姿态。**LoRA 负责质感，提示词负责信息密度，机位负责大胆度。**
    
    ### NSFW 效果（⚠️ 以下图片包含裸露内容）
    
    **作者原图**（Civitai showcase，本配方复刻的目标）：
    
    | 作者 · 淋浴（tawsLoRa） | 作者 · 按摩（tawsLoRa） | 作者 · 自拍（TheseAlpacas） |
    | --- | --- | --- |
    |  |  |  |
    
    用 §「快速开始」的命令可复刻淋浴那张（复刻输出已验证与作者原图同场景同构图，见 `downloads/samples/phase5_meta.json` 与本文快速开始一节）。
    
    ### 3D 人偶精确姿势（Route ④，136 姿势库）
    
    默认人物图 `references/src_standing.png`；姿势 = 骨骼旋转 JSON（MakeHuman 网格 + three.js 渲染），
    换姿势且保身份。姿势库来源：HuggingFace 4 个公开仓库（`Totemistyk/General_Poses`、
    `Totemistyk/Ballet_PoseStudio`、`MIUProject/VNCCS_PoseLibrary_Main`、
    `MIUProject/MySuperPoseRepo`）+ 55 个手工精选，共 **136 个**。
    
    ---
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  opengeos/RustGIS
    ⭐ 848 stars  |  🍴 115 forks  |  💻 Rust  |  📅 2026-10-10
    🔗 https://github.com/opengeos/RustGIS
    📡 来源: 🚀 5天300+星
    🏷️ geospatial, gis, remote-sensing, rust, rust-lang
    📝 A fast, free and open-source GIS in pure Rust.

    README 摘要:
    RustGIS
    
      A fast, free and open-source GIS in pure Rust for mapping, analyzing and sharing geospatial data.
      Native on Windows, macOS and Linux, and in your web browser. Your data stays on your machine
      unless you send it to an AI model you choose, and every action is a command you can script.
    
      
      
      
      
      
      
    
      
      
      
    
      
    
    ## Why RustGIS
    
    - **Fast and small.** One native program, drawn on the GPU, with no runtime to install and no
      server to run.
    - **Runs everywhere.** The same app on Windows, macOS and Linux, and compiled to WebAssembly at
      web.rustgis.app with nothing to install.
    - **Local and private.** Your files are read and written on your machine, and nothing is uploaded
      on its own. The network is used only when you ask for it: web basemaps, plugins, the GeoLibre
      tools and the AI model you pick, which receives your questions and the data it reads to answer
      them.
    - **Everything is a command.** Every button in the ribbon is a command with an id. Script it from
      `rustgis-cli`, chain it in notebooks and models, or ask the AI Assistant to run it for you.
    - **Familiar.** A ribbon laid out in the order of the work (Home, Data, Style, Edit, Analyze,
      View, Publish), Layers and Browser panes, an attribute table, and undo for every change.
    - **Extensible.** Over 1,000 GeoLibre and Whitebox tools for terrain, hydrology, LiDAR and remote sensing, and
      sandboxed WebAssembly plugins that add commands, tools and ribbon tabs.
    
    ## A tour
    
    Symbology and tables. Selecting a layer opens its contextual tabs: symbology, effects, labeling and data. Selection is synced between the map and the attribute table.
    AI Assistant. Ask about your data or tell the map what to do. The assistant runs RustGIS commands for you, and each change can be undone.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  jwuthri-cloud/Tracely-ai
    ⭐ 761 stars  |  🍴 107 forks  |  💻 Python  |  📅 2026-10-11
    🔗 https://github.com/jwuthri-cloud/Tracely-ai
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # Tracely
    
    ### Production failures become regression tests.
    
    **Trace-native CI/CD for AI agents.** Tracely grades every agent trace as it lands, clusters the
    failures into issues, freezes the bad runs into hermetic replayable cases, blocks the pull request
    that would ship them again — and tells you the moment any of it happens.
    
    production trace → failure detection → regression test → CI gate → alert
    
    **Website** · **Docs** · **Product guide** · **Agent skill** · **Guided tour** · **2-min demo** · **Design dossier**
    
         
    
    **Self-host the whole stack in one click** — API, worker, UI, Postgres, ClickHouse, Redis and MinIO:
    
    One workspace: what ran, what broke, what is already pinned as a test.
    
    ---
    
    ## Why another agent-observability tool?
    
    Because observability stops at the dashboard. You can see that your agent broke — then what?
    
    Every eval tool asks you to **hand-author a dataset**: sit down, invent questions, write ideal
    answers, keep them current as the product changes. That dataset is a guess about what might break.
    
    Production already handed you the real thing: a trace of the exact run that failed, with the exact
    input, the exact tool calls, the exact model responses.
    
    > **The recorded run _is_ the test.** Tracely freezes that trace into a hermetic regression case and
    > replays it on every PR. Everything else — quality scores, failure clusters, suggested fixes, CI
    > verdicts, trends, alerts — is **derived from the trace**. There are no hand-authored datasets.
    
    |  | Dataset-first tools | Tracely |
    |---|---|---|
    | Where tests come from | You write them | Promoted from real failing traces |
    | Fidelity to production | A guess | The exact failing run, byte for byte |
    | Cost to replay in CI | Live model calls | **$0** — recorded tool/LLM fixtures |
    | What happens on regression | A dashboard number moves | **The PR is blocked** |
