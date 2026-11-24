📊 开源日报 — 2026-11-24
共发现 8 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  wanshuiyin/Auto-claude-code-research-in-sleep
    ⭐ 19691 stars  |  🍴 1578 forks  |  💻 Python  |  📅 2026-03-10
    🔗 https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | LLM agent framework
    🏷️ ai-research, ai-tools, aris, autonomous-agent, claude, claude-code, claude-code-skills, codex, deep-learning, gpt
    📝 ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent.

    README 摘要:
    # Auto-claude-code-research-in-sleep (ARIS ⚔️🌙)
    
      
        
      
    
     ·  ·  ·  ·  ·  ·  ·  · 💬 Join Community · 
    
    🌱 *ARIS is a methodology, not a platform. What matters is the research workflow — take it wherever you go.*
    
    💡 *Use ARIS as a skill-based workflow in Claude Code / Codex CLI / Cursor / Trae / Antigravity / GitHub Copilot CLI / OpenClaw / DeepSeek Harness — enjoy any way you like!**The executor drives, an independent model (Codex MCP by default) reviews. Alternative model combinations, including ModelScope-hosted models, need no Claude or OpenAI API.*
    
    📦 *Those are the skills installed directly. Want it in one command? ARIS also ships as a standalone CLI and as plugins:*  ·  ·  · 
    
    **🤝 SuperARIS — Your personal research agent with ARIS, powered by a team of agents.**
    
    Put ARIS workflows in the hands of a persistent team: your main agent coordinates, while engineering and writing run in parallel. Every member can read ARIS skills and project context on demand. Work directly with Codex on experiments and Gemini on ideas and writing, or choose an all-Codex team. The main agent follows up on deliverables; project files carry memory across sessions. Your existing MCP workers and independent reviewers stay in the loop.
    
    **Homepage · GitHub**
    
    *Demo preview · click to watch the full 1080p video (~21 seconds).*
    
    ❗  **codex-cli 0.154.0 removed `codex mcp-server` — the entry point every ARIS reviewer call used. No impact on ARIS:** the `codex` MCP server is now ARIS's own bridge over `codex exec` (`mcp-servers/codex-exec/`), same tools, same results, all 82 skills unchanged, `ultra` and per-thread resume intact. One re-registration is all it takes — **already installed? → Quick Start step 2b** · **new install → step 2** · what changed.
    
    **🧩 The ARIS family** — same method, other jobs. One line each; the details live in their own repos.
    
     — **EasyAIOffer**: 34 bilingual ML / LLM interview cheat sheets on one page — derivations, from-scratch PyTorch, 25 questions each. 希望大家秋招轻松一点 🌱
    
     ·  — two sides of one disease. HERO: a ~550-token block for `CLAUDE.md` / `AGENTS.md` against the four shapes agents over-defend in (Hashing, Edge cases, Rubrics, Overbuild), bounding what the agent *proposes*, never what it *looks for*. Anti-Autoresearch: 61 integrity signals into a deterministic, reviewer-ready report — fabrication forensics, not an AI-text detector.
    
     — **ARIS goes multimodal**: a rough story in, a movie told in still frames out, every scene checked by another model

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  Marvisak/VIctory
    ⭐ 7520 stars  |  🍴 980 forks  |  💻 Rust  |  📅 2026-11-23
    🔗 https://github.com/Marvisak/VIctory
    📡 来源: 🚀 5天300+星
    📝 An attempt at running GTA VI on PC

    README 摘要:
    # VIctory
    
    Runs Grand Theft Auto VI (Xbox Series X|S) natively on Windows, from files
    the user supplies.
    
    The title's x86-64 code runs unchanged inside our process; VIctory supplies
    the platform underneath it and converts the title's data, ahead of time where
    it can and on first use where it must (shaders). See
    docs/architecture.md.
    
    ## Status (2026-11-23)
    
    **Not playable yet.** The title boots, runs its menus at its own 30 fps and
    loads the world, where rendering fails.
    
    | Stage | State |
    |-------|-------|
    | Boot, first-boot screens (accessibility, language, settings, legal) | works, 30 fps |
    | Intro video with sound | works |
    | Start screen, profile and saves | works |
    | Loading into the world (about 50 s) | works |
    | The world (first mission's intro) | reached and runs with indirect draws; its title card renders, the scene after it is still dark; 0.5-1.8 s per frame |
    
    Tested on one machine: Windows 11, AMD RX 6700 XT.
    
    > **Warning.** Entering the world on a real GPU can currently hang it, and
    > Windows then resets the display driver (every monitor goes black for a
    > moment). To look further, use a diagnostics build with
    > `VICTORY_D3D12_WARP=1`, which renders on the software adapter.
    
    What each part does today and what it still needs:
    
    | Subsystem | Today | Needs |
    |-----------|-------|-------|
    | Loader | Runs the title's executable and its DLLs in our process; crash reports name the faulting code and are kept in `crashes.log` | – |
    | Runtime services | One signed-in offline user, licences, packages, saves that survive a kill at any step, text entry dialog | Speech is silent; the dialog and relaunch are untested live |
    | Network | Offline by design: the title cannot reach the network | – |
    | Files and streaming | Archives and streamed data read, zlib and BCPack decoded in parallel | Loading is limited by writes into title memory |
    | Input | XInput pads, keyboard, keyboard stand-in pad | Trigger rumble |
    | Audio | Menu, video and loading sound; XMA voices and Opus streams decode | Reverb is silent; Opus results unverified against the title |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  ivall/xcl
    ⭐ 5989 stars  |  🍴 731 forks  |  💻 Rust  |  📅 2026-11-20
    🔗 https://github.com/ivall/xcl
    📡 来源: 🚀 5天300+星
    🏷️ d3d12, gdk, rdna2, xbox
    📝 Xbox Series compatibility layer for Windows - runs console game code natively, reimplements the console system libraries and recompiles RDNA2 shaders to DXIL

    README 摘要:
    # XCL – Xbox Series X|S → Windows compatibility layer
    
    **Discord: **
    
    XCL is a compatibility layer that runs Xbox Series X|S (GDK) games you own on a Windows PC - in the spirit of Wine/Proton. There is no CPU emulation: the game's x64 code runs natively, and XCL provides its own, independently written implementations of the console system libraries the PC does not have (`kernelx.dll`, XGameRuntime, `d3d12_xs.dll`, …). The console's GPU code (RDNA2 machine code) is recompiled into PC shaders (HLSL → DXIL).
    
    XCL works only on unpacked game files you already own. It does not download, decrypt or unpack game packages (XVC / MSIXVC) and contains nothing for circumventing DRM. The repository holds no code, headers or binaries from the console SDK, no keys and no game data; the Windows components XCL relies on (XGameRuntime, XAudio2, D3D12, DXC) come from your own system or the public Windows SDK and are not distributed with XCL.
    
    ## Games
    
    | Game | Package (version) | State | What works | Limits |
    |---|---|---|---|---|
    | **Minecraft Preview** | `Microsoft.MinecraftBeta` 1.18.3064.0 | ✅ | fully playable | – |
    | **Unicorn Overlord** | `SEGAofAmericaInc.Pa253b0c1Y` 1.0.0.6 | ✅ | fully playable | – |
    | **Fortnite** | `436609B6.FortniteClient` 2.0.1461.7919 | ✅ | works fully, as far as the game allows without its online services | the game itself is online-only (multiplayer servers) |
    | **XDefiant** | `Ubisoft.XDefiant-Game` 1.0.0.186 | ✅ | works fully, as far as the game allows without its servers | the game's own servers have been shut down |
    | **A newer retail game** | – | 🚧 | starts in ~4 s, runs at a steady 30 fps without a crash, shows its menus and goes on past the first one to its settings; fits a 32 GB machine (~15 GB committed in the menus) | gameplay not reached yet; its minimap mesh pipelines are refused |
    
    ## Highlights
    
    - **100 % of a retail game's shaders translate** – all 26 698 RDNA2 programs (26 503 records) of its shader pack
      become HLSL; random samples compile to DXIL with 0 errors.
    - **The game's own console DLLs run on the PC** – its Bink 2 video codec decodes the game's
      movies, its ray-tracing BVH builder builds acceleration structures on a PC GPU, the AMD FSR 4
      console upscaler runs a whole frame on a PC GPU, the GDK HTTP library initialises.
    - **Console textures decode exactly** – the GFX10 tiling and mip layout reproduce 909 of 912
      textures of the game's texture archive byte for byte, its volume textures included.
    - **370+ automated

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  AFK-surf/xnulinux
    ⭐ 2760 stars  |  🍴 111 forks  |  💻 Objective-C++  |  📅 2026-11-20
    🔗 https://github.com/AFK-surf/xnulinux
    📡 来源: 🚀 5天300+星
    📝 XNU as a loadable kernel module inside Linux (macOS personality for arm64 Linux)

    README 摘要:
    # xnulinux
    
    Run macOS userspace on Linux by loading the macOS kernel into it.
    
    xnulinux builds XNU, the open-source kernel of macOS, from Apple's published sources and runs it as a loadable kernel
    module (`xnu.ko`) inside an unmodified arm64 Linux kernel. The hosted XNU drives the CPU and MMU directly, so macOS
    processes run natively next to Linux processes on the same CPUs, with no hypervisor between them. Linux lends XNU its
    memory, timers, files, network and GPU through a small interface module (`fki.ko`).
    
    With a stock Ubuntu kernel, `insmod xnu.ko` boots a macOS 27 system disk made by Apple's own installer to the
    desktop: loginwindow, WindowServer, Dock, Finder, Safari and Chrome.
    
    *One system, two userspaces. Left: a Terminal in the hosted macOS 27.2.1 (`sw_vers`, the Darwin kernel, launchd,
    WindowServer, Dock and Finder running). Right: from that macOS, an SSH session into the Linux it runs inside (Ubuntu,
    Linux 7.0, the `xnu` and `fki` modules loaded, and the `insmod xnu.ko` process the macOS kernel runs in).
    Straight from the hosted framebuffer, 1280×800.*
    
    *The hosted desktop at the end of a 30-minute stress run, rendered on the CPU (no GPU bridge).*
    
    | | |
    |---|---|
    |  |  |
    |  | |
    
    *Safari in the hosted macOS: Wikipedia's article on XNU, kernel.org and the Linux repository on GitHub, over the
    hosted system's network link through Linux, with the GPU bridge on (`GPU=auto`).*
    
    *Bare-metal NVIDIA DGX Spark (Ubuntu 24.04.5 LTS aarch64, Linux `7.0.0-1025-nvidia`): hosted macOS 27 running with
    4 CPUs and 8 GiB of RAM (CPU rendering), shown over macOS Screen Sharing alongside an SSH session from the DGX Spark
    host into the hosted Darwin userspace.*
    
    *Inside the hosted macOS on DGX Spark: About This Mac (`Chip: Unknown`, `7.80 GB` memory, `macOS Golden Gate 27.2`)
    alongside `sysctl machdep.cpu` (`ARM processor`, `hw.cpufamily: 0`, `hw.ncpu: 4`) and `hw.optional.arm`.*
    
    ## How it works
    
    ```
     macOS processes (launchd, WindowServer, Safari...)    Linux processes (systemd, sshd, xnudrmd...)
     ──────────────────────────────────────────────────    ────────────────────────────────────────────
     XNU (source-built, LINUX64 machine layer, kexts)  │

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  4lwayz/portwatch-vi
    ⭐ 1489 stars  |  🍴 34 forks  |  💻 JavaScript  |  📅 2026-11-21
    🔗 https://github.com/4lwayz/portwatch-vi
    📡 来源: 🚀 5天300+星
    📝 Does GTA VI run on PC yet? A live tracker of community recompilation and emulation efforts, updated daily.

    README 摘要:
    # PortWatch VI
    
    **Does GTA VI run on PC yet?** A static GitHub Pages site that tracks every serious community effort to recompile, emulate or port the leaked Xbox Series build of GTA VI to PC. All efforts are scored on one ladder, and a scout refreshes the data every 3 hours.
    
    - One headline progress bar shows the closest effort, with the top projects pinned to it.
    - A live countdown runs to the missing executable's expected drop.
    - A leaderboard card per effort shows its own bar, milestone ladder, groundwork breakdown, what works and what's blocking.
    - Further sections cover the watchlist of early projects, a toolkit of asset tools, the scout's inbox of new candidates, and fake-download warnings.
    
    No game files, keys or executables are hosted or linked, ever.
    
    ## Deploy on GitHub Pages
    
    1. Create a new GitHub repository and push this folder to its `main` branch.
    2. In the repo, open **Settings → Pages** and set **Source** to **GitHub Actions**.
    3. Open **Settings → Actions → General** and make sure workflows are allowed.
    4. Open **Actions → Scout → Run workflow** to run the first scout. It commits fresh data and deploys the site.
    
    Each deploy also runs `scripts/build-site.mjs`, which turns `data/tracker.json` into pages search engines can read: one page per news story (`news/.html`), a news archive, an RSS feed (`news/feed.xml`) and `sitemap.xml`. It then pings IndexNow (Bing, Yandex and others; no account needed) with the URLs that changed since the last deploy. For Google, add the site in Search Console and submit `sitemap.xml`.
    
    From then on, `Scout` runs every 3 hours (00:17, 03:17, 06:17 … UTC) on GitHub's servers, so no computer of yours needs to be on. Any push to `main` redeploys the site through `Deploy site`. To change the frequency, edit the `cron` line in `.github/workflows/scout.yml`. For example, `17 6 * * *` runs it once a day. GitHub can delay scheduled runs by a few minutes when it's busy.
    
    ## What the scout does (`scripts/scout.mjs`)
    
    1. **Refreshes** every tracked repo: stars, forks, issues, last push, commits in the last 7 days, and whether it's gone (404, or 451 for a DMCA block). It also hashes each README to notice changes.
    2. **Spots claims.** If a README newly says GTA VI boots, reaches the menu or runs at some FPS, the card shows an "unverified claim" banner and the change feed records it.
    3. **Discovers** new repos from GitHub and GitLab searches (`scout.queries` in `data/tracker.json`), Hacker News, Bluesky, Mastodon, Lemmy and

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  zed-industries/gpui
    ⭐ 1076 stars  |  🍴 11 forks  |  💻 None  |  📅 2022-06-20
    🔗 https://github.com/zed-industries/gpui
    📡 来源: 🔧 开发/工具链 | 活跃 | cross-platform mobile fr
    🏷️ cross-platform, desktop, frameowrk, gpu, gpu-acceleration, gpui, gui, mobile, rust, web
    📝 A GPU-accelerated, open-source UI framework for Rust that combines immediate and retained modes.

    README 摘要:
    # gpui
    
    See you in a few weeks.
    
    - Website
    - crates.io

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  ubiquitarianism/leonida
    ⭐ 950 stars  |  🍴 212 forks  |  💻 Python  |  📅 2026-11-23
    🔗 https://github.com/ubiquitarianism/leonida
    📡 来源: 🚀 5天300+星
    📝 A continuation of Leonida, the Xbox > PC port of GTA VI

    README 摘要:
    Leonida Continued
      
    
    Grand Theft Auto VI (Xbox Series) running natively on Windows, built on your PC from your own copy.
    
      Other languages |
      Status |
      How to build |
      How it works |
      Want to help? |
      Credits |
      License |
      Discord
    
    Leonida is a static recompilation project. The Xbox Series CPU is x86-64 like a PC, so the game's code is loaded
    and run natively, and the console's system software is reimplemented. The console's precompiled RDNA2 GPU programs
    are translated to SPIR-V for Vulkan. The game's models, textures and audio are read from your package. All of this
    happens **on your PC, from your own copy of the game**.
    
    > [!IMPORTANT]
    > This repository **does not contain the game, keys or an executable**, and it does not explain how to get them. You
    > need your own copy, with its files already readable on disk. Nothing here decrypts or works around any protection.
    > Everything the build creates (the generated shaders, extracted assets, the runtime folder and your saves) comes
    > from your game and stays on your PC. Never share those files.
    
    > [!NOTE]
    > **This is a continuation of NotRexed's Leonida project.** The original
    > author has left the project, and development continues here with its full commit history. Credit for the work up to
    > that point belongs to NotRexed and the contributors listed in the history.
    
    Discord: https://discord.gg/ETf4qj5acN
    
    Original author's Git Mirror: https://git.notrexed.dev/notrexed/Leonida
    
    ## Project status
    
    **Early. The game does not boot yet.** Everything that can be done without the game's executable is in place, so
    work on booting can start as soon as one is available to a developer.
    
    | What | Status |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  cropflre/nowen-reader
    ⭐ 211 stars  |  🍴 22 forks  |  💻 TypeScript  |  📅 2026-03-04
    🔗 https://github.com/cropflre/nowen-reader
    📡 来源: 📖 阅读/内容平台 | 活跃 | epub reader open source
    🏷️ comic-reader, comics, docker, doujinshi, ebook-reader, epub, golang, manga, manga-reader, nas
    📝 NowenReader（弄文阅读）是开源自托管的漫画与小说书库。支持飞牛 fnOS 和 Docker 部署，自动扫描入库，按目录和标签找书。电脑上读到哪，手机上接着读。 | An open-source, self-hosted library for comics and novels. Deploy on fnOS or with Docker, scan your collection automatically, browse by folder or tag, and pick up where you left off on your phone.

    README 摘要:
    Nowen Reader（弄文阅读）
    
      
      
      
      
      
      
    
      高性能自托管漫画 & 小说管理阅读平台
      Go 单二进制构建 · 轻量极速 · AI 智能辅助 · NAS 友好
    
      简体中文 ·
      English
    
      快速开始 •
      安装指南 •
      配置说明 •
      API •
      开发 •
      FAQ
    
    ---
    
    > **问题反馈 QQ 群：`1093473044`**
    
    ## 💡 项目简介
    
    Nowen Reader（弄文阅读）是一个专为 NAS 与个人服务器场景优化的自托管漫画 / 小说管理阅读平台。
    
    | 🏆 核心优势 | 说明 |
    |:---|:---|
    | 💾 **极致轻量** | 内存限制 512 MB 即可流畅运行，Docker 镜像仅约 30 MB |
    | 📦 **零依赖部署** | Go 编译为单个静态二进制，前端通过 `go:embed` 嵌入其中 |
    | 🐳 **Docker 一键启动** | 提供通用、生产、NAS 三种 Compose 配置 |
    | 🤖 **AI 智能辅助** | 可选接入 17+ LLM 供应商（含主流国内大模型） |
    | 📚 **全格式覆盖** | 漫画 ZIP / CBZ / CBR / RAR / 7Z / CB7 / PDF；小说 TXT / EPUB / MOBI / AZW3 / HTML |
    | 🌐 **中文原生支持** | 中英双语界面、元数据中英翻译 |
    | 📱 **多端访问** | Web PWA + Flutter 原生客户端（Android / iOS / 桌面） |
    | 🏗️ **多平台架构** | amd64 / arm64，覆盖主流 NAS（群晖、威联通、绿联、铁威马等） |
