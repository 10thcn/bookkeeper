/**
 * stats-category.js — 按类别维度统计前端（7号）
 *
 * 分类占比条形列表 + Top N 排行
 * 提供图表数据给 9 号: [{label, value}]
 */

window.BookApp = window.BookApp || {};

window.BookApp.views["stats-category"] = {
  render(container) {
    // TODO: 7号实现 — 类别统计界面
    container.innerHTML = `
      <div class="card">
        <h2>🏷️ 分类统计</h2>
        <!-- TODO: 7号实现分类占比列表 -->
        <p style="color: #888;">分类统计待实现（7号）</p>
      </div>`;
  },
};