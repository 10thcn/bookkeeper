# static/vendor/ —— 目前为空

原计划把 Chart.js 下载到这里；实际改为在 `static/js/chart.js` 里手写 Canvas 实现，
不再依赖第三方图表库，所以本目录暂时不需要放文件。

不要往 `templates/index.html` 里加 Chart.js 的 `<script>` —— 会和 `window.Chart` 抢名字。
