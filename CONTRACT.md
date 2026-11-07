# CONTRACT.md — 数据结构 · API 表 · 文件归属

> 组长（1号）14:20 提交本文件，后续如有变更需全组确认。

---

## 一、核心数据结构

### Record（记账记录）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | string (UUID4) | ✅ | 唯一标识，由 `models.new_record()` 自动生成 |
| `type` | `"expense"` \| `"income"` | ✅ | 支出或收入 |
| `category` | string (枚举) | ✅ | 见下方分类枚举 |
| `amount` | number (float, 2 位小数) | ✅ | 金额，>0 |
| `date` | string (ISO 8601: `YYYY-MM-DD`) | ✅ | 日期 |
| `note` | string (≤100 字) | ❌ | 备注，可为空字符串 |
| `created_at` | string (ISO 8601 datetime) | ✅ | 创建时间，由 `models.new_record()` 自动生成 |

### 分类枚举

**支出 (expense)**：饮食、交通、购物、娱乐、学习、居住、医疗、其他

**收入 (income)**：工资、兼职、理财、其他

### 存储格式

- 文件：`data/records.json`
- 编码：UTF-8
- 内容：`Record[]` 数组
- 读写：`storage.py` 统一管理

---

## 二、API 接口表

所有响应的 Content-Type 为 `application/json`。
错误响应统一格式：`{"ok": false, "errors": ["错误描述1", ...]}`

| 方法 | 路径 | 说明 | 归属 | 请求体 / Query |
|------|------|------|------|----------------|
| `POST` | `/api/records` | 新增记录 | 4号 | `{type, category, amount, date, note?}` → 201 |
| `GET` | `/api/records` | 分页查询 | 5号 | `?type=&category=&date_from=&date_to=&q=&sort=&page=&page_size=` |
| `GET` | `/api/records/<id>` | 单条详情 | 5号 | — |
| `PUT` | `/api/records/<id>` | 更新记录 | 4号 | 部分或全部字段 |
| `DELETE` | `/api/records/<id>` | 删除记录 | 4号 | — |
| `GET` | `/api/stats/by-date` | 时间维度统计 | 6号 | `?granularity=day\|week\|month&from=&to=` |
| `GET` | `/api/stats/by-category` | 类别维度统计 | 7号 | `?type=expense\|income&from=&to=` |
| `GET` | `/api/stats/by-amount` | 金额维度统计 | 8号 | `?from=&to=` |
| `GET` | `/api/export` | 导出数据 | 11号 | `?format=json\|csv` |
| `POST` | `/api/import` | 导入数据 | 11号 | multipart/form-data (file) |

---

## 三、前端 JS 模块约定

### 全局命名空间

```js
window.BookApp = {
  views: {},     // 各模块在此注册 render(container) 函数
  api: {},       // api.js 提供的 get/post/put/del
  mock: {},      // mock.js 假数据
  state: {},     // 全局共享状态
}
```

### 视图注册（app.js 调度）

每个功能 JS 文件在末尾自注册：
```js
window.BookApp.views.record = { render(container) { /* ... */ } };
```

### 跨模块约定

| 约定 | 说明 |
|------|------|
| `BookApp.editRecord(id)` | 4号暴露：列表页点"编辑"时调用，回填表单 |
| `BookApp.refreshCurrentView()` | 各模块调用：刷新当前视图 |
| `BookApp.showToast(msg, type)` | 10号提供：轻提示 |

---

## 四、文件归属清单

| 编号 | 成员 | 文件 |
|------|------|------|
| **1** | **罗炜 (组长)** | `app.py`、`static/js/app.js`、`static/js/api.js`、`static/js/mock.js`、`CONTRACT.md`、`README.md`、`.github/` |
| 2 | 待定 | `storage.py`、`tests/test_storage.py` |
| 3 | 待定 | `models.py`、`tests/test_models.py` |
| 4 | 待定 | `routes/records.py`、`static/js/record.js` |
| 5 | 待定 | `routes/query.py`、`static/js/list.js` |
| 6 | 待定 | `stats/date.py`、`static/js/stats-date.js` |
| 7 | 待定 | `stats/category.py`、`static/js/stats-category.js` |
| 8 | 待定 | `stats/amount.py`、`static/js/stats-amount.js` |
| 9 | 待定 | `static/js/chart.js`、`static/vendor/` |
| 10 | 待定 | `templates/index.html`、`static/css/style.css` |
| 11 | 待定 | `seed.py`、`routes/io.py`、`static/js/io.js` |

---

## 五、依赖顺序 & 时间节点

```
2、3 ─┬─→ 4 ─┬─→ 6 ──→ 9
      │      ├─→ 7 ──→ 9
      │      ├─→ 8 ──→ 9
      │      ├─→ 5
      │      └─→ 11
10 ───┴──→ (先交挂载点，14:45 前)
```

- 14:20 — 组长提交目录结构 + CONTRACT.md + 全部空壳文件 + 每人一条 Issue
- 14:45 — 2、3、10 号交货
- 15:00 — 11 号 seed.py
- 16:10 — 9 号接上真实数据
- 16:55 — 打 tag v1.0.0 发 Release
- 17:00 — 提交链接 + 演示