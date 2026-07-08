# Yuanyuan Xu 个人网站 — 交接文档

**最后更新：2026年3月21日**

---

## 一、项目概况

这是一个学术个人网站，目标受众是学术同行、合作者和求职（教职/博后）。

- **技术方案**：纯HTML单文件 + 1张照片，无框架依赖
- **设计风格**：左右两栏（参考 xxuxian.github.io），左栏固定导航，右栏多页切换
- **参考网站**：Xian Xu (xxuxian.github.io)、Zhuying Li (zhuyingli.info)、Hua Shen (hua-shen.org)

---

## 二、文件清单

```
yuanyuan-website/
├── index.html      ← 网站主文件（所有内容、样式、脚本都在这一个文件里）
├── photo.jpg       ← 个人照片（侧边栏头像）
└── README.md       ← 本文档
```

---

## 三、部署方法（GitHub Pages）

### 步骤：
1. 在 GitHub 创建一个新 repo，命名为 `你的用户名.github.io`
2. 把 `index.html` 和 `photo.jpg` 上传到 repo 根目录
3. 去 Settings → Pages → Source 选 `main` branch
4. 等几分钟，访问 `https://你的用户名.github.io` 即可

### 自定义域名（可选）：
- 购买域名后，在 repo 根目录创建 `CNAME` 文件，写入你的域名
- 在域名DNS设置里添加 CNAME 记录指向 `你的用户名.github.io`

---

## 四、如何更新内容

网站是纯HTML，用任何文本编辑器（VS Code、Sublime Text、甚至记事本）打开 `index.html` 就能改。

### 常见更新操作：

#### 添加新论文
找到 `<!-- ──── PUBLICATIONS ──── -->` 部分，复制一个 `pub-item` 块，修改内容：

```html
<div class="pub-item">
  <div class="pub-title">论文标题</div>
  <div class="pub-authors"><span class="me">Y. Xu*</span>, 其他作者</div>
  <div class="pub-venue">会议/期刊名 <span class="pub-year">· 年份</span></div>
  <div class="pub-doi"><a href="https://doi.org/xxxxx" target="_blank">doi.org/xxxxx</a></div>
  <div class="pub-tags"><span class="pub-tag journal">Journal</span></div>
</div>
```

标签类型：
- `<span class="pub-tag journal">Journal</span>` — 绿色，期刊
- `<span class="pub-tag conf">Conference</span>` — 紫色，会议
- `<span class="pub-tag chapter">Book Chapter</span>` — 棕色，书章
- `<span class="pub-tag inpress">In Press</span>` — 橙色，待发表

#### 添加新闻
找到 `<ul class="news-list">`，在最上面加一条：

```html
<li>
  <span class="news-date">月 年</span>
  <span class="news-text">新闻内容 <span class="badge green">Upcoming</span></span>
</li>
```

Badge类型：
- `<span class="badge green">Upcoming</span>` — 绿色
- `<span class="badge">In Press</span>` — 棕色

#### 添加创意作品
找到 `<div class="creative-grid">`，添加一个卡片：

```html
<div class="creative-card">
  <div class="year">年份</div>
  <div class="title">作品名</div>
  <div class="desc">描述</div>
  <div class="award">奖项名（可选）</div>
</div>
```

#### 添加经历
找到对应的 `<h4>` 小标题下面，添加：

```html
<div class="timeline-item">
  <div class="period">时间段</div>
  <div class="role">职位/学位</div>
  <div class="org">机构</div>
  <div class="details">详细描述</div>
</div>
```

#### 添加奖项
```html
<div class="award-item">
  <span class="year">年份</span>
  <span class="name">奖项名</span>
  <span class="source"> — 颁发机构</span>
</div>
```

#### 添加审稿服务
```html
<li><strong>缩写</strong> — 全称</li>
```

#### 换照片
直接替换 `photo.jpg` 文件，保持同名即可。建议正方形或接近正方形的照片（会被圆形裁剪）。

---

## 五、网站包含的全部内容

### About 页
- 个人简介（研究方向、背景、heritage叙事）
- 研究关键词标签（7个）
- News 动态（7条）

### Publications 页
- Journal Articles: 8篇（含 Sustainability 2026, WEVJ, Computing & AI ×2, J. Univ. Shanghai, Literature Life, Art & Technology）
- Conference Papers & Book Chapters: 7篇（含 HCII LNCS ×3, HCII accepted, FFIT, AEHSSR）
- Forthcoming (In Press): 6篇（HCII 2026 ×3, DiGRA 2026 ×3）
- Patent: 1项（FPGA Blind Navigation）
- 所有有DOI的论文都加了可点击链接

### Creative Works 页
- 创意作品卡片: 7个（Roller-Skating Knight, Maison Margiela AR, The Struggle, Ganesha, Feather Columns, VW Immersive Space, Story of the Ocean）
- Presentations: 4条（SIGGRAPH 2025, HCII 2024, 同济毕业演讲, 华理毕业演讲）

### Experience 页
- Education: 3条（UBC PhD, 同济硕士含GPA和课程, 华理本科含GPA和课程）
- Professional Training: 1条（Think Tank Training Centre）
- Industry: 2条（SAP Labs, Siemens）
- Research Collaboration: 1条（CMU联合项目）
- Current Research Roles: 1条（UBC RA, Beaver Land Project）

### Service & Awards 页
- Academic Reviewing: 13个（CHI含Outstanding Review, DIS, C&C, UIST, ETRA, IMX, CUI, Auto UI, ISMAR, EuroVis, CAADRIA含Committee Member, IJHCI, ITA）
- Awards: 12条
- Research Funding: 5条（含项目名称）

---

## 六、数据来源

网站内容来自以下材料的完整合并：

1. `Yuan_s_Resume_Template.pdf` — 早期简历，包含GPA、课程、ITA审稿等
2. `SSHRC_Yuany_CV_1_.docx` — SSHRC格式CV，含creative outputs和applicant statement
3. `Yuany_SSHRC_cv.pdf` — 另一版SSHRC CV
4. `SSHRC_CV_YUANY.pdf` — SSHRC正式CV含funded research详情
5. `SSHRC_YUANY.pdf` — CGRSD完整申请（含proposal、diversity statement、funded research）
6. `SSHRC-CV-1.pdf` — SSHRC CV格式说明
7. `SSHRC_proposal_Yuany__two_pages_.docx` — 研究提案
8. `Yuany_SSHRC_proposal.pdf` — 研究提案PDF版
9. `CV2024_Core_1.pdf` — Emily Murphy教授的CV（格式参考）
10. 聊天中补充的新接收论文（Sustainability, HCII 2026 ×3, DiGRA 2026 ×3）
11. 聊天中补充的IJHCI审稿人身份
12. DiGRA 2026会议截图（Doctoral Consortium Jun 14, Education Session Jun 16）

---

## 七、待办 / 后续可以做的事

- [ ] 部署到 GitHub Pages
- [ ] 购买自定义域名（如 yuanyuanxu.com）
- [ ] 准备一份PDF版CV供下载（网站CV链接目前是占位符）
- [ ] 论文有新DOI后更新链接（HCII 2026和DiGRA 2026的in press论文）
- [ ] 可以考虑加一个 Research 页面专门介绍博士研究项目（Okanagan Water Knowledge Game）
- [ ] 如果想要更方便的更新系统，可以迁移到 Hugo + Markdown（内容存JSON/Markdown，不用改HTML）
- [ ] 添加 Google Analytics 跟踪访问量
- [ ] 创意作品页可以加缩略图/截图（目前是纯文字卡片）

---

## 八、联系方式（网站上展示的）

- Email: yuanyxu@student.ubc.ca
- Google Scholar: https://scholar.google.com/citations?user=2Sv5FNkAAAAJ
- LinkedIn: https://www.linkedin.com/in/xuyuanyuan/

---

## 九、设计变量速查

如果想改颜色或字体，修改 `index.html` 顶部的 CSS 变量：

```css
:root {
  --bg: #FAFAF8;           /* 主背景色 */
  --sidebar-bg: #F0EFEB;   /* 侧边栏背景 */
  --text: #1A1A18;          /* 主文字色 */
  --text-secondary: #5C5C58;/* 次要文字色 */
  --accent: #2D5A3D;        /* 主题绿色 */
  --accent-light: #3A7A52;  /* 浅绿色 */
  --highlight: #C8956C;     /* 高亮棕色（badge用） */
  --border: #D8D7D3;        /* 边框色 */
  --sidebar-w: 340px;       /* 侧边栏宽度 */
}
```

字体：
- 标题：DM Serif Display（衬线）
- 正文：Source Sans 3（无衬线）
- 代码/日期：JetBrains Mono（等宽）

所有字体通过 Google Fonts CDN 加载，无需本地安装。
