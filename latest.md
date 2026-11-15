📊 开源日报 — 2026-11-15
共发现 13 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  ag-ui-protocol/ag-ui
    ⭐ 17471 stars  |  🍴 1724 forks  |  💻 TypeScript  |  📅 2025-05-07
    🔗 https://github.com/ag-ui-protocol/ag-ui
    📡 来源: trending-daily
    🏷️ ag-ui-protocol, agent-frontend, agent-ui, agentic-workflow, ai-agents
    📝 AG-UI: the Agent-User Interaction Protocol. Bring Agents into Frontend Applications.

    README 摘要:
    #  AG-UI: The Agent-User Interaction Protocol
    
    AG-UI is an open, lightweight, event-based protocol that standardizes how AI agents connect to user-facing applications.
    Built for simplicity and flexibility, it enables seamless integration between AI agents, real time user context, and user interfaces.
    
    ---
    
     Join our Discord →  &nbsp;&nbsp;&nbsp;  Read the Docs →  &nbsp;&nbsp;&nbsp;  Go to the AG-UI Dojo →  &nbsp;&nbsp;&nbsp;  Follow us → 
    
    ## 🚀 Getting Started
    Create a new AG-UI application in seconds:
    ```bash
    npx create-ag-ui-app my-agent-app
    ```
    
     Useful Links:
    
    - The AG-UI Dojo
    - Build AG-UI-powered applications(Quickstart)
    - Build new AG-UI framework integrations (Quickstart)
    - Book a call to discuss an AG-UI integration with a new framework
    - Join the Discord Community
    
    ## What is AG-UI?
    
    AG-UI is an open, lightweight, event-based protocol for agent-human interaction, designed for simplicity & flexibility:
    
    - During agent executions, agent backends **emit events _compatible_ with one of AG-UI's ~16 standard event types**
    - Agent backends can **accept one of a few simple AG-UI compatible inputs** as arguments
    
    **AG-UI includes a flexible middleware layer** that ensures compatibility across diverse environments:
    
    - Works with **any event transport** (SSE, WebSockets, webhooks, etc.)
    - Allows for **loose event format matching**, enabling broad agent and app interoperability
    
    It also ships with a **reference HTTP implementation** and **default connector** to help teams get started fast.
    
    Learn more about the specs →
    
    ## Why AG-UI?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  martin-olivier/airgorah
    ⭐ 6041 stars  |  🍴 1045 forks  |  💻 Rust  |  📅 2022-09-30
    🔗 https://github.com/martin-olivier/airgorah
    📡 来源: trending-daily
    🏷️ gui, kali, linux-app, security, security-audit, wifi, wifi-security, wireless
    📝 A WiFi security auditing software

    README 摘要:
    Airgorah
    
      A WiFi security auditing software
    
      Installation
      &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
      Usage
      &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
      Credits
    
    `Airgorah` is a WiFi security auditing software that can capture nearby WiFi traffic, discover clients connected to access points, perform deauthentication attacks, capture handshakes and PMKIDs, and crack the password of access points.
    
    It is written in Rust and uses GTK4 for the graphical part.
    
    `⭐ Don't forget to put a star if you like the project!`
    
    ## Legal
    
    ⚠️ Airgorah is designed to be used in testing and discovering flaws in networks you are owner of. Performing attacks on WiFi networks you are not owner of is illegal in almost all countries. I am not responsible for whatever damage you may cause by using this software.
    
    ## Requirements
    
    This software only works on `linux`. The graphical interface runs as a normal
    user (so it works under both `X11` and `Wayland`). When a privileged operation is
    needed, it launches a small privileged agent (`airgorah-agent`) via `polkit`,
    which will prompt for authentication once.
    
    You will also need a wireless network card that supports `monitor mode` and `packet injection`.
    
    ## Installation
    
    The installation instructions are available here.
    
    ## Usage
    
    The documentation about the usage of the application is available here.
    
    ## License
    
    This project is released under MIT license.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  libracoder/kiri
    ⭐ 4194 stars  |  🍴 204 forks  |  💻 Rust  |  📅 2026-11-02
    🔗 https://github.com/libracoder/kiri
    📡 来源: 🚀 两周800+星
    🏷️ containers, docker, kubernetes, linux, macos, oci, windows
    📝 A small, fast container runtime for macOS, Windows and Linux with free Ngrok alternative

    README 摘要:
    A tiny, fast container runtime for macOS, Windows and Linux.
      Runs your Docker images and works with the docker CLI, Compose and buildx you already use.
    
      Download ·
      Features ·
      Build from source ·
      Releases
    
      
      
      
    
      🇬🇧 🇮🇩 🇩🇪 🇪🇸 🇫🇷 🇮🇹 🇵🇱 🇧🇷 🇻🇳 🇹🇷 🇷🇺 🇸🇦 🇯🇵 🇰🇷 🇨🇳 🇹🇼
      Kiri speaks 38 languages. Is yours one?
    
      
    
    ---
    
    Kiri is a lightweight replacement for Docker Desktop and OrbStack, written in
    Rust. It runs containers in one small Linux VM (or straight on the kernel on
    Linux) and speaks the Docker Engine API, so your tools just work.
    
    The name comes from the Igbo word *ntakịrị*, "small".
    
    ## Why Kiri
    
    - **Fast**: a container starts and exits in about 2.5 ms through the Docker API. That's around 80 times faster than Docker Desktop.
    - **Light**: the VM sleeps after 60 s idle, the daemon stays at about 15 MB, and it wakes in about 0.15 s.
    - **Compatible**: `docker`, Compose, buildx, `docker login` and amd64 images through Rosetta.
    - **Local domains**: `http://.kiri.local`, with HTTPS from Kiri's own certificate authority.
    - **More than containers**: a one-command Kubernetes cluster and Linux machines.
    - **A native window** for containers, images, volumes and networks, plus a menu bar item.
    - **In your language**: 38 languages, on macOS, Windows and Linux alike.
    
    ### In your language
    
    Kiri's window and setup come in these languages. It follows your system's language, and you can change it in Settings → Appearance. In Arabic, Persian and Central Kurdish the whole window reads right to left.
    
    | | Language | | Language | | Language | | Language |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  Tencent/LoopForge
    ⭐ 1022 stars  |  🍴 233 forks  |  💻 Go  |  📅 2026-07-28
    🔗 https://github.com/Tencent/LoopForge
    📡 来源: trending-daily
    🏷️ agent-orchestration, agentic-workflow, ai-agents, ai-coding, claude-code, code-review, codebuddy, codex, coding-agents, cursor
    📝 Self-hosted workflows for coding-agent delivery. Orchestrate CodeBuddy, Codex and Claude Code with scripts and human approval gates. Includes Local workflows for coding assistants.

    README 摘要:
    English · 简体中文
    
      Two ways to work ·
      Quick start ·
      SOPs ·
      Features ·
      Local ·
      FAQ ·
      Docs
    
    https://github.com/user-attachments/assets/8af401d9-1aae-427c-b4bc-455c12d17beb
    
    80-second product tour (1080p, with sound).
    
    **LoopForge** is a self-hosted workspace where your team ships software with coding agents. Describe what you need to **Main Bot** in chat: it opens a Docker sandbox, checks out your repositories, delegates to project roles, and opens the PR. When a way of working proves itself, save it as an **SOP** (a standard workflow of agents, scripts and human gates) so the next requirement is delivered the same way, with review and approval built in.
    
    Coding-agent CLIs do the work: CodeBuddy, Codex, Claude Code, OpenCode, Cursor CLI, Antigravity, Kimi Code, Pi, DeepSeek Harness and ZCode. LoopForge adds the roles, sandboxes, checkpoints and history around them, all on your own infrastructure under the MIT license.
    
    ## Two ways to work
    
    | | **Chat with Main Bot** | **Run an SOP** |
    | --- | --- | --- |
    | Best for | Exploring, quick fixes, iterating with the agent | Repeatable delivery with fixed stages and sign-off |
    | How it runs | Main Bot opens a conversation workspace (a Docker sandbox with your repos) on demand and calls project roles as subagents | The engine runs Agent, Script, Human-gate and sub-SOP nodes in order, in their own sandbox |
    | You stay in control by | Queuing or steering messages mid-reply, and pausing, resuming or taking over a running SOP from chat | Approving at human gates, sending work back to a chosen step, retrying or rerunning from any node |
    | Delivers | A PR/MR, or a direct merge into a shared branch (`mode=direct`) | Documents, code or a PR, plus per-node artifacts and logs |
    
    Both paths track the same **requirements**, so every change, whether made in chat or by an SOP, links back to what was asked for and counts toward delivery and cost reports.
    
      
        
        
      
    
    The chat home. Type a request, @ a role, skill, requirement, SOP or repository, and pick the executor, model and permission mode per conversation.
    
    ## Why LoopForge
    
    Ask a coding agent to "fix this bug" and the result depends on that run. It might skip the plan, forget the tests, review its own code, or stop halfway without anyone noticing. That's fine for a demo, but it isn't how a team ships.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  ⚠️风险  Eynnzerr/TelemetryCleaner
    ⚠️ 命中风险词: poc —— 默认归排除区，需人工确认
    ⭐ 724 stars  |  🍴 66 forks  |  💻 Kotlin  |  📅 2026-11-11
    🔗 https://github.com/Eynnzerr/TelemetryCleaner
    📡 来源: 🚀 5天300+星
    📝 基于 Shizuku 免 Root 清除国产安卓 SystemHelper、RegService 等系统预装隐私数据收集模块

    README 摘要:
    # 遥测清理 · TelemetryCleaner
    
    > 运营商为终端入网、自注册、网络运维和故障排查，确有在相应场景收集必要数据的实际需求！本项目仅供学习，用于了解 Android 系统包管理机制。
    
    TelemetryCleaner 可以检测国行 Android 固件预置的运营商组件，查看各空间的安装状态和权限，并管理卸载与恢复。下载： GitHub Releases
    
      
      
      
    
    您可通过不限于以下方式参与贡献，欢迎 PR：
    1. 提供清单未覆盖的厂商+运营商+包名线索，在 README.md 中补充即可；
    2. 提供针对某模块的实测与分析报告，不限制是否为 AI 生成，但需保证真实性。放于 docs 目录中即可；
    3. 协助实现未支持的免 Root 卸载功能（如**现版本不支持部分 vivo 系的电信/移动组件卸载**）；
    4. 对软件功能的反馈或改进。
    
    ## 背景介绍
    
    部分国产厂商在国行固件中预置了 `SystemHelper`、`RegService` 等运营商终端管理组件。这些组件在后台静默定时采集数据，用户无感；没有桌面入口，同时无法以常规手段禁用权限和卸载。
    
    WiSec 2023 的流量测量还在部分国行样机上观察到运营商组件上报数据，其中小米及 ColorOS 样本的中国移动组件上报了已安装软件列表。 WiSec 2023 实测论文
    
    在作者本人的 OPPO 真机上观测到 SystemHelper 有读取定位、设备和 SIM 标识、已安装应用以及按应用统计网络流量，随后向某云端上传的行为，分析详见 SystemHelper 代码与权限分析 by AI。
    
    ## 本项目原理
    
    Android 10 及以上设备可安装本项目，依赖 Shizuku。先按 Shizuku 启动指南通过 ADB 或无线调试启动 Shizuku，再回到 App 授权并选择需要检查的空间。Android 11 及以上可用无线调试启动。检测完成后，可打开组件详情查看权限，或勾选组件批量操作。
    
    ADB 启动的 Shizuku 以 shell 身份代理 Binder 调用。App 直接请求系统包管理服务，避开部分 ROM 对 `pm` 命令行入口的拦截。系统包管理服务仍会执行本机的权限和包状态校验。 Binder 调用实现
    
    少数 ROM 会在命令层直接拒绝卸载系统应用，例如返回 `Failure [only root can delete system app for a particular user]`。收到这类系统错误后，App 会以 shell 身份通过 `app_process` 调用隐藏的 `IPackageManager.deletePackageAsUser` 再试一次；重新读取包状态确认失败后，结果页仍显示原始系统错误，不会用兜底流程的错误信息覆盖它。 app_process 兜底实现
    
    卸载按选定空间执行，会清除该空间中的组件数据。恢复使用系统保留的 APK。自动清理默认关闭，开启后按配置的周期检查所选空间，只处理自动清理名单内的组件。
    
    ## 内置组件清单
    
    表中的「未验证」指尚无本人在相应厂商设备上的卸载验证。
    
    | 厂商 | 运营商 | 包名 | 卸载验证 |
    | --- | --- | --- | --- |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  opencoredev/islandcn
    ⭐ 692 stars  |  🍴 56 forks  |  💻 TypeScript  |  📅 2026-11-13
    🔗 https://github.com/opencoredev/islandcn
    📡 来源: 🚀 5天300+星
    🏷️ dynamic-island, nextjs, react, shadcn, typescript, ui-components
    📝 The open-source Dynamic Island for React, installed with shadcn.

    README 摘要:
    # islandcn
    
    A Dynamic Island-style component for any React app, installed with shadcn. Show an upload, a timer, a song, a ride on its way, an incoming call or a recording in one island at the top of your app, and shape each activity around your app's own actions.
    
    ```bash
    npx shadcn@latest add https://islandcn.dev/r/island-core.json
    ```
    
    ```tsx
    "use client";
    
    import { Island, IslandProvider, useIsland } from "@/lib/island";
    
    // Mount once near the root.
    
      
      
    ;
    
    // Then, from any component inside it:
    const island = useIsland();
    const upload = island.start({
      id: "upload",
      label: "Uploading report.pdf",
      compact: { leading: , trailing:  },
      expanded: { center: report.pdf, bottom:  },
    });
    upload.update({ compact: { trailing:  } });
    upload.end();
    ```
    
    ## What's here
    
    - **The engine** (`lib/island/`, registry item `island-core`): the activity stack, four presentations (idle, compact, the split, expanded), springs fitted to frame-by-frame recordings of the real island, long-press, alerts and reduced motion. React only.
    - **Presets** (`components/islandcn/`): upload, timer, now playing, incoming call, ride or delivery ETA, recording, nearby transfer, battery and the split, each one file on the engine, plus the content kit they share.
    - **The playground** (`/playground`): build an island for your app from a preset or a blank activity, fire every action, tune the motion and copy the install command and the code.
    - **The site and docs** (`app/`, `docs/content/`).
    
    Coding agents can use the optional `islandcn-skill` registry item as an install helper; see `/docs/agent-skill`.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  Topkiflare74/ai--manus2.0
    ⭐ 678 stars  |  🍴 5 forks  |  💻 None  |  📅 2026-11-14
    🔗 https://github.com/Topkiflare74/ai--manus2.0
    📡 来源: 🚀 5天300+星
    🏷️ ai, ai-agents, ai-sdk, anthropic, chatbot, function-calling, gemeni, generative-ai, llm, multimodal
    📝 AI Manus is a general-purpose AI Agent system that supports running various tools and operations in a sandbox environment.

    README 摘要:
    # Manus - Autonomous AI Agent
    
    PROMO2026
    ---
    
    ## Manus Highlights
    
    - **Autonomous Code Execution:** Manus AI agent runs code on its own to complete tasks, so you can focus on decisions instead of repetitive typing and debugging.
    - **Browser Control Made Simple:** Manus browser control lets the agent navigate websites, fill forms, and gather information without you manually clicking through every page.
    - **Task Automation For Daily Life:** Manus autonomous tasks handle small but time-consuming jobs, from organizing research to scheduling reminders, keeping your day running smoothly.
    - **Personal Assistant That Works Quietly:** Manus personal assistant stays ready in the background, responding when you need help with study, home projects, or light work tasks.
    - **Code And Browser In One Flow:** Manus code automation connects scripting with real browser actions, so your workflows move from idea to result without switching between tools.
    
    ---
    
    ## What Is Manus
    
    Manus is an autonomous AI agent designed to run code and control a browser on your behalf. Instead of acting like a simple chatbot that only answers questions, Manus AI agent takes action. It can write and execute scripts, open web pages, interact with elements, and carry out multi-step tasks with minimal supervision. This makes Manus code automation useful for anyone who wants to reduce manual effort without learning a full programming stack.
    
    The core idea behind Manus browser control is practical freedom. You describe what you need, and the agent figures out the steps. Whether that means checking a website for updated information, filling out a repetitive form, or testing a small script, Manus autonomous tasks turn your instructions into completed actions. Manus personal assistant works quietly in the background, ready whenever you need to delegate a small but annoying job.
    
    Manus is not a heavy studio suite or a complex enterprise platform. It is a focused helper built for home, study, and small tasks. Students can use Manus code automation to organize research notes or run quick calculations. Remote workers can rely on Manus browser control to gather data from multiple pages. Anyone juggling several small projects can let Manus autonomous tasks handle the repetitive parts while they focus on the parts that need human judgment.
    
    Over longer sessions, Manus personal assistant proves its value through consistency. You do not need to re-explain the same workflow every time. Manus AI agent remembers th

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  WarriorRemember/IPTV_Player_2.0
    ⭐ 673 stars  |  🍴 12 forks  |  💻 Rust  |  📅 2026-11-14
    🔗 https://github.com/WarriorRemember/IPTV_Player_2.0
    📡 来源: 🚀 5天300+星
    🏷️ dash, ip-tv, iptv, iptv-channels, iptv-m3u8, iptv-player, iptv-player-application, iptvtools, m3u, mag
    📝 🎬 A powerful, intuitive IPTV streaming app supporting M3U playlists, EPG, and community lists. Available for Windows, macOS, Linux, Android & TV Boxes. 

    README 摘要:
    # 📺 MegaCubo Free – Stream Live TV Channels in 4K Without Limits [2026]
    
      
      
      
      
      
    
      
    
      
        
      
    
     
    
    ---
    
    ## 🎴 Feature Cards
    
      
        
          
        
        
          
        
        
          
        
      
    
    ---
    
    ## 🎯 What Is MegaCubo Free?
    
    **MegaCubo Free** is a powerful IPTV player that gives you access to thousands of free TV channels from around the world in stunning 4K quality. Whether you're into news, sports, movies, or documentaries, MegaCubo Free has something for everyone.
    
    **No more:**
    - ❌ Expensive cable subscriptions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  trackboatwrightplan/GitHub-Copilot-app
    ⭐ 672 stars  |  🍴 12 forks  |  💻 None  |  📅 2026-11-14
    🔗 https://github.com/trackboatwrightplan/GitHub-Copilot-app
    📡 来源: 🚀 5天300+星
    🏷️ adminlte, agent-skills, ai, awesome, chatgpt, copilot, github-copilot, hacktoberfest, microsoft-copilot, openai
    📝 The GitHub Copilot app is an agent-native desktop experience for finding, running, steering, and landing software work across your GitHub repositories. 

    README 摘要:
    # GitHub Copilot app
    
    The GitHub Copilot app is an agent-native desktop experience for finding, running, steering, and landing software work across your GitHub repositories.
    
      
        
      
    
    https://github.com/user-attachments/assets/50f215b5-f708-444e-83f7-3303bfa97963
    
    ## The GitHub Copilot app
    
    The GitHub Copilot app is an agent-native desktop experience for managing software work from idea to pull request. It gives you a single control center for finding the right work to pick up, starting and steering agents, reviewing progress, and landing changes across repositories without constantly switching between terminals, editors, browser tabs, and GitHub pages.
    
    The app is built for parallel agent-driven development. Each local session runs in its own isolated git worktree, and cloud sessions let agents keep working in isolated GitHub-hosted environments that you can pick up from anywhere. That means you can have Copilot investigate bugs, implement issues, address review feedback, or explore changes side by side without branches or files colliding.
    
    Canvases turn agent work into shared, inspectable surfaces. Instead of burying plans, terminals, browser previews, diffs, and workflow state in a chat thread, canvases give you a place to see what an agent is doing, edit or redirect the work, and verify progress in context.
    
    But we also know as developers, much our time has always been devoted to tasks that aren't 'just' writing code. My Work brings together sessions, issues, pull requests, and repository context so you can decide what needs attention next. Automations turn repeatable prompts and workflows into scheduled or background tasks. Agent Merge helps carry pull requests through review, checks, and merge conditions so you stay focused on judgment, quality, and delivery.
    
    ## Getting started
    
    ### Prerequisites
    
    - Git
    - A GitHub Copilot plan — any plan works, including Copilot Free and GitHub Copilot Student. No Copilot plan? You can still use the app by bringing your own key (BYOK) with your own model provider.
    
    ### Install
    
    Download the app for your platform:
    
    You can also browse all builds on the Releases page.
    
    For setup and a walkthrough of your first session, see the documentation.
    
    ## This repository
    
    This repo is the public home for the GitHub Copilot app. Use it to:
    
    - Download releases from the Releases page

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  TrapAccountant/GitHub-Copilot-app
    ⭐ 670 stars  |  🍴 12 forks  |  💻 None  |  📅 2026-11-14
    🔗 https://github.com/TrapAccountant/GitHub-Copilot-app
    📡 来源: 🚀 5天300+星
    🏷️ adminlte, agent-skills, ai, awesome, chatgpt, copilot, github-copilot, hacktoberfest, microsoft-copilot, openai
    📝 The GitHub Copilot app is an agent-native desktop experience for finding, running, steering, and landing software work across your GitHub repositories. 

    README 摘要:
    # GitHub Copilot app
    
    The GitHub Copilot app is an agent-native desktop experience for finding, running, steering, and landing software work across your GitHub repositories.
    
      
        
      
    
    https://github.com/user-attachments/assets/50f215b5-f708-444e-83f7-3303bfa97963
    
    ## The GitHub Copilot app
    
    The GitHub Copilot app is an agent-native desktop experience for managing software work from idea to pull request. It gives you a single control center for finding the right work to pick up, starting and steering agents, reviewing progress, and landing changes across repositories without constantly switching between terminals, editors, browser tabs, and GitHub pages.
    
    The app is built for parallel agent-driven development. Each local session runs in its own isolated git worktree, and cloud sessions let agents keep working in isolated GitHub-hosted environments that you can pick up from anywhere. That means you can have Copilot investigate bugs, implement issues, address review feedback, or explore changes side by side without branches or files colliding.
    
    Canvases turn agent work into shared, inspectable surfaces. Instead of burying plans, terminals, browser previews, diffs, and workflow state in a chat thread, canvases give you a place to see what an agent is doing, edit or redirect the work, and verify progress in context.
    
    But we also know as developers, much our time has always been devoted to tasks that aren't 'just' writing code. My Work brings together sessions, issues, pull requests, and repository context so you can decide what needs attention next. Automations turn repeatable prompts and workflows into scheduled or background tasks. Agent Merge helps carry pull requests through review, checks, and merge conditions so you stay focused on judgment, quality, and delivery.
    
    ## Getting started
    
    ### Prerequisites
    
    - Git
    - A GitHub Copilot plan — any plan works, including Copilot Free and GitHub Copilot Student. No Copilot plan? You can still use the app by bringing your own key (BYOK) with your own model provider.
    
    ### Install
    
    Download the app for your platform:
    
    You can also browse all builds on the Releases page.
    
    For setup and a walkthrough of your first session, see the documentation.
    
    ## This repository
    
    This repo is the public home for the GitHub Copilot app. Use it to:
    
    - Download releases from the Releases page

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#11  TurquoiseDetective/IPTV_Player_2.0
    ⭐ 669 stars  |  🍴 12 forks  |  💻 Rust  |  📅 2026-11-14
    🔗 https://github.com/TurquoiseDetective/IPTV_Player_2.0
    📡 来源: 🚀 5天300+星
    🏷️ dash, ip-tv, iptv, iptv-channels, iptv-m3u8, iptv-player, iptv-player-application, iptvtools, m3u, mag
    📝 🎬 A powerful, intuitive IPTV streaming app supporting M3U playlists, EPG, and community lists. Available for Windows, macOS, Linux, Android & TV Boxes. 

    README 摘要:
    # 📺 MegaCubo Free – Stream Live TV Channels in 4K Without Limits [2026]
    
      
      
      
      
      
    
      
    
      
        
      
    
     
    
    ---
    
    ## 🎴 Feature Cards
    
      
        
          
        
        
          
        
        
          
        
      
    
    ---
    
    ## 🎯 What Is MegaCubo Free?
    
    **MegaCubo Free** is a powerful IPTV player that gives you access to thousands of free TV channels from around the world in stunning 4K quality. Whether you're into news, sports, movies, or documentaries, MegaCubo Free has something for everyone.
    
    **No more:**
    - ❌ Expensive cable subscriptions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#12  ⚠️风险  UlricagglenMonster/aion-2-prompt-rpocket-engineering-suite
    ⚠️ 命中风险词: poc —— 默认归排除区，需人工确认
    ⭐ 50 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-14
    🔗 https://github.com/UlricagglenMonster/aion-2-prompt-rpocket-engineering-suite
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-cheat, aion-2-download, aion-2-dps-meter, aion-2-farming-routes, aion-2-game, aion-2-guide, aion-2-hack, aion-2-kina
    📝 Aion 2 Trainer Tool: Complete Standalone Setup With Advanced AI Prompt Engineering

    README 摘要:
    (README 获取失败)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#13  mit-han-lab/EvolvingInfra
    ⭐ 44 stars  |  🍴 3 forks  |  💻 Python  |  📅 2026-11-10
    🔗 https://github.com/mit-han-lab/EvolvingInfra
    📡 来源: 🤖 AI / LLM / RAG | 新建 | LLM agent framework
    🏷️ distributed-systems, llm, llm-agents, system
    📝 A inference framework that adapt to diverse and dynamic agent workload

    README 摘要:
    Evolving Infra: Agent-Adaptive LLM Serving at Scale
    
      
      Corresponding author: hao.kang.sys@gmail.com
    
    | Website | Paper | Wiki |
    
      
      
      
      
      
      
      
    
    > [!TIP]
    > **This is an agent-native repository.** Use your coding agent (Claude Code, Codex, ...) to
    > understand, deploy, benchmark and develop Evolving Infra. It reads `AGENTS.md` for
    > the rules and the map of the code, and follows a skill for each task.
    
    ---
    
    https://github.com/user-attachments/assets/d158ee7e-d554-47f0-a40f-1db343a6cf91
    
    Evolving Infra is an LLM serving system that adapts itself to the agent workload **purely online**,
    with **no offline profiling**. Serving coding, math and computer-use agents with GLM-5.2 and Kimi K2.6
    on up to 256 GB300 GPUs, it reduces mean end-to-end latency by up to **4.1×** and P95 time to
    first token by up to **14×** compared with NVIDIA Dynamo,
    with up to **2.7×** its throughput.
    
      
      Math (Putnam), coding (Claude Code) and computer-use (OSWorld) agents, three concurrency levels each. Lower is better.
    
    ## About
    
    Evolving Infra adapts online through three designs:
    
    1. **Decouple** compute allocation from KV cache management, so online adaptation is cheap: a node
       switches between prefill and decode **in seconds, without a restart**, and its KV cache stays in
       a host-memory pool that every node can read.
