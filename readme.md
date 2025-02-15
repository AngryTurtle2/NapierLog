# 项目简介

本项目旨在科普 **纳皮尔对数表**，参与 B 站 UP 主 [漫士沉思录](https://space.bilibili.com/266765166) 发起的数学科普大会。

---

# 文件结构说明

1. **资料文件夹**  
   - [链接](./资料/链接.md)包含：阅读过的中文资料、外文资料、书籍，以及使用过的一些工具。

2. **视频文案文件夹**  
   - 包含：视频文案，以及文案中提取出的公式（使用 LaTeX 格式表示）。

3. **动画文件夹**  
   - `formula.py`：文案中的公式。  
   - 自定义动画的 Python 文件中写有一个动画效果。  
   - 动画文件包含所有 **Manim 动画**生成的代码。
   - 代码写的很不规范，中不中，西不西。哈哈哈哈哈。自己的项目瞎写着玩。有人看就多担待些。太丑了


4. **科大讯飞语音合成文件夹**  
   - 包含：科大讯飞长文本语音合成的代码实现（基于官方文档示例代码，已删除敏感信息如 appid 等）。

5. **数学 Python 文件夹**  
   - 包含：一个笔记和一个表格。  
     - **笔记**：Python 代码用于验证视频内容以及自动生成表格。  
     - **表格**：记录角度 89° 到 90° 之间，每分钟的角度变化对应的正弦值变化。

---

# 项目背景

- **兴趣与动机**  
  在了解到这个大会后，因为对主题感兴趣且有时间，希望通过参与获奖以获取奖金。翻阅了《数学珍宝历史文献精选》后，选择了 **纳皮尔对数表** 作为科普主题。  

- **资料查阅过程**  
  1. 从《奇妙对数定理的构造》摘抄部分内容，但发现理解困难。  
  2. 阅读了《奇妙对数定理的使用书》。  
  3. 查阅了 **17世纪数学网** 的英文译本（内容整理很好，但可能存在错误，影响了阅读理解）。  
  4. 最终通过阅读说明书和大量中外资料，逐渐理解了纳皮尔构造对数表的想法。

---

# 视频制作过程

## **步骤 1：搭建 Manim 环境并测试**
- 搭建并测试了 Manim 环境，确保动画生成正确。
- 阅读说明书和中外资料，尝试理解纳皮尔构造对数表的思路。

---

## **步骤 2：编写视频文案**
- 根据资料构思视频内容，编写视频文案或字幕。
- 文案重点：
  - 纳皮尔对数的定义。
  - 书中的几个例子。
  - 对数表每一行、每一列的含义。

---

## **步骤 3：编写动画代码**
- **初期尝试**：在代码中编写所有动画场景效果，但效率低下。  
- **优化方法**：  
  - 简化思路，将每个场景分为一个动画。  
  - 通过剪辑软件进行拼接、添加转场等操作，提高效率。  
- **动画效果**：  
  - 匀速运动的演示。  
  - 等比例衰减运动的演示。  
  - 公式的动态显示与消失。  
- **困难与取舍**：  
  - 由于时间和精力有限，部分复杂动画效果（如高亮、放大、箭头标注等）通过剪辑软件实现，而非编写代码。  

---

## **步骤 4：视频剪辑**
- **素材来源**：
  - 使用 OBS Studio 录制屏幕，如演示表格和截图讲解。  
  - 使用 WPS 打开表格，录制高亮效果。  
  - 在画图工具中框选重点内容，并录制屏幕。  
- **剪辑过程**：  
  - **初稿**：制作基础画面显示效果。  
  - **最终版**：配上语音、背景音乐等，完成剪辑。
  - 目前在犹豫是否上传剪映剪辑工程。初稿 大概240M，最终版502M
  - 也犹豫是否将初稿（1080P 26分 500M）终稿（1080P 25分 500M）上传到这里  
- **工具**：  
  - 剪映（够用，但 VIP 制度不友好，很多素材都需要VIP）。  

---

# 使用的 AI 工具

1. **ChatGPT**  
   - 编写文案后，利用 ChatGPT 提取文案中的数学公式，并直接输出为 LaTeX 格式，大大提升了效率。

2. **科大讯飞语音合成**  
   - 使用了科大讯飞长文本语音合成功能，以及输入法中的语音识别功能。

3. **其他 AI 工具**  
   - 包括豆包等多种工具，帮助提升工作效率。

**观点**：虽然 AI 工具可能存在不足，但不使用 AI 是更加愚蠢的选择。

---

# 制作过程中的感悟

1. **动画设计的挑战**  
   - 第一次使用 Manim，动画效果较为简单，主要是内容的出现与消失。  
   - 想实现更酷炫的效果（如运动轨迹的高亮显示、两种运动的对应关系等），但受限于时间和能力，只能通过剪辑软件部分实现。

2. **OBS 的灵活运用**  
   - 利用 OBS 录制屏幕，配合画图软件与表格演示，实现了部分直观的讲解效果。

3. **剪辑软件的优势**  
   - 虽然编写动画代码的效率较低，但通过剪映等剪辑软件的拼接与调整，简化了整体工作流程。

4. **对 AI 工具的依赖**  
   - ChatGPT 帮助提取公式和转换格式，极大减少了手动操作的工作量。  
   - 科大讯飞提供了语音合成的解决方案，进一步完善视频内容。

---

# 总结

- 本项目通过对 **纳皮尔对数表** 的科普，尝试用视频形式简要讲解纳皮尔对数的定义、书中几个例子，以及对数表的含义。  
- 最终成果虽有不足，但通过合理利用工具（如 Manim、OBS、剪映、AI 工具等），有效完成了视频制作任务。

---
##### 本文件我写了初稿后，chatgpt总结归纳整理重新排列了内容，并且生成了漂亮的格式