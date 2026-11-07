/**
 * record.js — 记账模块前端（4号）
 *
 * 表单：支出/收入切换、类别联动、金额、日期、备注
 * 功能：新增、编辑回填、删除确认
 */

window.BookApp = window.BookApp || {};

window.BookApp.views.record = {
  render(container) {
    // TODO: 4号实现 — 记账表单界面
    container.innerHTML = `
      <div class="card">
        <h2>📝 记一笔</h2>
        <!-- TODO: 4号实现表单 -->
        <p style="color: #888;">记账表单待实现（4号）</p>
      </div>`;
  },
};

/**
 * 编辑记录回填（被 5号列表调用）
 * @param {string} id
 */
window.BookApp.editRecord = function (id) {
  // TODO: 4号实现 — 加载记录数据并回填到表单
};