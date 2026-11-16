📊 开源日报 — 2026-11-16
共发现 8 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  ggml-org/ggml
    ⭐ 16009 stars  |  🍴 2057 forks  |  💻 C++  |  📅 2022-09-18
    🔗 https://github.com/ggml-org/ggml
    📡 来源: trending-daily
    🏷️ machine-learning
    📝 Tensor library for machine learning

    README 摘要:
    # ggml
    
    Tensor library for machine learning
    
    ## Quick start
    
    Build from source:
    
    ```bash
    git clone https://github.com/ggml-org/ggml
    cd ggml
    
    mkdir build && cd build
    cmake ..
    cmake --build . --config Release -j 8
    ```
    
    For a minimal, fully commented example (matrix multiplication), see examples/simple.
    
    ## Description
    
    The main goal of `ggml` is to be a simple, portable, and efficient tensor library for machine learning with minimal setup.
    
    - Plain C/C++ implementation without any dependencies
    - Cross-platform - x86, ARM, RISC-V, LoongArch, PowerPC, s390x, and WebAssembly
    - SIMD-optimized kernels for x86, ARM, and RISC-V
    - Broad backend support - CPU, GPU, NPU, and browser
    - 2- to 8-bit integer quantization, plus MXFP4 and NVFP4 microscaling formats
    - Zero memory allocations during runtime
    
    ## Documentation
    
    - The GGUF file format
    - Introduction to ggml
    - GGML tips & tricks
    
    ## Contributing
    
    - For changes to the core `ggml` library (including to the CMake build system), please open a PR in llama.cpp - doing so will make your PR more visible, better tested, and more likely to be reviewed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  ⚠️风险  elementalsouls/Claude-BugHunter
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 6786 stars  |  🍴 1046 forks  |  💻 Python  |  📅 2026-05-05
    🔗 https://github.com/elementalsouls/Claude-BugHunter
    📡 来源: trending-daily
    🏷️ ai-security, anthropic, application-security, bug-bounty, bugbounty, bugcrowd, claude, claude-code, claude-skills, ethical-hacking
    📝 A Claude Code skill bundle for bug hunting and external red-team work - 82 skills, 15 slash commands, 681 disclosed-report patterns curated across 24 core vulnerability classes, plus enterprise identity + infrastructure attack matrices.

    README 摘要:
    # claude-bughunter
    
    > A self-contained Claude skill bundle for bug hunting and external red-team work · **83 skills** · 15 slash commands · **681 disclosed-report patterns** (433 now individually cited & auditable) across 24 core vulnerability classes · enterprise identity + infrastructure attack matrices · engagement-folder scaffolding · Burp MCP integration · battle-tested across authorized red-team and bug-hunting engagements, plus public training platforms (DVWA, OWASP Juice Shop, Hacker101, testphp.vulnweb.com).
    
    Built by **Sachin Sharma** — Bug Hunting & GenAI Security Research.
    
      SPONSORED BY
      
      
        
          
          
        
      
      &nbsp;&nbsp;&nbsp;&nbsp;
      
        
          
          
        
      
    
    ---
    
    ## What is this?
    
    `claude-bughunter` is a drop-in skill bundle for the Claude Code skills system. Install once and Claude Code stops being a chatbot and starts behaving like a senior bug-hunting researcher or red-team operator: it knows the techniques, the chain templates, the VRT mappings, the platform CVE chains, and the hygiene — and it stays in scope.
    
    Four layers stack:
    
    - **Think** — `bb-methodology` + `redteam-mindset`: the 5-phase non-linear workflow, critical-thinking framework, and red-team operator discipline.
    - **Hunt webapps** — 58 `hunt-*` skills curated from 681 disclosed HackerOne reports: per-class detection patterns, payloads, bypass tables, and chain templates.
    - **Hit the perimeter** — enterprise platform chains (M365/Entra, Okta, vCenter, SSL-VPN appliances, SharePoint, cloud IAM): current 2024–2026 CVE chains + post-credential escalation.
    - **Ship it** — `triage-validation` + reporting + `evidence-hygiene`: the 7-Question Gate, VRT-aware severity, OOS rebuttals, PII redaction, and red-team deliverables.
    
    All triggered automatically by topic — describe what you're testing in plain English and the relevant skill loads. No invocation by name.
    
    ---
    
    ## Quickstart

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  NVIDIA/SkillEvaluator
    ⭐ 2002 stars  |  🍴 278 forks  |  💻 Python  |  📅 2026-06-24
    🔗 https://github.com/NVIDIA/SkillEvaluator
    📡 来源: trending-daily
    🏷️ agent-evaluation, agent-plugins, agent-security, agent-skills, agentic-ai, benchmark, claude-code, codex, evaluate, evaluation
    📝 Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.

    README 摘要:
    # SkillEvaluator
    
    > 📺 **Livestream:** Ask the Experts: Evaluating Agent Skills
    
    SkillEvaluator checks AI agent skills and measures their effect on task results:
    start with quality checks, then compare runs with and without a skill.
    
    Agent skills are folders of instructions and supporting files defined by the
    Agent Skills specification. SkillEvaluator is part of
    the NVIDIA Verified Skills pipeline.
    
    ## Get started
    
    Three ways in, one CLI, same results.
    
    1. Run the CLI directly
    2. Add it to your repo via CI
    3. Wire it to your agent
    
    Install (or `uv tool install`):
    
    ```bash
    pip install skillevaluator
    ```
    
    Run all Tier 1 checks, no API key:
    
    ```bash
    skillevaluator validate \
      ./my-skill --tiers 1
    ```
    
    Or run from a clone: Quickstart.
    
    Check changed skills on every pull request. On GitHub, run:
    
    ```bash
    skillevaluator ci init
    ```
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  hitkeeen/blender-ai-mcp-addon
    ⭐ 1854 stars  |  🍴 49 forks  |  💻 None  |  📅 2026-11-12
    🔗 https://github.com/hitkeeen/blender-ai-mcp-addon
    📡 来源: 🚀 5天300+星
    🏷️ ai-agents, ai-assistant, blender, blender-addon, blender-ai, blender-automation, blender-mcp, blender-plugin, blender-scripting, bpy
    📝 AI assistant and MCP server for Blender: visual chat, scene tools, multi-agent workflows. Works with ChatGPT/GPT, Claude, Gemini, Ollama, OpenCode. Blender AI addon, copilot for 3D, bpy Python scripting, MCP integration.

    README 摘要:
    # mcp-for-blender-pro
    
    ### Your Blender scene. Your AI models. One creative workspace.
    
    **An AI assistant for Blender that can inspect your scene, build objects, edit materials, find assets and carry out multi-step workflows—with a visual chat workspace and a built-in Model Context Protocol (MCP) server.**
    
    Download · Getting started · Connections and agents
    
    ## Turn a creative brief into scene operations
    
    Start with an idea. Ask the assistant to inspect your scene, create a product-display layout, arrange objects, assign materials or prepare an export. Follow its actions in the conversation and inspect the result in the viewport preview. Keep working in Blender throughout the process.
    
    **mcp-for-blender-pro brings conversation, scene tools, model choice and agent workflows together.** It is designed for artists who want faster iteration, technical artists who automate repetitive work, and developers connecting AI tools to Blender.
    
    ## Why choose mcp-for-blender-pro?
    
    | Capability | What it gives you |
    |---|---|
    | **Blender-aware assistance** | Scene and object inspection gives the assistant context before it acts. |
    | **A visual Studio workspace** | Chat, scene objects, viewport snapshots, approvals and a task board in a companion window. |
    | **Your choice of AI** | Connect supported cloud providers, local Ollama models or compatible custom endpoints. |
    | **Saved connections** | Keep work and personal connections separate, including multiple keys for the same provider. |
    | **One assistant or a team** | Use a single model for quick changes, or managers, workers and reviewers for structured tasks. |
    | **Built-in MCP server** | Connect OpenCode and other clients supporting authenticated Streamable HTTP MCP. |
    | **21 scene tools** | Create, inspect, edit, capture, search assets, consult Blender APIs and export scenes. |
    | **Multilingual menus** | Choose English, German, French, Spanish or Chinese for the main interface. |
    
    ## From a quick edit to an agent team
    
    Use **Single assistant** for direct, conversational work. For larger tasks, configure a **Team chain** with individual responsibilities, instructions and models.
    
    - **Manager:** breaks the request into assignments and acceptance criteria.
    - **Workers:** perform the assigned scene operations.
    - **Reviewers:** inspect results and approve work or return specific findings.
    
    Tasks run sequentially so scene edits stay ordered. A blocked task gets one correction attempt; a second failed review stops the workf

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  Noniv/abyssal-garden
    ⭐ 1262 stars  |  🍴 196 forks  |  💻 JavaScript  |  📅 2026-11-12
    🔗 https://github.com/Noniv/abyssal-garden
    📡 来源: 🚀 5天300+星
    📝 A dreamy underwater world you can swim through in your browser: swaying kelp forests, sunbeams, a sunken ship and manta rays. Everything is generated by code with WebGPU (no images, models or sound files), all in a single 97 KB HTML file.

    README 摘要:
    # Abyssal Garden
    
    **A dreamy underwater world you can swim through, right in your browser.**
    
    Towering kelp forests, sunbeams pouring through a rippling surface, a sunken ship, manta rays gliding overhead.
    And all of it is made by code: no images, no 3D models, no sound files. The whole world fits in **one 96 KB HTML file**.
    
    ## Try it
    
    1. Download `index.html`.
    2. Open it in **Chrome** or **Edge** on a desktop computer.
    3. Wait a few seconds while the world is built, then press **Dive in** and start swimming.
    
    Nothing to install, and it works offline. It needs a browser with **WebGPU**. If you see *"This scene needs WebGPU"*, update your browser or switch to Chrome / Edge.
    
    ## What's down there
    
    - **Kelp forests** that sway in the current and sparkle with tiny gold and green specks
    - **Light rays** streaming down from a wavy surface, with shimmering caustics on the sea floor
    - **A sunken wooden ship**, a **giant stone whale tail**, rock arches, canyons and floating boulders
    - **Manta rays**, schools of fish, rising bubbles and drifting particles
    - **A purple grotto** with glowing magenta ground cover, coral and barrel sponges
    - **A soundscape** made up as you listen: a deep rumble, distant whale calls, soft chimes and bubbles
    
    | | |
    |---|---|
    |  |  |
    |  |  |
    
    ## Controls
    
    | | Keyboard & mouse |
    |---|---|
    | Look around | Move the mouse |
    | Swim | `W` `A` `S` `D` |
    | Up / down | `E` / `Q` |
    | Swim faster | Hold `Shift` |
    | Jump to a viewpoint | `1` to `6` (the spots in the screenshots) |
    | Menu | `Esc` releases the mouse and opens the menu with the list of controls; **Resume** takes you back |
    | Sound on / off | `M` (sound starts when you dive in) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  ⚠️风险  duwqijlk/muse-protocol
    ⚠️ 命中风险词: cookie —— 默认归排除区，需人工确认
    ⭐ 1208 stars  |  🍴 502 forks  |  💻 Python  |  📅 2026-11-14
    🔗 https://github.com/duwqijlk/muse-protocol
    📡 来源: 🚀 5天300+星
    📝 muse.ai 注册与邀请码兑换协议研究（纯 HTTP Python 实现）

    README 摘要:
    # muse.ai 注册 / 邀请码兑换 协议分析
    
    补充一下，记得用JP 节点， JP 不需要绑卡，直接过
    
    纯 HTTP 实现 muse.ai 的注册与邀请码兑换流程，不依赖浏览器。本文记录的是通过抓包逐字段比对得出的协议细节。
    
    ## 快速开始
    
    ```bash
    pip install -r requirements.txt
    cp config.example.json config.json   # 填入邮箱与可选代理
    python example_register.py
    ```
    
    ## 目录结构
    
    ```
    musepy/
      client.py    注册 + 兑换的完整协议客户端
      runner.py    多账号批量调度（sticky 代理 / 预算 / 停止语义）
      otp.py       验证码轮询（幂等：只取 send 之后的最新码）
      falco.py     行为埋点上报（可选）
      caa.py       注册漏斗事件上报（可选）
    example_register.py        单账号端到端示例
    example_batch.py           多账号批量示例
    config.example.json        配置模板
    test_onboarding_smoke.py   离线冒烟（披露解析纯函数）
    test_runner_smoke.py       离线冒烟（批量调度，mock 网络）
    ```
    
    ## 协议流程
    
    ```
    GET  /                                   拿初始 cookie
    POST /api/auth/native/restart            → 201 {csrf_token}
    POST /api/auth/native/send-otp           → 201
    POST /api/auth/native/confirm-otp        → 200 {registration_state:"completion_required",
                                                   tos:{content_version}}（动态 TOS 版本）
    POST /api/auth/native/register-completion→ 200 {auth_meta_session:{frl_access_token, frl_account_id}}
    POST auth.meta.com/hatch/session/bootstrap/ → 302…→ muse.ai 200 HTML（会话引导，必须）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  ⚠️风险  ZiChuanLan/freebie-radar
    ⚠️ 命中风险词: 白嫖 —— 默认归排除区，需人工确认
    ⭐ 931 stars  |  🍴 161 forks  |  💻 TypeScript  |  📅 2026-11-12
    🔗 https://github.com/ZiChuanLan/freebie-radar
    📡 来源: 🚀 5天300+星
    📝 白嫖资源聚合雷达：57 个源定时采集 + AI 二审过滤假福利 + 获取方式分级隔离抽奖/试用/推广 + Telegram 即时推送

    README 摘要:
    资源雷达 · Resource Radar
      全网福利、黑五好价、拼车交易、开源项目与新闻资讯的多兴趣自托管聚合雷达站
      五大内容形态分流 · 21 类分频道目录 · 统一屏蔽词省额度 · AI 语义定级 · 多路由精准推送
    
      
        简体中文 · English
      
    
      
        
        
        
        
        
      
    
    ---
    
    **资源雷达（Resource Radar / repo: `freebie-radar`）** 是一款轻量、开箱即用的多兴趣社区信息聚合与精准推送工作台。它从各大开发者社区、游戏平台、软件限免站、GitHub、Reddit、Bluesky、Telegram 频道及自定义 RSS 采集信息，并通过 **「规则初筛与统一屏蔽 → AI 语义定级与分流 → 分频道目录呈现 → 多路由精准推送」** 把每条内容送到它该去的位置：
    
    - 只想纯粹蹲羊毛？首页默认 **「真福利精选」** 严格锁定 AI 验真的 `freebie`（直接白嫖 + 实操可领的有条件福利），绝不被付费好价、拼车、二手或新闻污染。
    - 想看 **黑五 VPS 好价 / 合规拼车 / 开源项目 / 重大新闻与科技资讯**？一键切换顶部兴趣频道即可浏览各自专属的下级分类、真实有效计数与图文卡片，并可分别配置互不干扰的 Telegram 专题推送路由。
    
    ---
    
    > 在线演示：
    
    ---
    
    ## 界面预览
    
    | 工作台列表视图（多兴趣频道栏 + 跨源折叠 + 兑换码一键复制） | 三列图文卡片视图（零额外请求封面图提取 + 响应式 2列/3列网格） |
    | :---: | :---: |
    |  |  |
    
    | 多路由精准推送（分形态/分类/获取方式/关键词定制即时或攒批路由） | AI 语义引擎（21 类分流、自适应学习与零 Token 存量重整分类） |
    | :---: | :---: |
    |  |  |
    
    ---

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  faizfahmi77/ScanDot
    ⭐ 540 stars  |  🍴 5 forks  |  💻 Kotlin  |  📅 2026-11-13
    🔗 https://github.com/faizfahmi77/ScanDot
    📡 来源: 🚀 5天300+星
    🏷️ 3d-scanning, android, photogrammetry, point-cloud
    📝 Experimental Android 3D scanning and point-cloud viewer

    README 摘要:
    # ScanDot
    
    ScanDot is an experimental Android app for capturing and viewing 3D point clouds on a supported phone. It combines ARCore camera tracking and depth estimates, saves scans locally, and provides an interactive viewer.
    
    The repository also contains a separate video photogrammetry pipeline that runs on a workstation using FFmpeg and COLMAP. **The Android app does not reconstruct ordinary video with photogrammetry on the phone.**
    
    ## Current status
    
    - Capture, save and reopen point clouds on devices that support ARCore Depth.
    - Rotate, pan and zoom scans in the viewer. An optional full-depth mode interpolates missing depth and can distort surfaces.
    - Prepare video frames and run a sparse or dense COLMAP reconstruction on a workstation.
    
    This is an early prototype. Results can contain gaps, drift and noise; they are not textured meshes or validated measurements. Reflective, transparent and textureless subjects are difficult. Capture quality and device compatibility need further testing.
    
    ## Try the preview
    
    Download the preview APK. The release notes describe compatibility and signing limitations.
    
    ## Build the Android app
    
    You need JDK 17, Android SDK 36, and an Android device with ARCore Depth support. Camera permission is required; Google Play Services for AR may require installation or an update.
    
    ```sh
    cd android-app
    ./gradlew assembleDebug lintDebug testDebugUnitTest
    ```
    
    On Windows, use `gradlew.bat` in place of `./gradlew`. The debug APK is written to `android-app/app/build/outputs/apk/debug/app-debug.apk`. Install it as an update to preserve existing app data.
    
    In the app, name the scan, tap **Start scan**, and move slowly around the subject in good light. Save it, then open it from **Results**. Scans are stored in the app's private storage; uninstalling the app removes them.
    
    ## Workstation video pipeline
    
    The benchmark requires Python 3.12 or newer, FFmpeg, FFprobe and a compatible COLMAP installation. Dense reconstruction requires a compatible COLMAP configuration. From the repository root:
    
    ```sh
    python -m processing.benchmark prepare "path/to/input.mp4" --output "path/to/new-run" --fps 5
    python -m processing.benchmark reconstruct "path/to/new-run" --colmap "path/to/colmap" --dense
    ```
    
