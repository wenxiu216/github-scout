📊 开源日报 — 2026-11-27
共发现 5 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  obsidianmd/obsidian-skills
    ⭐ 54147 stars  |  🍴 3852 forks  |  💻 Shell  |  📅 2026-01-02
    🔗 https://github.com/obsidianmd/obsidian-skills
    📡 来源: trending-weekly
    🏷️ agents, agentskills, bases, chatgpt, claude, claude-code, claude-skills, cli, codex, defuddle
    📝 Teach your agent to use Obsidian and open formats including Markdown, Bases, JSON Canvas.

    README 摘要:
    Agent Skills for use with Obsidian.
    
    These skills follow the Agent Skills specification, so they work with any agent that supports skills, including Claude Code, Claude, ChatGPT, Antigravity, Cursor, GitHub Copilot, Grok Bot, Hermes Agent, Kiro, Muse, OpenCode, and many more.
    
    ## Installation
    
    Obsidian is an official plugin for Claude, ChatGPT, Dots, Cursor, Grok Bot, Hermes, and Kiro. Most other agents can install the skills from GitHub.
    
    ### Claude
    
    Add Obsidian from the official Claude plugin directory.
    
    For the Claude Code CLI use:
    
    ```sh
    claude plugin marketplace add obsidianmd/obsidian-skills
    claude plugin install obsidian@obsidian-skills
    ```
    
    From within a Claude Code session:
    
    ```sh
    /plugin marketplace add obsidianmd/obsidian-skills
    /plugin install obsidian@obsidian-skills
    ```
    
    To get new skills later, run `claude plugin update obsidian@obsidian-skills`.
    
    ### ChatGPT
    
    Add Obsidian from the ChatGPT plugin directory. The plugin works in ChatGPT, Codex, and Dots.
    
    To install from this repo instead:
    
    ```sh
    codex plugin marketplace add obsidianmd/obsidian-skills
    ```
    
    Then install Obsidian from the plugin directory in Codex or the ChatGPT desktop app.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  alesha-pro/llm.asm
    ⭐ 1792 stars  |  🍴 277 forks  |  💻 Assembly  |  📅 2026-11-25
    🔗 https://github.com/alesha-pro/llm.asm
    📡 来源: 🚀 5天300+星
    🏷️ assembly, avx2, bare-metal, llm, machine-learning, nasm, osdev, qwen, transformer, x86-64
    📝 Qwen3-0.6B inference (12 KB), bare-metal bootable OS (22 KB), and from-scratch Mini-GPT trainer with live Braille TUI (32 KB) in 100% pure x86-64 NASM assembly. Zero C, zero libc, zero dependencies.

    README 摘要:
    # llm.asm
    
    **Three complete LLM projects written in 100% pure x86-64 NASM assembly.**
    Zero C, zero C++, zero Rust, zero libc, zero libm, zero runtime dependencies.
    
    Assembled directly with `nasm` and linked with `ld`. Every math kernel (`expf`, `sincosf`, `RMSNorm`, `RoPE`, `SiLU`, `Softmax`), AVX2+FMA+F16C GEMM/GEMV engine, BPE tokenizer, `clone()`/`futex()` thread pool, bare-metal SMP kernel, analytical backward pass, AdamW optimizer, and live Unicode Braille TUI is hand-written x86-64 assembly (`17,252` lines total across all three projects).
    
    ## The Trilogy
    
    | Project | Binary | Size | Deps | Key Numbers |
    |---|---|---:|---:|---|
    | **01-qwen3-inference/** | `build/asm-llm` | **14,712 B** *(14,008 B `FAST_Q8=0`)* | **0** | Static Linux ELF running `Qwen/Qwen3-0.6B` (Q8_0, built-in BPE tokenizer, GQA + QK-Norm + RoPE + SwiGLU, single-shot & `--chat` multi-turn KV-cache REPL). **`FAST_Q8=1` (default):** **126.8 tok/s** decode at 40T (**20.7 tok/s** at 1T), **+18% to +36% faster than `llama.cpp` CPU (`Q8_0`) across 1..40T**, **`0.99965`** cosine & **64/64** exact greedy tokens vs PyTorch FP32. |
    | **02-baremetal-os/** | `build/asm-llm-os.elf` | **24,252 B** *(23,612 B `FAST_Q8=0`)* | **0** | Bootable bare-metal `Qwen3-0.6B` OS with no Linux or Windows. Multiboot 1 -> Long Mode -> AVX2/FMA/F16C -> ACPI/APIC SMP -> VGA + PS/2 + COM1 multi-turn KV-cache chat (`/clear`, `/think`, `/bench`). **74–94 ms** boot, **134.9 tok/s** KVM EPYC (**23.7 tok/s** 1 vCPU, **136.6 tok/s** peak), **55.4 tok/s** live on Proxmox Xeon E5-2670 v3 with **0 GB** disk. |
    | **03-minigpt-train/** | `build/asm-gpt-train` | **32,944 B** | **0** | From-scratch FP32 Mini-GPT trainer and sampler. Register-blocked `6x16` AVX2+FMA SGEMM, full analytical backward pass (**`1.0000000000`** cosine across all 21 gradient tensors vs PyTorch CPU), decoupled AdamW, **27,662 train tok/s**, live 80x24 Braille TUI, `val_loss 4.19 -> 1.51` on TinyShakespeare in 4 min. |
    
    ---
    
    ## Head-to-Head CPU Decode Benchmark: `llm.asm` vs `llama.cpp` (`Qwen3-0.6B Q8_0`)
    
    Measured on the same machine (**AMD EPYC 7642**, 47C online, 256 MiB L3, DDR4, CPU-only `-ngl 0`), same model (`Qwen3-0.6B Q8_0`: `613.66 MiB` `.asmbin` v2 FP16-scale vs `604.15 MiB` GGUF `Q8_0`), `34` prompt tokens / `64` generated tokens, `3`-run average:
    
    | Threads | `llm.asm` (`FAST_Q8=0`, FP32 act) | `llama.cpp` (`Q8_0`, `-ngl 0`) | **`llm.asm` (`FAST_Q8=1`, 14.7 KB)** | **vs `llama.cpp`** | **Bare-Metal OS KVM (`FAST_Q8=1`)** |
    |---:|---:|---:|

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  nexu-io/opengame
    ⭐ 1636 stars  |  🍴 273 forks  |  💻 TypeScript  |  📅 2026-11-25
    🔗 https://github.com/nexu-io/opengame
    📡 来源: 🚀 5天300+星
    🏷️ agent-skills, ai-agents, ai-game-generator, claude-code, codex, deepseek, deepseek-harness, dsh, dsh-plugin, game-development
    📝 The Super Game Agent — the Unity & Unreal for AI agents, with 100+ viral games to remix. Turn 20+ coding agents (Claude Code, Codex, DeepSeek, etc.) into a full-stack AI game studio. Build and publish 3D & mini-games to WeChat, Douyin, TikTok, Telegram, itch.io, and more.

    README 摘要:
    The First Super Game Agent — Open-Source Full-Stack AI Game Studio
    
      
    
      
      
      
    
      
      
      
      
      
      
    
    Quick Start · Agents · Playable Templates · Why OpenGame · Publish &amp; Monetize · Setup &amp; MCP · Community
    
    **English** · 简体中文 · 日本語
    
    # Introducing OpenGame
    
    OpenGame is **the first open-source Super Game Agent** — turning **DeepSeek (DSH)**, **Claude Code**, **Codex**, or any of your local coding agents into an AI Unreal Engine / Unity and full-stack game studio. Go from a single idea to **AAA-grade 3D worlds** or **monetization-ready viral mini-games** in one end-to-end pipeline.
    
    - 🚀 **Build AAA-Grade 3D Games with Your Agent.** Drive full-stack 3D gameplay, art, music, and voice straight from **DeepSeek (DSH)**, **Claude**, **Codex**, or **Gemini** — from one prompt to playable 3D action, racing, and open-world games.
    - 🎮 **One-Click Remix & Re-style Any Game.** Start from **25 built-in playable templates** (3D, voxel, anime, pixel & 9:16 hits) with full editable source — keep proven mechanics while swapping characters, worlds, and art styles in minutes.
    - 💰 **Build Games That Earn: Create → Verify → Monetize.** Automated logic checks, balance simulation, headless playtesting, covers, and gameplay trailers — ship live web links, export single-file **9:16 Playable Ads**, and connect publishing paths for **WeChat Mini Games**, **TikTok**, and **Douyin**.
    - 🔓 **Full-Stack Open Source (BYOA + BYOK).** Code, art, video, music, voice, SFX, and Three.js 3D are all open source — plug in your favorite local agent and own API keys, or connect OpenDesign Go (Black Friday lowest-ever discount, with free access to **DeepSeek V4.1 Flash**, **Seedream**, and more).
    
     
    
    ## ⚡ Quick Start
    
    ### 1. Give one prompt to your local Agent
    
    Paste this instruction into **DeepSeek TUI / Harness**, **Claude Code**, **Codex**, **WorkBuddy**, **Cursor**, **Gemini CLI**, or any of the 22 supported local agents:
    
    ```text
    Follow https://github.com/nexu-io/opengame/blob/main/docs/opengame-setup.md to connect OpenGame to this agent and open the Game Studio template gallery.
    ```
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  Reukix/Reloc
    ⭐ 1126 stars  |  🍴 215 forks  |  💻 Swift  |  📅 2026-11-25
    🔗 https://github.com/Reukix/Reloc
    📡 来源: 🚀 5天300+星
    📝 iOS accessory-level location simulator over local loopback (iAP2 / MFi-v3 / NMEA)

    README 摘要:
    Reloc
      面向 iOS 的外设级定位模拟工具
      
        基于 Swift、Objective-C 与 Rust FFI 构建 · 通过本机回环实现 iAP2 / MFi-v3 / NMEA 外设定位注入
      
      
        
        
        
      
    
    ---
    
    ## 简介
    
    **Reloc** 是一款运行在 iPhone 本机的外设级定位模拟应用。应用通过外部代理提供的本地回环（`10.7.0.1`）连接系统的 `com.apple.carkit.service` 服务，完成 Remote Pairing / Lockdown 会话协商、iAP2 链路同步、MFi-v3 鉴权与 NMEA-0183（`$GPGGA` / `$GPRMC`）报文流式下发，使系统以标准外设 GPS 身份接收实时坐标。
    
    ---
    
    ## 核心功能
    
    | 模块 | 能力说明 |
    | :--- | :--- |
    | **定格定位** | 地图点击选点、关键词搜索、手动输入 WGS-84 坐标、多级反地理编码（`CLGeocoder` → `Nominatim` → `BigDataCloud` 兜底不卡顿）、运行中浏览并热更新定位 |
    | **多源地图与纠偏** | 默认使用 **Apple 地图（MapKit 原生）** 并支持中国大陆 GCJ-02 ↔ WGS-84 自动双向纠偏；同时内置免 API Key 的 **全球街道图（Esri） / OpenStreetMap / 全球卫星图** 纯原生 WGS-84 瓦片地图（完全脱离 `MKMapView`，无高德字样）；可选 ±0.6 m 自然微漂移 |
    | **极速触发与优雅恢复** | iAP2 鉴权后延迟唤醒 `CoreLocation` + 自动脉冲订阅 `0xFFFA` + 初始高速锁定突发，首页实时显示外设生效状态；系统缓存顽固时提供 **一键刷新定位服务（PiP 悬浮 5 秒倒计时）**；停止定位时下发 NMEA 失效报文（`quality=0` / `V`）与 iAP2 `RST` 复位包并自动唤醒本机真实 GPS |
    | **后台保活** | 导航级后台定位保活 + 非零次声音频双保险；支持开关系统「定位服务」刷新缓存后自动重建后台断言，以及断线自动重连 |
    | **本机配对与导入** | 兼容 `.rppairing` / `.mobiledevicepairing` / `.mobilepair` / `.plist`；原生副本文件选择器避免置灰不可选，支持「用 Reloc 打开」直接导入；iOS 27+ 支持本机一键配对与 **画中画（PiP）悬浮指引窗** 实时展示 6 位配对码 |
    | **数据与实测** | 收藏夹（支持重命名 / 删除）、最近 30 条使用记录、异常中断一键恢复；内置 `CoreLocation` 实测面板（`isSimulatedBySoftware` / `isProducedByAccessory`）与协议日志筛选 |
    
    ---
    
    ## 系统兼容性
    
    | 设备 / 系统版本 | 日常脱离电脑运行 | 首次获取配对文件方式 | 说明 |
    | :--- | :---: | :--- | :--- |
    | **iPhone · iOS 27.0+** | 支持 | **本机一键配对**（免电脑）或导入已有文件 | 通过 `_remotepairing-pairable-host._tcp.` + 画中画悬浮窗完成配对 |
    | **iPhone · iOS 17.0 – 26.x** | 支持 | **需电脑通过 USB 首次导出**，导入后长期脱离电脑 | iOS 27 之前系统限制陌生主机无线首次配对 |
    | **iPad（iPadOS）** | **不支持** | — | iPadOS 不支持 CarPlay 且不提供 `com.apple.carkit.service` 外设通道，启动时将自动提示不可用 |
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  yzfly/LightRead
    ⭐ 154 stars  |  🍴 15 forks  |  💻 TypeScript  |  📅 2026-07-05
    🔗 https://github.com/yzfly/LightRead
    📡 来源: 📖 阅读/内容平台 | 活跃 | epub reader open source
    🏷️ android, arxiv, azw3, calibre, cross-platform, djvu, ebook-reader, epub, epub-reader, mobi
    📝 轻阅 LightRead · 免费开源的全格式电子书阅读器 Free open-source ebook reader: EPUB / PDF / MOBI / AZW3 / FB2 / TXT / DjVu / 漫画 · 点睛阅读、打字机等多种阅读模式 · 听书 TTS · PDF 对照翻译 · Windows / macOS / Linux / Android 多端同步

    README 摘要:
    # LightRead 轻阅 · 开源免费的全格式电子书阅读器
    
    **让想读的书，变成读进去的书。**
    
    EPUB / PDF / MOBI / AZW3 / TXT 全格式 · 点睛阅读 · 多种阅读模式 · 听书 · PDF 对照翻译 · 多端同步
    
    中文 · English
    
    **官网** · **下载桌面版** · **下载安卓 App** · 国内镜像（GitCode） · 使用手册 · 反馈建议
    
    Windows · macOS · Linux · Android · iOS（TestFlight 测试版）· 网页 PWA
    
    免费、开源、无广告。本地阅读无需账号、无需联网；藏书、进度与笔记默认留在自己的设备上。
    
    PDF 翻译 · 点睛阅读 · 书单 · 阅读记录 · 听书与专注
    
    ## 一眼看懂轻阅
    
    | | |
    | --- | --- |
    | 是什么 | 开源、本地优先的电子书与 PDF 阅读器，读书、读论文、听书都在一个应用里 |
    | 支持设备 | Windows 10 / 11、macOS（Apple 芯片与 Intel）、Linux（deb / rpm / AppImage）、Android（arm64）、网页 PWA |
    | 支持格式 | EPUB、PDF、MOBI、AZW、AZW3、FB2、TXT、Markdown、HTML、DjVu、CBZ / CBR 漫画，以及代码、日志等纯文本文件 |
    | 阅读模式 | 点睛阅读（重点词 / 要句标记）、打字机、歌词、仿生阅读、自动翻页与匀速滚动、听书跟读；夜读、护眼、墨水屏、大字、沉浸场景 |
    | 排版 | 翻页 / 按章滚动 / 跨章连续滚动，单栏 / 双栏，字号、行距、边距、字体、主题随手调；App 支持音量键翻页、PDF 重排 |
    | 多端 | 轻阅账号或 WebDAV 同步进度、笔记、书签、书单、阅读记录与设置；藏书包导入导出 |
    | 费用与隐私 | 免费，AGPL-3.0 开源；不需要账号即可使用，联网功能按需开启 |
    | 不支持 | KFX 与 DRM 加密文件 |
    
    ## 手机 App
    
    安卓 App 与桌面版共用同一套阅读引擎，界面按手机重新设计：底部标签栏、单手可达的阅读工具栏、底部抽屉面板。
    
    | 藏书 | 正文 · 点睛阅读 | 阅读模式 | 排版 · 音量键翻页 |
    | --- | --- | --- | --- |
    |  |  |  |  |
    
    | 听书 | 书源 | 阅读记录 |
    | --- | --- | --- |
    |  |  |  |
