---
title: 说说
---
<!-- <script src="//cdn1.tianli0.top/npm/leancloud-storage@4.13.2/dist/av-min.js"></script>
<div id="lyxTalk"></div>

<script src="/js/lyxTalk.js"></script>
<link rel="stylesheet" src="/css/lyxTalk.css">
<script>
  const { Query, User } = AV;
document.title = '说说 | Zhpxfyの小窝'; 
lyxTalk.init("ZjGE8CHHQDqhfpwm77Ji5w9t-MdYXbMMI",
  "76UQuBqAL2znnhxs8F7hevN0",
  'https://zjge8chh.api.lncldglobal.com',
   1919810)
</script> -->
<!-- 存放哔哔的容器 -->
<div id="bbtalk"></div>
<!-- 引用 bbtalk -->
<script data-pjax="" src="/js/bbtalk.js">
  </script>
<script>
  function doSpeaks() {
  document.title = '说说 | Zhpxfyの小窝'; 
bbtalk.init({
  appId: "ZjGE8CHHQDqhfpwm77Ji5w9t-MdYXbMMI",
  appKey: "76UQuBqAL2znnhxs8F7hevN0",
  serverURLs: 'https://zjge8chh.api.lncldglobal.com',
  pageSize:1919810
})
}
  document.addEventListener('DOMContentLoaded', (e) => {
    doSpeaks();
})
document.addEventListener('pjax:complete', (e) => {
    doSpeaks();
})
  
</script>