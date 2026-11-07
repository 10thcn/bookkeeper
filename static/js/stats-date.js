/**
 * stats-date.js — 按时间维度统计前端（6号）
 *
 * 粒度切换（日/周/月）、日期范围
 * 三张汇总卡片（总收入/总支出/结余）+ 明细表
 */

window.BookApp = window.BookApp || {};

window.BookApp.views["stats-date"] = {
  render(container) {
    // TODO: 6号实现 — 时间维度统计界面
    container.innerHTML = `
      <div class="card">
        <h2>📊 时间统计</h2>
        <!-- TODO: 6号实现汇总卡片+明细表 -->
        <p style="color: #888;">时间统计待实现（6号）</p>
      </div>`;
  },
};