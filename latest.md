📊 开源日报 — 2026-10-29
共发现 5 个新项目（已自动过滤历史记录）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  xiaolai/the-craft-of-selfteaching
    ⭐ 18690 stars  |  🍴 17909 forks  |  💻 Jupyter Notebook  |  📅 2019-03-14
    🔗 https://github.com/xiaolai/the-craft-of-selfteaching
    📡 来源: trending-daily
    📝 One has no future if one couldn't teach themself.

    README 摘要:
    # the-craft-of-selfteaching
    
    > One has no future if one couldn't teach themself[1].
    
    # 自学是门手艺
    
    > 没有自学能力的人没有未来
    
    **作者：李笑来**
    
    特别感谢**霍炬**（@virushuo）、**洪强宁**（@hongqn) 两位良师诤友在此书写作过程中给予我的巨大帮助！
    
    ```python
    # pseudo-code of selfteaching in Python
    
    def teach_yourself(anything):
        while not create():
            learn()
            practice()
        return teach_yourself(another)
    
    teach_yourself(coding)
    ```
    
    请先行阅读 T-appendix.jupyter-installation-and-setup 以便在本地安装 Jupyterlab 而后就能用更好的体验阅读本书。
    
    有兴趣帮忙的朋友，请先行阅读 如何使用 Pull Request 为这本书校对。
    
    2019 年 3 月 23 日，新增 Markdown 版本：
    
    > https://github.com/selfteaching/the-craft-of-selfteaching/tree/master/markdown
    
    ### 目录
    
    > - 01.preface（**前言**）
    > - 02.proof-of-work（**如何证明你真的读过这本书？**）
    > - Part.1.A.better.teachyourself（**为什么一定要掌握自学能力？**）
    > - Part.1.B.why.start.from.learning.coding（**为什么把编程当作自学的入口？**）
    > - Part.1.C.must.learn.sth.only.by.reading（**只靠阅读习得新技能**）
    > - Part.1.D.preparation.for.reading（**开始阅读前的一些准备**）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#2  expo/skills
    ⭐ 3674 stars  |  🍴 234 forks  |  💻 Shell  |  📅 2025-11-30
    🔗 https://github.com/expo/skills
    📡 来源: trending-daily
    📝 A collection of AI agent skills for working with Expo projects and Expo Application Services

    README 摘要:
    Expo Skills
    
      
      
      
    
      Official AI agent skills from the Expo team for building, deploying, upgrading, and debugging Expo apps.
    
    ## How It Works
    
    Skills give AI agents focused Expo knowledge: when to use Expo APIs, how to structure common workflows, and which Expo, EAS, React Native, iOS, and Android constraints matter. Expo documentation, Expo CLI, and EAS CLI remain the source of truth; these skills help agents apply them correctly.
    
    ## Installation
    
    For Claude Code or Codex, install the plugin so updates are handled by the official plugin marketplace. For Cursor, OpenCode, and other AI coding agents, use the skills CLI.
    
    | Path | Best for |
    | --- | --- |
    | Plugin install | Claude Code or Codex, with updates handled by their official plugin marketplaces. |
    | Skills CLI | Cursor, OpenCode, GitHub Copilot, Windsurf, Gemini, Cline, AMP, Factory Droid, Antigravity, Kiro CLI, and other AI coding agents. |
    
    ### Skills CLI
    
    Install all Expo skills with the skills CLI:
    
    ```text
    npx skills@latest add expo/skills --skill '*'
    ```
    
    This selects every Expo skill without selecting every agent. The CLI will still ask where to install them; to target one agent directly, add `--agent `.
    
    For most agents, this is the only install command you need. Run it from the project root, then restart or refresh your agent session so it can discover the installed `SKILL.md` files.
    
    ### Claude Code Plugin
    
    Install from the official Claude Code plugin marketplace:
    
    ```text
    claude plugin install expo@claude-plugins-official
    ```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#3  Motionsites-AI/claude-skill
    ⭐ 971 stars  |  🍴 102 forks  |  💻 Python  |  📅 2026-10-26
    🔗 https://github.com/Motionsites-AI/claude-skill
    📡 来源: 🚀 5天300+星
    📝 Free Claude skill: make Claude build award-level, cinematic landing pages. By MotionSites.

    README 摘要:
    # MotionSites Web Builder: a free Claude skill
    
    **Make Claude build award-level, cinematic landing pages instead of average AI layouts.**
    
    AI-built websites tend to look the same for three reasons: a vague plan, no real media, and nobody looking at the result. This skill fixes all three. Claude studies the most-liked designs from MotionSites, picks real cinematic media, writes a precise build spec, builds the page, then **screenshots its own work and fixes it** until it clears a gallery-level bar.
    
    8 of the 40 example designs inside the skill, each shown next to the video it's built on. All 50+ videos are on the skill's media shelf.
    
    ## What's inside
    - **40 example prompts:** the most-liked free prompts on MotionSites, the designs people actually love. Claude reads the closest 2–3 for every brief to match their level of detail and taste.
    - **A media shelf:** 50+ cinematic hero videos, 30 transparent 3D cut-outs and 29 images, publicly hosted and shown on numbered contact sheets so Claude picks media by eye.
    - **55+ technique recipes** with working code, for example:
      - seamless video loops;
      - liquid glass;
      - word-by-word blur headlines;
      - mouse-scrubbed video;
      - spotlight reveals;
      - depth carousels;
      - scroll stories;
      - real 3D models (Three.js).
    - **Design taste rules with real numbers:** type scale, tracking, spacing, colour, motion timing and copy.
    - **A spec template:** the precise brief Claude writes before coding. That's where quality is decided.
    - **A look-and-fix loop:** a screenshot + QA script (broken assets, mobile overflow, fonts, video playback) and a scoring rubric.
    - **Prompt mode:** ask for a prompt instead of code, and get one tuned for Lovable, Bolt, v0, Cursor, Manus, Google AI Studio or Kimi.
    
    ## Install
    
    ### Claude.ai and Claude desktop
    1. Download **`motionsites-web-builder.zip`** from the latest release.
    2. In Claude, open **Customize → Skills → + → Create skill → Upload a skill**, choose the zip, and switch the skill on. (Code execution must be enabled in Settings → Capabilities.)
    
    ### Claude Code (plugin)
    ```
    /plugin marketplace add Motionsites-AI/claude-skill
    /plugin install motionsites-web-builder@motionsites
    ```
    No GitHub SSH key? Use `/plugin marketplace add https://github.com/Motionsites-AI/claude-skill.git` instead.
    
    ### Claude Code (manual)
    Copy `plugins/motionsites-web-builder/skills/motionsites-web-builder` into `~/.claude/skills/`.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4  ZiChuanLan/agent-purge
    ⭐ 833 stars  |  🍴 621 forks  |  💻 JavaScript  |  📅 2026-10-25
    🔗 https://github.com/ZiChuanLan/agent-purge
    📡 来源: 🚀 5天300+星
    🏷️ claude-code, codex, coding-agent, deepseek-harness, harness, omp, opencode, pi, system-prompt
    📝 One persona, many coding agents. Replace or inject system prompts across codex, claude, opencode, grok, omp, hermes, pi, zcode - with a local web console.

    README 摘要:
    # agent-purge
    
    一份系统提示词，喂给多个 coding agent。支持替换（replace）、只发人设（strict）、追加（append）、清空（off）四种模式，可热切换，全程可逆。
    
    ```
    agent-purge web          # 本地控制台 http://127.0.0.1:7788
    agent-purge codex        # 用当前 persona 启动 codex
    agent-purge pi --ask "…" # 一次性提问
    ```
    
    ## 它做什么
    
    每家 coding agent 读系统提示词的位置都不一样：有的认启动参数，有的认配置文件，有的只能靠插件改运行时对象。agent-purge 把这些入口统一成三件事：
    
    | 通道 | 机制 | 生效范围 |
    |---|---|---|
    | `install` | 写入该 harness 的托管配置块（Markdown / hooks / 插件） | 常驻，别人启动也生效 |
    | `shim` | 往 PATH 前置同名小壳，转发给 `agent-purge ` | 裸敲命令也接管 |
    | `slash` | 会话内 `/purge on\|off\|status` | 热切换，不动磁盘 |
    
    三层都写的是同一份 `personas/.md` 的正文。`--mode off` 或 Web 总开关关掉时，全部撤回到原样——不留残渣。
    
    ## 安装
    
    ```bash
    npm i -g agent-purge     # 或 npx agent-purge web
    ```
    
    要求 Node ≥ 20，零依赖。
    
    **用 magpie 网关？** 插件不在 npm 包里，在仓库的 `magpie-plugin/` 子目录——不要指向仓库根（根 `package.json` 是 CLI，只有 `bin`，magpie 会拒绝）：
    
    ```bash
    magpie plugin add /path/to/agent-purge/magpie-plugin
    ```
    
    首次使用先跑一次 `agent-purge web`（打开 http://127.0.0.1:7788 的控制台，先看/选一个人设；不想开界面就用 `agent-purge ls`），它会生成 `~/.agent-purge/personas/`；再跑 `node magpie-plugin/gen-personas.mjs` 生成 Persona 页的人设清单。
    
    详见下文「magpie 网关插件（可选）」。
    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#5  kargulstudio/calender-app-design
    ⭐ 791 stars  |  🍴 95 forks  |  💻 TypeScript  |  📅 2026-10-26
    🔗 https://github.com/kargulstudio/calender-app-design
    📡 来源: 🚀 5天300+星
    📝 无描述

    README 摘要:
    # Kargul Calender Design Prototype
    
    A design prototype of **Kargul Workspace**, a people-ops workspace built from the
    "Dashboard – calendar" Figma design. Live at https://calender-app-design.vercel.app.
    
    The **Time off** page (`/time-off`, the default route) reproduces the design
    pixel-for-pixel; every other page in the sidebar is built in the same visual
    language. Everything runs in the browser — there is no backend; data persists
    to `localStorage`.
    
    ## Stack
    
    - **Next.js 16** (App Router, Turbopack) · **React 19** · **TypeScript**
    - **Tailwind CSS v4** with design tokens mapped from the Figma variables
    - **shadcn/ui** (Radix primitives) themed to the design
    - **Zustand** for state (`persist` middleware → `localStorage`)
    - **next-themes** for dark mode, **Sonner** for toasts, **cmdk** for the command palette
    
    ## Getting started
    
    ```bash
    npm install
    npm run dev
    ```
    
    Open http://localhost:3000. To return to the exact design state, use
    **Settings → Data → Reset demo data** (or clear site data).
    
    ## What works
    
    - **Calendar** — week / day / month views; drag on empty space to create, drag
      events to move (across days), drag the bottom edge to resize; overlapping
      events lay out side by side; all-day lane with public holidays; live now-line;
      origin-aware details popover.
    - **Time off** — request dialog that counts working days (skips weekends and
      holidays) and shows the balance after the request; stats computed from your
      requests and allowance; requests table with search, filters, sorting, details,
      edit/cancel/delete, and a manager approve/decline preview.
    - **Shell** — workspace switcher, ⌘K search across pages/events/requests/
      documents/invoices, notifications, help menu, dark mode, account menu.
