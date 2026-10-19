📊 开源日报 — 2026-10-19
共发现 9 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  mlabonne/llm-course
    ⭐ 84180 stars  |  🍴 9792 forks  |  💻 None  |  📅 2023-06-17
    🔗 https://github.com/mlabonne/llm-course
    📡 来源: trending-daily
    🏷️ course, large-language-models, llm, machine-learning, roadmap
    📝 Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks.

    README 摘要:
    𝕏 Follow me on X • 
        🤗 Hugging Face • 
        💻 Blog • 
        📙 LLM Engineer's Handbook
      
    
    The LLM course is divided into three parts:
    
    1. 🧩 **LLM Fundamentals** is optional and covers fundamental knowledge about mathematics, Python, and neural networks.
    2. 🧑‍🔬 **The LLM Scientist** focuses on building the best possible LLMs using the latest techniques.
    3. 👷 **The LLM Engineer** focuses on creating LLM-based applications and deploying them.
    
    > [!NOTE]
    > Based on this course, I co-wrote the LLM Engineer's Handbook, a hands-on book that covers an end-to-end LLM application from design to deployment. The LLM course will always stay free, but you can support my work by purchasing this book.
    
    For a more comprehensive version of this course, check out the DeepWiki.
    
    ## 📝 Notebooks
    
    A list of notebooks and articles I wrote about LLMs.
    
    Toggle section (optional)
    
    ### Tools
    
    | Notebook | Description | Notebook |
    |----------|-------------|----------|
    | 🧐 LLM AutoEval | Automatically evaluate your LLMs using RunPod |  |
    | 🥱 LazyMergekit | Easily merge models using MergeKit in one click. |  |
    | 🦎 LazyAxolotl | Fine-tune models in the cloud using Axolotl in one click. |  |
    | ⚡ AutoQuant | Quantize LLMs in GGUF, GPTQ, EXL2, AWQ, and HQQ formats in one click. |  |
    | 🌳 Model Family Tree | Visualize the family tree of merged models. |  |
    | 🚀 ZeroSpace | Automatically create a Gradio chat interface using a free ZeroGPU. |  |
    | ✂️ AutoAbliteration | Automatically abliteration models with custom datasets. |  |
    | 🧼 AutoDedup | Automatically deduplicate datasets using the Rensa library. |  |
    
    ### Fine-tuning
    
    | Notebook | Description | Article | Notebook |
    |---------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  google-research/harness2
    ⭐ 7693 stars  |  🍴 687 forks  |  💻 Python  |  📅 2026-10-06
    🔗 https://github.com/google-research/harness2
    📡 来源: 🚀 两周800+星
    📝 无描述

    README 摘要:
    Recursive Agent Harnessing for an Open World
    
      
      
      
      
    
      
        
      
    
    A **harness** is the system around a model that enables it to act as an agent:
    prompts, tools, memory, skills, orchestration, and more. **Harnessing** is the
    process of optimizing that system.
    
    Harness² is a plug-and-play framework for **recursive agent harnessing** in an
    open world, where agents encounter tasks unseen during harness design. It
    connects two levels of recursion while keeping model weights fixed:
    
    * **Task-level recursion** refines the execution harness for the current task
      through a contrastive **Propose–Probe–Compose** step: propose edits, probe
      their effects on the same task, and compose a refined harness from behavioral
      contrasts between executions, without ground-truth feedback.
    * **Harnessing-level recursion** updates a persistent *improvement harness*
      with adopted harnesses and evidence-supported lessons from each task to guide
      future refinement.
    
      
        
      
    
    Across three professional benchmarks and four model–harness configurations, a
    single Harness² step improves GLM-5 and Gemini 3.5 Flash over their base
    harnesses, with gains of up to 11.5 points on WorkBuddy-Bench, 4.5 points on
    JobBench, and 11.8 percentage points on LAB's partial pass rate. Increasing the
    task-level recursion budget brings further gains.
    
    The release supports **parallel and sequential recursion**, **OpenCode and
    Codex executors**, and **JobBench, LAB, and WorkBuddy-Bench**.
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  Kruk2/jasna
    ⭐ 2553 stars  |  🍴 196 forks  |  💻 Python  |  📅 2026-01-18
    🔗 https://github.com/Kruk2/jasna
    📡 来源: trending-daily
    📝 Video restoration tool

    README 摘要:
    > **The only places to get a genuine License code for the supporter models are Buy Me a Coffee, Unifans, and for China the seller in the Chinese README.**
    >
    > **支持者模型的正版许可证码只能通过 Buy Me a Coffee、Unifans 或 闲鱼 获取。**
    
    **English** | 日本語 | 中文
    
    #  Jasna 
    
    Jasna restores mosaics in videos and images. It is free, has a simple app
    and a command line, and runs on your GPU.
    
    ## Contents
    
    **Start here**
    
    - What Jasna does
    - What you need
    - Quick start
    - Help and community
    - Supporting the project (supporter models)
    
    **Advanced**
    
    - How Jasna works
    - Command line
    - All guides
    - Benchmarks
    - Licensing
    - Acknowledgments
    
    ## What Jasna does
    
    - Finds mosaics in a video and restores them. The rest of the picture is not
      touched.
    - Two restoration models: fast **BasicVSR++** (free) and slow but more
      detailed **LTX** (for supporters, NVIDIA only).
    - Restores only the parts you choose, with a preview, in the **Segment
      Editor**.
    - Works with VR180 videos and still images (SD 1.5, for supporters).
    - Lets you watch a video restored live in the **Video Player**, without making

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  Gathin23/tv-vibehack
    ⭐ 2479 stars  |  🍴 296 forks  |  💻 Java  |  📅 2026-10-17
    🔗 https://github.com/Gathin23/tv-vibehack
    📡 来源: 🚀 5天300+星
    🏷️ ad-free, adb, android-tv, android-tv-launcher, bloatware-removal, claude-code, debloat, google-tv, hisense, home-screen
    📝 Your TV, minus the ads. Debloat any Android TV or Google TV over Wi-Fi and swap the ad-filled home screen for a clean Apple TV-style launcher. No root, fully reversible.

    README 摘要:
    # tv-vibehack
    
    **Your TV, minus the ads.**
    
    Strip the bloatware from any Android TV or Google TV over Wi-Fi, and replace the ad-filled home
    screen with a clean launcher that looks like an Apple TV.
    
    **No root, no cable, nothing uninstalled, and a one-line restore if you change your mind.**
    
    It started as an afternoon fixing my parents' Mi TV, which showed them an advert before they
    could reach Netflix. The whole thing was done with Claude Code talking to the real TV, and the
    prompt that did it is in this repo so you can do the same with yours. The replies to the
    tweet below are where most of the TV lists in
    this repo came from.
    
      
    
    ---
    
    ## Table of contents
    
    - How it works
    - Quick start
    - What you get
    - Supported TVs
    - Doing it by hand
    - The launcher
    - Troubleshooting
    - Questions people ask
    - Contributing
    - Licence
    
    ---
    
    ## How it works
    
    Android TVs have the same debug bridge as Android phones. Once you switch on USB debugging in the
    TV's developer options, the TV listens on your Wi-Fi and asks you once to allow your computer.
    After that, everything is standard Android tooling:
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  ly05010419/MacNativeGames
    ⭐ 1074 stars  |  🍴 182 forks  |  💻 C  |  📅 2026-10-17
    🔗 https://github.com/ly05010419/MacNativeGames
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # MacNativeGames
    
    # English
    
    > **Use your AI assistant to help you build the Mac app. We recommend Claude Code, Codex, or any other AI assistant you prefer.**
    
    English | 中文
    
    Play your own copy of **The Legend of Zelda: Tears of the Kingdom** natively on an Apple silicon Mac. Bring your game file (XCI or NSP) and your `prod.keys`; one script turns them into a Mac app. This project currently supports **Mac only**. It is not an emulator: the game's own ARM64 code runs directly on the Apple chip (rewritten only where macOS requires it), the Switch system services are answered by a small host, and the game's NVN graphics are rebuilt on Metal 4. Nothing from the game is in this repository, and the project is not affiliated with Nintendo.
    
    Update history:
    
    October 18: Added 1.4.3 support and shader prewarming before the first play session (about 10 minutes).
    October 17: Added 1.0.0 and 1.1.2 support. First-launch shader prewarming was not available yet, so new scenes could stutter.
    
    **Stuttering when you first start playing or enter a new scene is expected while new shaders compile—don't be surprised.** Performance typically improves as the cache warms up.
    
    ## Audio fix
    
    Streamed music and dialogue lookup for `content://Sound/...` paths has been fixed. Opening dialogue and music were verified locally on version 1.0.0; other versions and scenes still need validation. Rebuild your app with the original game inputs to apply the fix. See audio troubleshooting and validation for details.
    
    ## Local testing
    
    Tested on **MacBook Air M4 and Mac mini M4**. Local testing has collected **8,582 shaders**, with performance at approximately **90 FPS after shader warm-up, reaching 120 FPS in menus**.
    
    Those are earlier local observations, not a stable frame-rate promise for every version or scene. Version 1.4.3 measurements and compilation stalls are recorded separately in the test notes.
    
    Shaders are automatically collected, compiled and cached as you play. Returning to previously visited scenes typically brings noticeable improvements in frame rates and smoothness because cached shaders can be reused. **8,582 is the number collected so far in local testing, not the game's total shader count or a collection limit**; the cache continues to grow as you explore.
    
    **Shader prewarming on the first launch:** Building the app automatically prepares at least 8,000 shaders from your selected game data and includes them in the app. Even with an empty user cache, the first launch discover

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#6  LiCinCan/blender-ai-mcp-addon
    ⭐ 788 stars  |  🍴 377 forks  |  💻 Python  |  📅 2026-10-15
    🔗 https://github.com/LiCinCan/blender-ai-mcp-addon
    📡 来源: 🚀 5天300+星
    🏷️ ai-assistant, blender, blender-addon, blender-ai, blender-automation, blender-extension, blender-mcp, blender-plugin, blender-python, blender-scripting
    📝 AI assistant and MCP server for Blender: visual chat, scene tools, multi-agent workflows. Works with OpenAI, ChatGPT, Claude, Gemini, Ollama, OpenCode. Blender AI addon and plugin, copilot for 3D, bpy Python scripting, MCP integration.

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
#7  OpenMOSS/MOSS-Image
    ⭐ 756 stars  |  🍴 35 forks  |  💻 Python  |  📅 2026-10-16
    🔗 https://github.com/OpenMOSS/MOSS-Image
    📡 来源: 🚀 5天300+星
    🏷️ controllable-generation, foundation-models, image-generation, text-rendering, text-to-image
    📝 Official repository for MOSS-Image, a 5B-parameter base DiT model with high-quality text rendering, layout generation, and efficient fine-tuning.

    README 摘要:
    &nbsp;
        
        &nbsp;
        
        &nbsp;
        
        &nbsp;
        
        &nbsp;
        
        &nbsp;
        
        &nbsp;
        
        &nbsp;
        
        &nbsp;
        
        &nbsp;
        
        &nbsp;
        
      
      
        English &nbsp; | &nbsp; 简体中文
      
    
    ## News
    
    - **[2026-10-19]** 📄 The MOSS-Image Technical Report is now available on arXiv.
    
    - **[2026-10-16]** 🚀 MOSS-Image has day-0 support in SGLang, vLLM-Omni, and ComfyUI.
    
    - **[2026-10-16]** 🎉 We are introducing **MOSS-Image-Base** and **MOSS-Image-SFT**! Code and model weights are publicly available.
    
      **Our key highlights:**
    
      - 📐 **Layout control:** Control the placement of text and visual elements.
      - ✍️ **Strong text rendering:** Generate clear, accurate text within images.
      - 📜 **Long-prompt support:** Accept text prompts of up to 4K tokens.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#8  danishashko/geo-aeo-tracker
    ⭐ 299 stars  |  🍴 70 forks  |  💻 TypeScript  |  📅 2026-02-14
    🔗 https://github.com/danishashko/geo-aeo-tracker
    📡 来源: 🤖 AI / LLM / RAG | 活跃 | open source ChatGPT alte
    🏷️ aeo, ai-search, ai-visibility, answer-engine-optimization, brand-monitoring, chatgpt, copilot, gemini, generative-engine-optimization, geo
    📝 Open-source alternative to Profound and Otterly. Track how ChatGPT, Perplexity, Gemini, Copilot and Google AI Mode mention and cite your brand. Self-hosted, MIT, bring your own keys.

    README 摘要:
    GEO/AEO Tracker
    
      Open-source, self-hosted AI visibility tracker for GEO and AEO.
      Track your brand in ChatGPT, Perplexity, Gemini, Microsoft Copilot and Google AI Mode.
    
      Features · 
      Quick Start · 
      Deploy · 
      Cloud Sync · 
      API
    
    GEO/AEO Tracker is an open-source alternative to Profound, Otterly and AthenaHQ. Each run scores your brand from 0 to 100 on mentions, position, frequency, citations and sentiment, and adds citation analysis, competitor battlecards and SRO analysis. It is for marketers, SEO teams and founders who want to own their data and their code. The software is free under the MIT license. Bright Data, OpenRouter and Gemini bill per API call. Try the live demo.
    
    ---
    
    > 🌐 **Built with Bright Data** — the world's leading web data platform.
    > GEO/AEO Tracker uses Bright Data's AI Scraper API to reliably collect structured responses from 5 AI engines.
    > Get your API key →
    
    ---
    
    ## Why
    
    AI models are replacing traditional search for millions of queries. If your brand isn't visible in ChatGPT, Perplexity, or Gemini responses, you're invisible to a growing audience.
    
    Paid AI visibility tools run from $29 a month to custom enterprise quotes, and they keep your data on their servers. How it compares lists current prices and plan limits.
    
    **GEO/AEO Tracker** is the alternative:
    
    - 🔑 **BYOK** (Bring Your Own Keys): results are stored in your browser by default
    - 🤖 **5 AI engines** simultaneously: ChatGPT, Perplexity, Gemini, Copilot and Google AI Mode
    - 💸 **Free software, pay-per-call data**: the code is MIT licensed, and Bright Data, OpenRouter and Gemini bill per call
    - 🛡️ **Local-first** by default: IndexedDB + localStorage, no external database
    - ☁️ **Optional cloud sync** via your own Supabase project (free tier) for multi-device access
    
    ## How it compares
    
    | Tool | Plan and price | Engines on that plan | Prompt allowance | Open source / self-hosted | Where data lives |
    |------|-------------|-----------------------|------------------|---------------------------|------------------|
    | **GEO/AEO Tracker** | Free (MIT), you pay API providers per call | ChatGPT, Perplexity, Gemini, Copilot, Google AI Mode | No plan cap, limited by your API spend | Yes, MIT | Your browser (optional own Supabase) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#9  orylite/lindyson-ai
    ⭐ 31 stars  |  🍴 18 forks  |  💻 TypeScript  |  📅 2026-10-15
    🔗 https://github.com/orylite/lindyson-ai
    📡 来源: 🤖 AI / LLM / RAG | 新建 | AI image generation
    🏷️ ai-video, ai-video-generation, aigc, chatgpt, ecommerce, fastify, image-to-video, mcp, mcp-server, model-context-protocol
    📝 AI video & image generation workspace for e-commerce teams, built on Volcengine Seedance / Seedream, with MCP for ChatGPT & Codex · 面向电商团队的 AI 视频与图片生成工作台

    README 摘要:
    简体中文 · English
    
      
    
    Lindyson AI Video Generator
    
    把一张商品图，变成能直接发布的短视频和商品图
    
      面向电商与短视频团队的 AI 视频与图片生成工作台。
      开箱自带积分计费、订阅套餐、管理后台和 MCP 接口，换个品牌就能上线自己的 AI 生成服务。
    
      
    
      
      
      
      
      
      
    
      五分钟试玩 ·
      功能 ·
      准备密钥 ·
      部署上线 ·
      常见问题 ·
      二次开发 ·
      贡献 ·
      安全 ·
      联系我们
    
    ---
    
    ## 💡 为什么开源这个项目
    
    > 我们自身是做 TK 的跨境卖家，很多时候都在用 AI 生成视频跑业务。比起实拍，这样不仅省下了大笔成本，而且更容易做出爆款。后来在一些同行交流会上，不少同行就找过来，想让我们也帮他们提供这项服务。
    >
    > 久而久之我们发现，自己这边写脚本、做视频的人手，根本跟不上这么大的需求量了。这也让我们意识到，这个市场是有真实需求的。
    >
    > 所以我们才开发了这套系统工具，直接开放给大家用。重点是，我们自己沉淀了一套提示词系统：客户只要上传一张图片，就能自动生成 3 套提示词方案，直接提交就能跑出很不错的效果。
    >
