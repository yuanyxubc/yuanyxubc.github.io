# Yuanyuan Xu 个人网站 — 交接文档 v2

**最后更新：2026年3月22日（本次 Claude 会话）**

---

## 一、本次会话做了什么

### 读取的资料文件夹
- `【个人资料】/` — 所有本科荣誉证书、奖状图片、媒体报道、专利申请文件
- `2019.5申请交大/` — 自荐信、研究计划、作品集材料
- `2019.5申请同济/` — 研究计划书、简历、上海日报专访 docx
- `2019.6 清华大学/` — 申请材料
- `2019.6申请交大ICCI 2020 Elite Camp/` — 面试 PPT、自我介绍
- `files/yuanyuan-website.tar.gz` — 原始网站文件（读取了交接文档和 index.html 全文）

### 实际修改内容（基于原始 index.html）

#### Publications — 新增 2 项专利（共 3 项）
- 智能保温杯实用新型专利（申请号 2019210545455）
- 刺猬花园治疗玩具外观专利（申请号 2019302922040）

#### Creative Works — 净效果：保留 2021 年后专业作品（共 7 件）
先加了 4 件本科作品，后来做减法全删了。最终只保留：
- Roller-Skating Knight (2025)、AR Game for Maison Margiela (2024)、The Struggle (2024)、Ganesha (2024)、Feather Columns (2023)、Immersive Automotive Space (2022)、The Story of the Ocean (2021)

#### Service & Awards — 从原 12 条精简为 12 条（替换了内容）
保留的奖项（按时间倒序）：
1. ACM CHI Outstanding Review × 2 (2025)
2. Rookie of the Year A Ranking · Game (2025)
3. Rookie of the Year A Ranking · VFX + 3D Animation (2024)
4. Graduate Commencement Speaker — Tongji (2023)
5. Full Scholarship ¥32,000 — Tongji (2021)
6. IOAF Bronze Award (2021)
7. Shanghai Outstanding Graduate Top 2% (2020)
8. Graduate Commencement Speaker — ECUST (2020)
9. Challenge Cup National First Prize 全国一等奖 — FPGA Blind Navigation (2019)
10. Chuang Qingchun National Gold Award 全国金奖 — SharePlay (2018)
11. National Scholarship Top 0.2% (2017)
12. Cheng Si-wei Honorary Principal's Scholarship Top 1% + Grand Prize Scholarship Rank #1 / 5 consecutive semesters (2016–2019)

#### Experience — 精简
- 删除了独立的 Teaching、Leadership 区块
- 把 TA 信息一句话并入本科学历描述
- SharePlay 在 Industry 里保留但大幅缩减为 2 句话
- 新增 SharePlay Co-founder 条目（精简版）

#### About — Press Coverage 区块删除
- 把上海日报头版链接一句话嵌入简介正文
- 删掉了 36kr、上海广播电视台的单独列举

#### CSS 修复
- 照片正圆问题：加了 `align-self: center`、`flex-shrink: 0`、`aspect-ratio: 1/1`、`min-width/min-height: 140px`、`display: block` on img

---

## 二、当前文件位置

```
files/
├── yuanyuan-website-updated/   ← 本次修改后的版本（最新）
│   ├── index.html              ← 主文件（1135行）
│   ├── photo.jpg               ← 照片（415×415 正方形，已可正圆显示）
│   └── HANDOFF.md              ← 本文档
└── yuanyuan-website.tar.gz     ← 原始版本存档（不要删）
```

---

## 三、已确认的事实（从文件中读出）

### 专利情况
| 类型 | 名称 | 申请号 | 状态 |
|------|------|--------|------|
| 发明专利（已授权） | FPGA-Based Vision Method for Blind Navigation | CN110070514B | 已列入网站 |
| 实用新型申请 | 智能保温杯 | 2019210545455 | 仅申请受理，非授权 |
| 外观设计申请 | 玩具（刺猬） | 2019302922040 | 仅申请受理，非授权 |

> ⚠️ 注意：后两项目前写的是"Patent Application"，如果后来已授权，需要改成正式授权号

### 上海日报专访
- 时间：2019年5月30日，头版头条
- 内容：Hedgehog Garden 自闭症玩具 + T-BIKE 老年健身车
- 原文链接：https://www.shine.cn/news/metro/1905305710/
- 已嵌入 About 简介正文

### 挑战杯澄清
- 网站原来写的是"National Gold Award"（含糊）
- 实际证书显示：**第十六届挑战杯全国大学生课外学术科技作品竞赛一等奖**（一等奖 = 最高奖，英文用 National First Prize）
- 另有：第十六届挑战杯**上海市特等奖**（已从网站删除，因为全国奖更重要）

### 创青春
- 创青春上海市大学生创业大赛 2018 **金奖**（上海市级）
- 创青春全国大学生创业大赛 2018 **全国金奖**（国家级，网站保留）
- 汇创青春上海市大学生文化创意作品大赛 2018 **一等奖/金奖**（已从网站删除）

### 成绩信息
- 华东理工大学：GPA 3.7/4.0，连续5学期专业第一，24门必修课满绩
- 同济大学：GPA 89.9/100，全额奖学金

---

## 四、下次 Claude 会话可继续做的事

### 待定内容（用户还没决定）
- [ ] 网站是否要加一个专门的 Research 页面介绍 Okanagan Water Knowledge Game 项目
- [ ] Creative Works 页面是否加作品缩略图/截图（目前纯文字卡片）
- [ ] 是否把 Hedgehog Garden、T-BIKE 这类有故事性的本科作品单独放一个"Earlier Work"折叠区块（而非完全删除）
- [ ] 照片更换（当前是侧边栏圆形头像）

### 部署（还未做）
- [ ] 部署到 GitHub Pages（README.md 里有详细步骤）
- [ ] 购买自定义域名（如 yuanyuanxu.com）
- [ ] PDF 版 CV 供下载（网站 CV 链接目前是占位符）

### 内容更新（待用户补充）
- [ ] HCII 2026 和 DiGRA 2026 的正式 DOI（in press 论文）
- [ ] 智能保温杯、刺猬玩具专利是否已授权（更新授权号）

---

## 五、设计变量速查（不变）

```css
:root {
  --bg: #FAFAF8;
  --sidebar-bg: #F0EFEB;
  --text: #1A1A18;
  --text-secondary: #5C5C58;
  --accent: #2D5A3D;
  --accent-light: #3A7A52;
  --border: #D8D7D3;
  --highlight: #C8956C;
  --sidebar-w: 340px;
}
```

字体：DM Serif Display（标题）/ Source Sans 3（正文）/ JetBrains Mono（日期）

---

## 六、联系方式（网站展示）

- Email: yuanyxu@student.ubc.ca
- Google Scholar: https://scholar.google.com/citations?user=2Sv5FNkAAAAJ
- LinkedIn: https://www.linkedin.com/in/xuyuanyuan/
