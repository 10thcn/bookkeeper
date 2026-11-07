/**
 * stats-amount.js — 按金额维度统计前端（8号）
 *
 * 统计卡片 + 金额分布区间 + 最大 5 笔记录列表
 * 提供 distribution 给 9 号（柱状图数据）
 */

window.BookApp = window.BookApp || {};

window.BookApp.views["stats-amount"] = {
  render(container) {
    // TODO: 8号实现 — 金额统计界面
    container.innerHTML = `
      <div class="card">
        <h2>💰 金额分析</h2>
        <!-- TODO: 8号实现统计卡片+分布区间 -->
        <p style="color: #888;">金额分析待实现（8号）</p>
      </div>`;
  },
};