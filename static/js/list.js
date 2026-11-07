/**
 * list.js — 查看模块前端（5号）
 *
 * 默认显示最近 10 笔；筛选栏（类型/类别/日期范围/关键字）
 * 表格列：日期、类别、金额（红/绿）、备注、操作
 * 分页或"加载更多"、空状态、删除二次确认
 */

window.BookApp = window.BookApp || {};

window.BookApp.views.list = {
  render(container) {
    // TODO: 5号实现 — 记录列表界面
    container.innerHTML = `
      <div class="card">
        <h2>📋 收支明细</h2>
        <!-- TODO: 5号实现筛选栏+表格 -->
        <p style="color: #888;">明细列表待实现（5号）</p>
      </div>`;
  },
};