/**
 * api.js — API 请求封装（1号·组长）
 *
 * 提供 get / post / put / del 四个 fetch 封装。
 * 设置 USE_MOCK = true 可切换为本地 mock 模式。
 */

window.BookApp = window.BookApp || {};

const BASE_URL = "/api";

/** 设为 true 使用 mock 数据，false 请求真实 API */
const USE_MOCK = false;

/**
 * 通用请求封装
 * @param {"GET"|"POST"|"PUT"|"DELETE"} method
 * @param {string} path - 如 "/records"
 * @param {object|null} body - 请求体（GET/DELETE 忽略）
 * @returns {Promise<object>} JSON 响应
 */
async function request(method, path, body = null) {
  if (USE_MOCK) {
    return window.BookApp.mock.handle(method, path, body);
  }

  const opts = {
    method,
    headers: { "Content-Type": "application/json" },
  };
  if (body && (method === "POST" || method === "PUT")) {
    opts.body = JSON.stringify(body);
  }

  const res = await fetch(BASE_URL + path, opts);
  const data = await res.json();

  if (!res.ok) {
    const err = new Error(data.errors?.[0] || "请求失败");
    err.errors = data.errors || [];
    err.status = res.status;
    throw err;
  }

  return data;
}

/** GET 请求 */
function get(path) {
  return request("GET", path);
}

/** POST 请求 */
function post(path, body) {
  return request("POST", path, body);
}

/** PUT 请求 */
function put(path, body) {
  return request("PUT", path, body);
}

/** DELETE 请求 */
function del(path) {
  return request("DELETE", path);
}

// ── 挂载到全局 ──
window.BookApp.api = { get, post, put, del, USE_MOCK, setMock(m) { /* USE_MOCK = m */ } };