📊 开源日报 — 2026-10-21
共发现 9 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  vllm-project/vllm
    ⭐ 94526 stars  |  🍴 23687 forks  |  💻 Python  |  📅 2023-02-09
    🔗 https://github.com/vllm-project/vllm
    📡 来源: trending-daily
    🏷️ amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama
    📝 A high-throughput and memory-efficient inference and serving engine for LLMs

    README 摘要:
    Easy, fast, and cheap LLM serving for everyone
    
    | Documentation | Blog | Paper | Twitter/X | User Forum | Developer Slack |
    
    🔥 We have built a vLLM website to help you get started with vLLM. Please visit vllm.ai to learn more.
    For events, please visit vllm.ai/events to join us.
    
    ---
    
    ## About
    
    vLLM is a fast and easy-to-use library for LLM inference and serving.
    
    Originally developed in the Sky Computing Lab at UC Berkeley, vLLM has grown into one of the most active open-source AI projects built and maintained by a diverse community of many dozens of academic institutions and companies from over 2000 contributors.
    
    vLLM is fast with:
    
    - State-of-the-art serving throughput
    - Efficient management of attention key and value memory with **PagedAttention**
    - Continuous batching of incoming requests, chunked prefill, prefix caching
    - Fast and flexible model execution with piecewise and full CUDA/HIP graphs
    - Quantization: FP8, MXFP8/MXFP4, NVFP4, INT8, INT4, GPTQ/AWQ, GGUF, compressed-tensors, ModelOpt, TorchAO, and more
    - Optimized attention kernels including FlashAttention, FlashInfer, TRTLLM-GEN, FlashMLA, and Triton
    - Optimized GEMM/MoE kernels for various precisions using CUTLASS, TRTLLM-GEN, CuTeDSL
    - Speculative decoding including n-gram, suffix, EAGLE, DFlash
    - Automatic kernel generation and graph-level transformations using torch.compile
    - Disaggregated prefill, decode, and encode
    
    vLLM is flexible and easy to use with:
    
    - Seamless integration with popular Hugging Face models
    - High-throughput serving with various decoding algorithms, including *parallel sampling*, *beam search*, and more
    - Tensor, pipeline, data, expert, and context parallelism for distributed inference
    - Streaming outputs
    - Generation of structured outputs using xgrammar or guidance
    - Tool calling and reasoning parsers
    - OpenAI-compatible API server, plus Anthropic Messages API and gRPC support
    - Efficient multi-LoRA support for dense and MoE layers
    - Support for NVIDIA GPUs, AMD GPUs, Intel GPUs, and x86/ARM/PowerPC CPUs. Additionally, diverse hardware plugins such as Google TPUs, Intel Gaudi, IBM Spyre, Huawei Ascend, Rebellions NPU, Apple Silicon, MetaX GPU, and more.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  sickn33/agentic-awesome-skills
    ⭐ 48193 stars  |  🍴 7023 forks  |  💻 Python  |  📅 2026-01-14
    🔗 https://github.com/sickn33/agentic-awesome-skills
    📡 来源: trending-daily
    🏷️ agent-skills, agentic-skills, ai-agent-skills, ai-agents, ai-coding, ai-workflows, antigravity, antigravity-skills, claude-code, claude-code-skills
    📝 AAS Core is the local, agent-first control plane for complete catalog discovery, agent-owned selection, stack validation, and planning, backed by 2,600+ agentic skills. Includes CLI, local MCP, catalog, plugins, and Workbench.

    README 摘要:
    # AAS Core — Agentic Awesome Skills
    
    > **Find reusable instructions for your project, inspect their complete files, and keep an exact skill set you can review and reuse.**
    
    Agentic Awesome Skills is a library of 2,724+ installable `SKILL.md` playbooks. AAS Core helps Codex or Claude search the complete local catalog, record the skills the agent chooses, and preview a plan you can inspect before changing a target. Core does not rank or recommend skills.
    
    **Current release: V19.12.1.** AAS Core supports local catalog inspection, agent-owned selection, stack validation, and plan preview. Apply and recovery remain experimental. Read the AAS Core preview guide for setup and exact trust boundaries.
    
    This README tracks `main`. Features listed under Unreleased require a later release; the versioned guide describes the published package.
    
    This is an independent community project, not affiliated with or endorsed by Google. Google, Antigravity, Gemini, and related names describe compatibility and install targets. The GitHub repository is canonical; the hosted catalog and browser-local Workbench are companion discovery and review surfaces.
    
    ## Table of Contents
    
    - Watch the Introduction
    - Support the Project
    - AAS Core: Agent-First Preview
    - Installation
    - Choose Your Tool
    - Recommended Specialized Plugins
    - Bundles & Workflows
    - Browse 2,724+ Skills
    - Troubleshooting
    - Stable Skills Manifest v1
    - Contributing
    - Community
    - Credits & Sources
    - Top Contributors
    - Repo Contributors
    - Star History
    - License
    
    ## Watch the Introduction
    
    A 40-second introduction to Agentic Awesome Skills. Press play to watch it here on GitHub.
    
    https://github.com/user-attachments/assets/02aa20ca-c3bb-4984-807e-7b06ef77e785
    
    If GitHub's player stalls, watch the video on the AAS website.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  wshobson/agents
    ⭐ 41331 stars  |  🍴 4396 forks  |  💻 Python  |  📅 2025-07-24
    🔗 https://github.com/wshobson/agents
    📡 来源: trending-daily
    🏷️ agent-skills, agentic-ai, ai-agents, anthropic, antigravity, claude, claude-code, claude-code-marketplace, claude-code-plugin, claude-skills
    📝 Multi-harness agentic plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Google Antigravity, and Pi

    README 摘要:
    # Plugins, agents, and skills for AI coding tools
    
    Use one collection of plugins, agents, skills, and commands across Claude Code, OpenAI Codex CLI, Cursor, OpenCode, Antigravity CLI, GitHub Copilot, and Pi. A harness is the coding tool that loads and runs the components. Plugins cover Python and JavaScript development, code review, testing, infrastructure, security, and other work.
    
    The catalog contains 94 plugins, including 92 local plugins and 2 external entries. The local source contains 202 agents, 185 skills, and 105 commands. The components share a Markdown source, with installation and capabilities adapted to each harness.
    
    ## Multi-harness support
    
    Choose the harness you use and follow its setup route. Available components depend on the installation route and the harness's capabilities.
    
    | Tool | Installation | Components and limits |
    |---|---|---|
    | Claude Code | Plugin marketplace | Source agents, skills, and commands; plugin-specific hooks and MCP configuration |
    | OpenAI Codex CLI | Native marketplace or generated artifacts | Native source skills; generated TOML agents and commands as skills use a separate route |
    | Cursor | Plugin marketplace | Source agents, skills, and commands, with curated project rules |
    | OpenCode | `make install-opencode` | Generated agents, skills, and commands, with translated tool permissions |
    | Antigravity CLI | `make install-antigravity` | Generated plugins containing agents, skills, and commands |
    | GitHub Copilot | `make install-copilot` | Generated agent profiles and skills; commands also become invocable skills |
    | Pi | `make install-pi` | Generated skills and prompt templates; agents require a subagent extension |
    
    See the capability matrix for model mappings, tool permissions, hooks, and installation differences.
    
    For individual skills, use a skills-only installer and select your coding tool.
    
    ## Quick start
    
    Choose a plugin for the work you do:
    
    | Plugin | Use it for |
    |---|---|
    | python-development | Python, Django, FastAPI, testing, and packaging |
    | javascript-typescript | JavaScript and TypeScript development and project setup |
    | developer-essentials | Code review, debugging, Git, and testing patterns |
    | security-scanning | Security review, dependency checks, and code scanning |
    
    See the plugin catalog for all 94 plugins and the usage guide for commands and examples.
    
    ### Claude Code
    
    Run these commands inside Claude Code to register the marketplace and install the Python development plugin:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  deepseek-ai/DeepInfer
    ⭐ 14720 stars  |  🍴 1421 forks  |  💻 Python  |  📅 2026-10-16
    🔗 https://github.com/deepseek-ai/DeepInfer
    📡 来源: 🚀 两周800+星
    📝 DeepInfer: High-performance, large-scale inference framework for DeepSeek models

    README 摘要:
    # DeepInfer
    
    DeepInfer is the high-performance inference framework that powers DeepSeek's large-scale production services. This open-source release provides offline inference with the core features needed for serving at scale.
    
    Supported models:
    
    - DeepSeek-V4.1-Flash
    
    Supported features:
    
    - Optimized kernels, model and sampler runtime
    - Parallelism: Attention DP / balanced CP, MoE EP + EPLB
    - DSpark and confidence-scheduled verification
    - SWA bounded replay
    - Asynchronous scheduling (zero-overhead batch scheduler)
    - Batch-invariant inference
    - Deterministic sampling
    - Structured outputs
    
    Feature details and configuration
    
    - **Optimized kernels:** FlashMLA, DeepGEMM, DeepEP, TileKernels, DeepSelect, and custom TileLang kernels.
    - **DSpark and confidence-scheduled verification:** accelerate decoding with draft tokens and use confidence estimates to schedule verification. Set `DEEPINFER_ENABLE_MTP_VARLEN=1`; `DEEPINFER_USE_NEXTN_DECODE` controls the maximum draft length (default: 5).
    - **Decoder SWA bounded replay:** reduce decoder prefill work by replaying only a bounded suffix. Set `DEEPINFER_YOCO_PREFILL_TRUNCATION_MODE=compact` and `DEEPINFER_YOCO_PREFILL_KEEP_TOKENS=140` for the default V4.1 settings; the retained suffix must cover the SWA window plus the maximum backtracking length.
    - **Asynchronous scheduling:** overlap CPU batch scheduling with device execution. Enabled by default.
    - **Batch-invariant inference:** keep model results identical across different batch compositions. Enable with `DEEPINFER_BATCH_INVARIANT=1` (NVIDIA only).
    - **Deterministic sampling:** produce identical outputs for identical input tokens and sampling parameters. Set `DEEPINFER_BATCH_INVARIANT=1 DEEPINFER_ENABLE_MTP_VARLEN=0` and pass a fixed `seq_seed` to `SamplingParams` (NVIDIA only).
    - **Structured outputs:** constrain generation to a regex, JSON schema, or EBNF grammar. Pass `so_args={"schema_type": ..., "schema": ...}` to `SamplingParams`; see examples.
    
    Supported hardware:
    
    - NVIDIA SM100 GPUs
    - Huawei Ascend 950 NPUs
    
    Required for a complete inference service (not included in this release):
    
    - A KV cache system
    - VE/Prefill/Decode disaggregation (most required engine functionality is already implemented)
    - Load balancing across data-parallel replicas for both prefill and decode
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  T-Auto/dsh-ops
    ⭐ 3518 stars  |  🍴 100 forks  |  💻 JavaScript  |  📅 2026-10-08
    🔗 https://github.com/T-Auto/dsh-ops
    📡 来源: 🚀 两周800+星
    🏷️ dsh, dsh-plugin, dsh-plugins
    📝 A toolkit for low-level operations in DSH, designed to reduce token usage and task execution time / DSH 底层操作工具插件，旨在减少 Token 消耗与任务耗时

    README 摘要:
    中文 | English
    
      
        
      
    
      
      
      
    
    # dsh-ops
    
    以提高token效率为目的，提供新增的ops系列工具并隐藏部分官方工具为方案的插件，低改动面，低侵入性，与其他插件广泛兼容。
    
    - （仅windows平台）启用与dsh原生bash行为一致的ops_bash，并可选禁用powershell
    - 启用 DSH 预留的 `tools_addition` 动态工具加载，并提供渐进式纰漏的工具，作为高级功能（如pdf、word读取、超多文件批量修改）的加载平台，大大减少常见特定场景的token消耗量，且不会导致系统提示词膨胀
    - 为 Native 模式提供返回紧凑、带行号和更好错误回馈的工具以遏制报错循环，减少调用轮次
    - 为 PTC 模式提供一些返回结构化 JSON 值的工具以降低 ai 在 ptc 模式下编写 TypeScript 代码的token总量和心智负担
    
      
    
    在当前，dsh的token效率并不算突出。dsh-ops团队将致力于持续优化dsh的token效率
    
    ## 安装、更新、卸载
    
    ### 官方插件市场
    
    在目标 DSH 应用的插件市场中输入 npm 包名 **`dsh-ops`**，选择自定义地址，输入 `https://mirrors.huaweicloud.com/repository/npm/`，安装后选择启用。目前不推荐用npmmirror安装，有bug。
    
    当然，如果你确定可以连接 npm 官方源那就选择官方源，如果你不确定那就按教程操作。
    
    ### npm 一键安装
    
    #### 安装方法
    
    ```console
    npx --yes dsh-ops@latest install --profile desktop
    npx --yes dsh-ops@latest install --profile web
    npx --yes dsh-ops@latest install --profile tui
    ```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  simbasjungles/free-my-tv
    ⭐ 2013 stars  |  🍴 208 forks  |  💻 Java  |  📅 2026-10-19
    🔗 https://github.com/simbasjungles/free-my-tv
    📡 来源: 🚀 5天300+星
    🏷️ android-tv, claude-code, google-tv, home-screen, launcher, no-ads, open-source, tmdb
    📝 A fast, ad-free home screen for Google TV. Open source, built with Claude Code. One button to undo.

    README 摘要:
    # Free My TV
    
    **A fast, ad-free home screen for Google TV, LG and Samsung TVs.**
    
    Trending picks from your own apps, the weather at a glance, and a look that follows the sunset.
    Open source. Built with Claude Code. One button to undo.
    
    **freemytv.io** · Install · LG TVs · Samsung TVs · Any TV · Make it yours
    
    ## What you get
    
    - **No ads.** No sponsored rows, banners or autoplaying promos. Not one.
    - **Your apps, front and center.** The streaming apps you actually use, on a glass shelf. Pick them and their order right on the TV.
    - **Trending, not sponsored.** Three fresh picks every hour from what's trending this week and the latest releases, only from apps you already have. Movies and Shows get their own tabs.
    - **Weather and markets, one press away.** The hour-by-hour forecast, sunrise and sunset, and live crypto prices.
    - **Light by day, dark by night.** It follows your city's real sunset, the way your phone does.
    - **A screensaver to match.** Full-screen photos of the picks with a big glass clock.
    - **Fast.** 60 fps, every frame in 16.6 ms, on the TV's own chip. The home screen uses 96 MB of memory instead of 242 MB (−60%).Measured on a 98″ TCL Google TV running Android 14.
    - **Set up on the TV.** Language, your city, temperature, theme, the weather and prices cards, which coins, and the apps on the shelf, in Free My TV's own settings.
    - **Safe.** No root. Nothing is uninstalled. One button brings back the factory home screen.
    
    ## Install
    
    About ten minutes. You need a Google TV or Android TV (Android 9 or newer) and a computer on the same Wi-Fi.
    
    ### The easy way: Claude Code
    
    1. **On the TV**, turn on developer mode: Settings → System → About → press *Android TV OS build* 7 times. Then Settings → System → Developer options → turn on **USB debugging**. Write down the TV's IP address (Settings → Network & Internet).
    2. **On your computer**, get the code:
       ```bash
       git clone https://github.com/simbasjungles/free-my-tv && cd free-my-tv
       ```
    3. **Open Claude Code in that folder** and say:
       > Install Free My TV on my TV at 192.168.1.50. I live in Lisbon.
    
       It installs the tools it needs, builds the app and puts it on your TV. Swap in your TV's IP and your city.
    4. **On the TV**, open *Free My TV* → *Home Screen* → *Free My TV*, and accept the debugging prompt (tick *Always allow*).
    
    ### The manual way
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  ⚠️风险  JoasASantos/REA-Prompts
    ⚠️ 命中风险词: vulnerability research, bypass —— 默认归排除区，需人工确认
    ⭐ 1108 stars  |  🍴 162 forks  |  💻 None  |  📅 2026-10-19
    🔗 https://github.com/JoasASantos/REA-Prompts
    📡 来源: 🚀 5天300+星
    🏷️ prompt-engineering, rea, reverse-enginnering
    📝 REAP - Prompts for you to use REA (Reverse Engineer Anything), get the most out of it, and clone or break down any program

    README 摘要:
    # REA Investigation Prompts (REAP) — Reverse Engineering with your Coding Agent
    
    A curated collection of prompts for REA (Reverse Engineer Anything) — the toolset that lets your AI coding agent inspect how software works, from native binaries, firmware and kernels to games, Electron apps, APKs and websites.
    
    Prompts are ready to paste into your agent. Replace everything in `` and keep each request focused on **one feature** — narrow questions get evidence-backed answers.
    
    ## Sources & credits
    
    - **REA tools & guides:** https://rea.tools/
    - **Official prompt gallery:** https://madewithrea.com/prompts
    - **Intro thread ("REA is the most dangerous thing on the internet right now")** by codila — https://x.com/0xCodila/status/2109623431763292649
      (quoting Matthew Berman — https://x.com/MatthewBerman/status/2108245653843509415)
    - **REAP Name** by https://x.com/zazencodes?s=11
    ## Table of contents
    
    | # | Section |
    |---|---------|
    | 0 | Install & verify |
    | 1 | Getting started |
    | 2 | Feature tracing (any program) |
    | 3 | Native binary exploration |
    | 4 | Software & feature cloning |
    | 5 | Games |
    | 6 | Game portability to WASM |
    | 7 | Firmware & embedded |
    | 8 | Android |
    | 9 | Kernel analysis |
    | 10 | Vulnerability research |
    | 11 | Electron & JavaScript |
    | 12 | Anti-cheat & protection research |
    | 13 | DMA & hardware-assisted cheat research (defensive) |
    | 14 | Software cracking research |
    | 15 | Version comparison & crash work |
    | 16 | Long-running investigations |
    | — | Wildcard prompt · Prompt-writing tips · Next steps |
    
    > ⚠️ **Use responsibly.** Only analyze software you own or are explicitly authorized to test. Anti-cheat, DMA, DRM, kernel and vulnerability prompts below are for **security research, interoperability, CTFs, bug bounties and testing the protection of your own software**. Bypassing protection of software you don't own, cheating in online games, or weaponizing a found vulnerability may violate law and terms of service. Every prompt asks the agent to separate *confirmed facts* from *hypotheses* and to cite evidence — treat that as non-negotiable.
    
    ---
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  pengchujin/aerial-tv
    ⭐ 1069 stars  |  🍴 75 forks  |  💻 Kotlin  |  📅 2026-10-20
    🔗 https://github.com/pengchujin/aerial-tv
    📡 来源: 🚀 5天300+星
    📝 给国产电视的一块干净桌面：参照 tvOS 设计的开源 Android TV 桌面，没有广告，开机自动接管。A tvOS-style launcher for Xiaomi, TCL and other China-market TVs.

    README 摘要:
    # Aerial
    
    **给国产电视的一块干净桌面。**
    
    参照 tvOS 设计的 Android TV 桌面：没有广告，没有推荐流，只有你的 App、你的壁纸和 Apple TV 航拍屏保。
    为小米、TCL 等国产电视而做，开机自动接管，待机也不会被清理。
    
    **中文** · English
    
    | 电视自带的桌面 | 换上 Aerial 之后 |
    |:---:|:---:|
    |  |  |
    
    ## 功能
    
    ### 首页
    
      
      
    
    - **时钟**：大号细体时钟压在壁纸上，壁纸底部和左侧自动压暗。往下滚动时，时钟收进状态栏。
    - **应用网格**：每行 5 个，聚焦时浮起并显示名字。默认加一圈白色描边，离得远也看得清；在「控制中心 → 个性化 → 焦点样式」可以改回 tvOS 的原样。
    - **图标**：有电视横幅就用横幅；方形图标用自己的底色铺满磁贴；自适应图标拆成两层做视差。
    - **全部 App**：小米「应用中心」「高清播放器」「米家」这类没有标准入口的系统 App 也会显示。
    - **信号源磁贴**：把 HDMI、AV、电视天线固定到首页，按一下直接切换（控制中心 → 信号源 → 显示在主屏幕）。
    - **返回键**：和 tvOS 一样，在网格里按返回回到第一行，在第一行按返回开始屏保。
    
    ### 长按菜单
    
    长按 OK 键：**移动**（其他磁贴自动让位）、**从主屏幕隐藏**、**应用信息**、**卸载**。
    
    ### 控制中心
    
    在第一行按上键到右上角，再按确定打开（焦点在右上角时，也可以按菜单键 ≡）。包括信号源（显示 CEC 设备）、网络、设置，音量和亮度滑块，以及个性化（壁纸、屏保、焦点样式、天气）和隐藏的 App。网络和设置会打开电视自己的面板。在某个 App 上按菜单键，会打开这个 App 的菜单（移动、隐藏等），和长按确定键一样。
    
    ### 屏保
    
      
      
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  Ansub/tv-detox
    ⭐ 995 stars  |  🍴 102 forks  |  💻 Java  |  📅 2026-10-18
    🔗 https://github.com/Ansub/tv-detox
    📡 来源: 🚀 5天300+星
    📝 Make an old Android TV fast again with Claude Code or Codex: a tiny ad-free home screen plus the prompt to clean it up

    README 摘要:
    # TV Detox
    
    ### Make an old, slow Android TV fast again.
    
    Claude Code or Codex does the work. You just press OK on the remote.
    
    **As seen on**
    
    🧹 Removes the junkBloatware, ads and sponsored rows, gone.
    📺 A calm home screenYour apps, your HDMI inputs and a clock. Nothing else.
    ↩️ Undo anytimeApps are turned off, never deleted.
    
    ## Watch it work
    
    **▶ Claude Made My Old Android TV Feel Brand New** · the full setup on a real TV, in 4 minutes.
    
    ## Get started
    
    > [!WARNING]
    > **Google TV and Chromecast with Google TV:** don't turn off the TV's own home screen. On some of these devices that left them stuck restarting, and the only fix was a factory reset. Since v1.4.1, `install.sh` leaves it on for Google TV unless you opt in with `GOOGLE_TV=1`. The cleanup still works and makes the TV faster. You just keep Google TV's own home screen.
    
    > [!WARNING]
    > **OLED TVs:** keep the screensaver on. It stops a still picture from burning into the screen. Don't leave any home screen, this one included, on for hours.
    
    **1. Turn on developer mode on the TV.**
    Settings → Device Preferences → About → press **Build** 7 times. Then turn on **USB debugging** in **Developer options**. Stuck?
    
    **2. Open Claude Code or Codex on your laptop.**
    The laptop and TV must be on the same Wi-Fi.
    
    **3. Paste this in.**
    
    ```text
    Help me clean up my Android TV and make it faster.
    My TV is a .
    
    1. Connect to my TV over Wi-Fi. Walk me through anything
       I need to tap on the TV.
    2. Before changing anything, list every app in plain English:
       safe to turn off, needed by the TV, and apps I use.
