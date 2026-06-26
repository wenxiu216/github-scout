# NT Scout

每天自动扫描 GitHub，发现有价值的开源项目，写入 Google Doc，配合 AI 分析。

## 工作流程

```
GitHub Actions 每天 09:00 自动触发
    ↓
① 抓取 GitHub Trending（日榜 + 周榜）
② 搜索多方向关键词
③ 捕捉"火箭上升"项目（短期 star 暴涨）
    ↓
自动去重（过滤掉之前已收录的项目）
    ↓
取 Top 20 → 抓取 README → 写入 Google Doc
```

## 配置

### Secrets（仓库 Settings → Secrets → Actions）

| Secret | 说明 |
|---|---|
| `GH_PAT` | GitHub Personal Access Token（Public repo 只读权限） |
| `GOOGLE_APPS_SCRIPT_URL` | Google Apps Script Web App URL |

### Google Apps Script 设置

1. 打开目标 Google Doc → Extensions → Apps Script
2. 粘贴以下代码：

```javascript
function doPost(e) {
  var doc = DocumentApp.getActiveDocument();
  var body = doc.getBody();
  var text = e.postData.contents;
  body.insertParagraph(0, text);
  body.insertParagraph(0, "═".repeat(50));
  return ContentService.createTextOutput("ok");
}
```

3. Deploy → New deployment → Web app → Anyone → Deploy → 复制 URL
4. 存入 GitHub Secret `GOOGLE_APPS_SCRIPT_URL`

## 自定义

编辑 `scout.py` 中的 `SEARCH_GROUPS` 调整扫描方向，修改 `MAX_REPOS` / `MIN_STARS` / `SEARCH_DAYS` 调整数量和范围。

## 成本

$0/月（全部使用免费额度）
