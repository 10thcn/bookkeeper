/**
 * mock.js — 假数据 & Mock 处理器（1号·组长）
 *
 * 提供 20 条覆盖所有类别的模拟记录，供前端开发调试使用。
 */

window.BookApp = window.BookApp || {};

/** 20 条假数据 */
const MOCK_RECORDS = [
  { id: "m001", type: "expense", category: "饮食", amount: 15.00, date: "2026-11-07", note: "午餐外卖" },
  { id: "m002", type: "expense", category: "交通", amount: 6.00, date: "2026-11-07", note: "地铁通勤" },
  { id: "m003", type: "expense", category: "购物", amount: 89.90, date: "2026-11-06", note: "网购T恤" },
  { id: "m004", type: "expense", category: "娱乐", amount: 35.00, date: "2026-11-05", note: "电影票" },
  { id: "m005", type: "expense", category: "学习", amount: 49.00, date: "2026-11-04", note: "二手教材" },
  { id: "m006", type: "expense", category: "居住", amount: 1200.00, date: "2026-11-01", note: "11月房租" },
  { id: "m007", type: "expense", category: "医疗", amount: 68.50, date: "2026-10-28", note: "感冒药" },
  { id: "m008", type: "expense", category: "其他", amount: 20.00, date: "2026-10-25", note: "打印资料" },
  { id: "m009", type: "expense", category: "饮食", amount: 28.00, date: "2026-10-22", note: "聚餐AA" },
  { id: "m010", type: "expense", category: "交通", amount: 12.00, date: "2026-10-20", note: "打车" },
  { id: "m011", type: "expense", category: "饮食", amount: 9.50, date: "2026-10-15", note: "早餐" },
  { id: "m012", type: "expense", category: "购物", amount: 256.00, date: "2026-10-10", note: "蓝牙耳机" },
  { id: "m013", type: "income", category: "工资", amount: 3000.00, date: "2026-11-05", note: "11月实习工资" },
  { id: "m014", type: "income", category: "兼职", amount: 500.00, date: "2026-10-28", note: "家教" },
  { id: "m015", type: "income", category: "理财", amount: 32.50, date: "2026-10-20", note: "基金收益" },
  { id: "m016", type: "income", category: "其他", amount: 200.00, date: "2026-10-15", note: "红包" },
  { id: "m017", type: "income", category: "兼职", amount: 800.00, date: "2026-09-30", note: "翻译兼职" },
  { id: "m018", type: "income", category: "工资", amount: 3000.00, date: "2026-10-05", note: "10月实习工资" },
  { id: "m019", type: "expense", category: "娱乐", amount: 128.00, date: "2026-09-25", note: "游戏充值" },
  { id: "m020", type: "expense", category: "学习", amount: 199.00, date: "2026-09-18", note: "网课会员" },
];

/**
 * Mock 请求处理器
 * 模拟后端 API 行为，返回符合约定的 JSON
 */
function handleMock(method, path, body) {
  return new Promise((resolve) => {
    setTimeout(() => {
      // GET /api/records
      if (method === "GET" && path.startsWith("/records") && !path.includes("/records/")) {
        resolve({ items: MOCK_RECORDS, total: MOCK_RECORDS.length, page: 1, pages: 1 });
        return;
      }

      // GET /api/records/:id
      if (method === "GET" && path.startsWith("/records/")) {
        const id = path.split("/").pop();
        const rec = MOCK_RECORDS.find((r) => r.id === id);
        resolve(rec || { ok: false, errors: ["记录不存在"] });
        return;
      }

      // POST /api/records
      if (method === "POST" && path === "/records") {
        const rec = { ...body, id: "m" + Date.now(), created_at: new Date().toISOString() };
        resolve({ ok: true, record: rec });
        return;
      }

      // PUT /api/records/:id
      if (method === "PUT" && path.startsWith("/records/")) {
        resolve({ ok: true, record: { ...body, id: path.split("/").pop() } });
        return;
      }

      // DELETE /api/records/:id
      if (method === "DELETE" && path.startsWith("/records/")) {
        resolve({ ok: true });
        return;
      }

      // GET /api/stats/*
      if (method === "GET" && path.startsWith("/stats")) {
        resolve({ ok: true, data: [] });
        return;
      }

      // GET /api/export
      if (method === "GET" && path === "/export") {
        resolve({ ok: true, data: MOCK_RECORDS });
        return;
      }

      resolve({ ok: false, errors: ["Mock: 未实现的端点 " + path] });
    }, 200);
  });
}

window.BookApp.mock = {
  records: MOCK_RECORDS,
  handle: handleMock,
};