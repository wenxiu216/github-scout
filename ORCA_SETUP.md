# 在 Orca 里跑通"开源日报自动分析"

这份文档讲：从零开始，把这个仓库 clone 下来、装好分析 skill、配好 Orca，
最终实现 **每天自动抓项目 → 一键 AI 分析** 的闭环。

## 整体闭环长这样

```
① github-scout（已部署的定时任务）
   每天北京 9:00 自动抓 20 个开源项目
   → 写进 Google Doc + 仓库的 latest.md
            ↓
② 你在 Orca 里点一下"分析日报"
   → Claude Code 读 latest.md
   → 用 noveltime-repo-scout skill 分析
   → 按优先级排出值得做的项目
            ↓
③ 你挑中的项目 → 在 Orca 里开 worktree 直接动手
```

①已经在 GitHub Actions 上自动跑了，不用管。
这份文档配的是 ②——让 Orca 能读日报、能用 skill 分析。

---

## 一、把仓库 clone 到本地

打开终端（Orca 里的 Terminal 也行），选一个你放代码的目录，执行：

```bash
git clone https://github.com/wenxiu216/github-scout.git
cd github-scout
```

clone 完你会看到这些文件：
- `latest.md` —— 最新一期日报（Orca 要读的就是这个）
- `reports/` —— 历史日报按日期归档
- `scout.py` —— 抓取脚本（GitHub Actions 自动跑，本地不用动）

---

## 二、安装分析 skill 到本地 Claude Code

skill 是一个 `.skill` 文件（本质是压缩包），要解压到 Claude Code 的 skills 目录。

假设 `noveltime-repo-scout.skill` 在你的下载文件夹：

```bash
# 创建 skills 目录（如果还没有）
mkdir -p ~/.claude/skills

# 解压进去
unzip ~/Downloads/noveltime-repo-scout.skill -d ~/.claude/skills/
```

装完确认一下：

```bash
ls ~/.claude/skills/noveltime-repo-scout/
# 应该看到 SKILL.md
```

看到 `SKILL.md` 就成功了。这个 skill 让 Claude Code 用"默认假设有用、
穷尽找连接、分档输出"的姿势分析项目，而不是一刀切判无关。

---

## 三、在 Orca 里添加项目

1. 打开 Orca
2. 左侧 **Projects** 区域点 **+**
3. 选刚才 clone 下来的 `github-scout` 文件夹
4. 添加后左侧会出现 `github-scout` 项目，下面有 `main 主工作树`

---

## 四、配一个"分析日报"快捷命令

这样以后一键就能触发分析，不用每次手敲。

1. Orca 里找到 **快捷命令**（设置 → 工作流 → 快捷命令，或界面上的快捷命令入口）
2. 点 **添加快捷命令**，按下面填：

| 字段 | 填什么 |
|---|---|
| **标签** | `分析日报` |
| **操作** | 选 **Agent 提示** |
| **Agent** | 选 **Claude** |
| **范围** | 选 **项目** → `github-scout` |
| **提示** | 见下方 |

**提示内容：**

```
读 latest.md，按 noveltime-repo-scout skill 的方法分析里面的项目，
挑出值得做的，按优先级排，说清每个为什么值得做、怎么用在 NovelTime。
```

3. 保存

---

## 五、日常怎么用

每天三步：

```bash
# 1. 进项目目录，拉最新日报
cd github-scout
git pull
```

```
# 2. 在 Orca 里点"分析日报"快捷命令
#    （或用顶部 ▷ 命令 / 左侧 任务 手动发那段提示）
```

```
# 3. Claude Code 给出排好序的分析
#    挑中想做的 → 在 Orca 开新 worktree 动手
```

### 想完全无人值守？

Orca 左侧有 **自动化** 功能。如果它支持定时任务，可以设成：
每天早上自动 `git pull` + 自动触发"分析日报"。
这样你打开 Orca 就能看到当天分析好的结果。

---

## 常见问题

**Q：在终端打那段中文指令，报 command not found？**
A：那段指令是给 Claude Code（AI agent）的，不是给 shell 的。
要通过 Orca 的"任务""命令"或"快捷命令"发，不能直接在终端打。

**Q：Claude Code 说找不到 skill？**
A：确认 skill 装对位置了：`ls ~/.claude/skills/noveltime-repo-scout/SKILL.md`
有这个文件才算装好。

**Q：latest.md 是空的或者很旧？**
A：先 `git pull` 拉最新。日报由 GitHub Actions 每天北京 9:00 自动更新，
如果当天还没到点，看到的就是前一天的。

**Q：想手动触发一次抓取，不等定时？**
A：去 GitHub 仓库 → Actions → Daily GitHub Scout → Run workflow。
跑完 `git pull` 就能拿到最新 latest.md。

---

## 文件清单

```
github-scout/
├── scout.py                          # 抓取脚本（Actions 自动跑）
├── latest.md                         # 最新日报 ← Orca 读这个
├── reports/                          # 历史日报归档
│   └── YYYY-MM-DD.md
├── history.json                      # 已分析项目记录（自动去重用）
├── requirements.txt                  # Python 依赖
├── .github/workflows/daily-scout.yml # 定时任务
├── README.md                         # 项目说明
└── ORCA_SETUP.md                     # 本文档

~/.claude/skills/noveltime-repo-scout/
└── SKILL.md                          # 分析 skill（单独安装）
```
