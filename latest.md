📊 开源日报 — 2026-10-17
共发现 5 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  ⚠️风险  hmjz100/LinkSwift
    ⚠️ 命中风险词: 破解, cookie —— 默认归排除区，需人工确认
    ⭐ 23919 stars  |  🍴 1457 forks  |  💻 JavaScript  |  📅 2022-08-10
    🔗 https://github.com/hmjz100/LinkSwift
    📡 来源: trending-daily
    🏷️ 123pan, aliyun-drive, aliyunpan, aria2, baidu, baidu-netdisk, baidunetdisk, baidupan, baiduyun, guangya-netdisk
    📝 一个基于 JavaScript 的网盘文件下载地址获取工具。基于【网盘直链下载助手】修改 ，支持 百度网盘 / 阿里云盘 / 中国移动云盘 / 天翼云盘 / 迅雷云盘 / 夸克网盘 / UC网盘 / 123云盘 八大网盘

    README 摘要:
    > [!IMPORTANT]
    > 如果您是从 GreasyFork 找到这的，建议前往下方的 安装 选择一个合适的源覆盖安装，避免因脚本失效或 GF 黑产刷子导致无法及时更新。
    
    “出淤泥而不染，濯清涟而不妖”
    
       搭配使用，效果更佳！👋扩展脚本
       
       123 云盘会员青春版 | 百度网盘会员青春版 | 阿里云盘会员青春版
       
       ↓&nbsp;&nbsp;↓&nbsp;&nbsp;↓&nbsp;&nbsp;↓&nbsp;&nbsp;↓
    
       
       
       
       
       
       
       
       
       
       
       
       
    
    ## 介绍
    
    支持 百度网盘 / 阿里云盘 / 中国移动云盘 / 天翼云盘 / 迅雷云盘 / 光鸭云盘 / 夸克网盘 / UC网盘 / 123云盘 九大网盘  
    相比较原脚本，增加了更多功能~
    
    ## 安装
    
    根据需要选择合适的源，点击链接即可安装
    
    ### LinkSwift
    直链获取、UI 美化、支持多种下载器
    
    #### 正式版
    - Github 国际: hmjz100/LinkSwift/（改）网盘直链下载助手.user.js
    - OpenUserJS 国际（更新不及时）: hmjz100/LinkSwift.user.js
    - 脚本猫 国内: hmjz100/1604/LinkSwift.user.js

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  android/skills
    ⭐ 8143 stars  |  🍴 539 forks  |  💻 Kotlin  |  📅 2026-03-16
    🔗 https://github.com/android/skills
    📡 来源: trending-daily
    🏷️ skills
    📝 无描述

    README 摘要:
    ## Android skills
    
    **Android skills** are a dedicated repository of **AI-optimized, modular instructions** and
    resources, to help agents better understand and execute specific patterns that follow the best
    practices and guidance on Android development
    from developer.android.com.
    
    Android skills follow the open-standard agent skills - markdown
    files (SKILL.md) that provide a technical specification of a task, and **ground LLMs** with
    information on specialized domains and workflows.
    
    Our Android skill development focuses on **use cases and workflows where evaluations show LLMs
    underperform**.
    We aren't prioritizing well-established areas where LLMs are already proficient, such
    as basic Jetpack Compose best practices.
    
    To learn more, read the official documentation:
    
    - Android skills
    - Android CLI
    - Android Studio
    
    ### Install Android skills
    
    Use Android CLI to install a specific skill into the current directory:
    
    ```
    android skills add r8-analyzer --project=.
    ```
    
    Use Android CLI to install all Android skills to directories for all detected agents:
    
    ```
    android skills add --all
    ```
    
    If you don't have any existing agent directories and don't specify particular agents, the skills
    will be installed for Gemini and Antigravity at `~/.gemini/antigravity/skills`.
    
    **Options:**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  feder-cr/git-ai
    ⭐ 1071 stars  |  🍴 115 forks  |  💻 Go  |  📅 2026-10-15
    🔗 https://github.com/feder-cr/git-ai
    📡 来源: 🚀 5天300+星
    🏷️ ai-agents, coding-agents, git, golang, scion, version-control
    📝 Git designed for AI agents.

    README 摘要:
    Git designed for AI agents.
    
    Anthropic built **Scion**, a faster version control system for coding agents,
    and described it in
    Redesigning source control:
    a server-centric system built for hundreds of agents that read, write and land
    code at the same time. Scion is internal to Anthropic and is not available to
    the public.
    
    So I built **gitai**: an open-source version of that design that anyone can
    run, and that the community can improve and maintain together.
    
    MIT licensed. Vendor neutral: the server never calls a language model, and every
    AI feature works with any provider, or none.
    
    gitai is an independent implementation of the publicly described design. It is not affiliated with or endorsed by Anthropic.
    
    ---
    
    ## Why
    
    Classic Git hosting was built for humans who clone a repository, work for hours
    and push once. Coding agents work differently: thousands of short-lived tasks,
    each touching a few files, each wanting to land in seconds, all on the same
    branches. Full clones, merge queues and client-side history walks become the
    bottleneck.
    
    Scion's answer is to move the work to the server: clients stay online and fetch
    only what they need, history questions are answered (and cached) by the server,
    changes land through a compare-and-swap instead of a queue, every update is an
    entry in a changeset log, and the repository state lives in a consistent
    database plus object storage so servers scale out. gitai implements these
    ideas, with normal Git repositories underneath.
    
    ## The Scion ideas, implemented
    
    | Scion idea | In gitai |
    |---|---|
    | **Always-online clients** that fetch exactly what they need | `ObjectService` serves single objects and sparse trees; `graft clone` and `graft sparse` materialize only the paths you ask for. |
    | **Source control as an API**: history runs on the server | Blame, path history, ancestry and code search run server-side and are memoized as derived data, computed once per commit. |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  Supermedo/uncharted_pc
    ⭐ 1056 stars  |  🍴 52 forks  |  💻 C++  |  📅 2026-10-15
    🔗 https://github.com/Supermedo/uncharted_pc
    📡 来源: 🚀 5天300+星
    📝 Uncharted: The Nathan Drake Collection running natively on Windows - by SuperMedo

    README 摘要:
    # Uncharted: The Nathan Drake Collection for Windows
    
    **Uncharted 1, 2 and 3 from the PS4 collection running natively on Windows 10 and 11, by SuperMedo.** Mohammed Albarghouthi
    
    Same idea as my Bloodborne port: the original PS4 game
    code runs directly on your PC and the graphics are translated to Vulkan. Unpack the zip, start
    `Uncharted.exe`, pick your game folder, choose a game and press **PLAY**.
    
    **Download the latest version** · **Join the Discord**
    
    > **No game files are included.** You need your own decrypted dump of the collection
    > (CUSA02343, CUSA02320, ...: the folder with eboot.bin, big2-ps4_Shipping.elf,
    > big3-ps4_Shipping.elf, sce_sys, u1data, u2data and u3data).
    > This project is not affiliated with Sony Interactive Entertainment or Naughty Dog.
    
    ## Features
    
    - All three games from one launcher: Drake's Fortune, Among Thieves and Drake's Deception.
    - 60 FPS like on PS4, or 120 FPS (higher rates are experimental).
    - Anti-aliasing with TAA, AMD FSR 3.1, AMD FSR 4 or NVIDIA DLSS (DLAA).
    - Frame generation: AMD FSR 3 (any GPU) or NVIDIA DLSS (RTX 40 2x, RTX 50 up to 4x).
    - Keyboard, mouse and controller together, all remappable. Mouse look in U3.
    - Add to Steam and desktop shortcuts from the launcher, automatic updates.
    
    ## Requirements
    
    - Windows 10 (1903 or later) or Windows 11, 64-bit.
    - A graphics card with Vulkan 1.3 and a current driver, with **6 GB of video memory or more**.
      4 GB cards (GTX 1650, RX 570) run out of video memory and crash after a while; on those, keep
      Anti-aliasing and Frame generation off.
    - About 8 GB of free memory (RAM + page file).
    
    ## Known problems
    
    - **Uncharted 3, Cartagena square (chapter 2):** at high frame rates (240 Hz setting, ~80 FPS)
      the game could freeze and close with "GPU crash: the graphics device was lost". It came from
      the speed fix for that area and is fixed in 0.3. If it still happens to you, set Frame rate to
      60 on the Display page and open an issue with your `user\last_run.log`.
    - **Uncharted 3:** green or black shapes flash for a single frame on some characters (Sully's
      shirt in Cartagena). It happens in shadPS4 too, so it's a shader translation problem. Not fixed yet.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  Zfinix/eleven
    ⭐ 633 stars  |  🍴 104 forks  |  💻 TypeScript  |  📅 2026-10-13
    🔗 https://github.com/Zfinix/eleven
    📡 来源: 🚀 5天300+星
    🏷️ acp, ai-agents, android, decompiler, disassembler, ghidra, hopper, macos, rea, reverse-engineering
    📝 Agent-first reverse engineering for macOS, Windows and Linux: any ACP agent reads, renames and patches binaries, Android apps and GPU kernels next to you.

    README 摘要:
    Eleven
    
    An agent-first reverse-engineering app for macOS, Windows and Linux.
    
    **English** · 简体中文 · 繁體中文 · 日本語 · 한국어 · Türkçe · Русский · Tiếng Việt · ไทย · Deutsch · Español · Français · Українська · Polski · Português (Brasil) · العربية · فارسی · Bahasa Indonesia · Italiano
    
      
    
    Eleven is a reverse-engineering app built around agents. Drop in an app, a binary, an Android APK, a GPU kernel, a shader or a model and ask what it does. Any agent that speaks the Agent Client Protocol can read the code, follow references, rename functions, leave notes and suggest patches, while you watch and approve in the same window.
    
    Native code is read by Ghidra through REA, or by Rizin when you want files to open in seconds. Android apps are read by jadx. The UI is React rendered natively on GPUI by GPUIX.
    
    ## Features
    
    - **Bring your own agent.** Aster, Claude, Codex, Gemini, Cursor, Copilot, OpenCode and any other ACP agent. Run several on the same project, each in its own chat.
    - **Agents drive the window.** Eleven serves its own MCP tools so an agent can open a function, switch views, rename, add notes, change types and propose patches.
    - **Ask about any code.** Select lines in pseudocode, assembly or a source file and ask, explain or copy them. The answer opens under the lines, and a suggested rename arrives as a card you accept or decline.
    - **You stay in control.** Every change by you or an agent is logged with its author and can be undone. Byte patches from agents arrive as suggestions you accept or decline.
    - **Mach-O, ELF and PE.** Functions, pseudocode, assembly, control-flow graph, cross-references, strings, segments and hex. Change a line's type (code, procedure, data, string) and number format with Hopper's keys.
    - **Android apps.** APKs open with Java from jadx, smali from apktool when it's installed, string resources, and the manifest, `res`, assets and native libraries in a Resources list. Split bundles (`.xapk`, `.apks`) open with every split in place.
    - **Source files.** Eleven finds the source files a binary was built from, reads Swift types straight from the binary, and has your agent recreate a whole file, with each function linked back to its address.
    - **Rewrite in any language.** Show a function's pseudocode rewritten by your agent in C, C++, Rust, Go, Swift, Python, TypeScript, Java, C# or Zig.
    - **GPU kernels.** CUDA and HIP fat binaries open as highlighted PTX, with notes beside each block and rewrites in CUDA C++, HIP C++ or Me
