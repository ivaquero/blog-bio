---
title: Markdown 基本语法
zhihu-url: https://zhuanlan.zhihu.com/p/139141155
zhihu-title-image: images/vscode/md-preview.png
zhihu-tags: Markdown, Visual Studio Code
---

# Markdown 基本语法

Markdown 是一种轻量级的标记语言（markup language），由 John Gruber（1973 ∼）与 Aaron Swartz（1986 ∼ 2013）于 2004 年创造，被网站用于编写说明文件（readme）、技术文档或在论坛上发布信息。由于其语法简单，易于读写，且编写出的作品简洁美观，目前也被越来越多的人群用于日常写作、发布电子书甚至书写电子邮件。可说，Markdown 是极简主义（minimalism）的代表作品。

简单说，Markdown 有如下优势：

- 语法简单，易于学习
- 简洁美观，易于阅读
- 兼容 HTML，可添加丰富的样式
- 跨平台
- 越来越多的网站支持

## 1. 通用格式

### 1.1. 标题

- 在想要设置为标题的文字前面加#来表示
- 1 个 `#` 是一级标题，2 个 `#` 是二级标题，以此类推。一般最多支持五级标题。

```markdown
# 这是一级标题

## 这是二级标题

### 这是三级标题

#### 这是四级标题

##### 这是五级标题
```

### 1.2. 字体

```markdown
**这是加粗的文字**
_这是倾斜的文字_
**_这是斜体加粗的文字_**
~~这是加删除线的文字~~
```

**这是加粗的文字**
_这是倾斜的文字_
**_这是斜体加粗的文字_**
~~这是加删除线的文字~~

### 1.3. 引用

- 在引用的文字前加>即可
- 引用也可嵌套，如>>，>>>

```markdown
> 这是引用的内容
```

> 这是引用的内容

### 1.4. 分割线

- 三个或三个以上的 `-` 或 `*`

```markdown
---
---

---

---
```

---

## 2. 外部链接

### 2.1. 图片

- ![图片 alt](图片地址 ''图片 title'')

> 图片 alt 就是显示在图片下面的文字，相当于对图片内容的解释
>
> 图片 title 是图片的标题，当鼠标移到图片上时显示的内容。title 可加可不加

```markdown
![知乎](https://pic2.zhimg.com/80/v2-48bbd284deacef0b5896427e660b2a51_1440w.png "知乎")
```

![知乎](https://pic2.zhimg.com/80/v2-48bbd284deacef0b5896427e660b2a51_1440w.png "知乎")

### 2.2. 超链接

```markdown
[百度](http:/baidu.com)
```

[百度](http:/baidu.com)

### 2.3. html

- Markdown 本身语法不支持链接在新页面中打开，若想要在新页面中打开的话可用 html 语言的 a 标签代替

```markdown
<a href = "https:/www.jianshu.com/u/1f5ac0cf6a8b" target = "_blank">知乎</a>
```

<a href = "https://zhuanlan.zhihu.com/p/139140492" target = "_blank">知乎</a>

## 3. 表单

### 3.1. 无序列表

- 无序列表用 `-` 、 `+` 、 `*` 任何一种都可

```markdown
- 列表内容

* 列表内容

- 列表内容
```

- 列表内容

### 3.2. 有序列表

- 数字加点

```markdown
1. 列表内容
2. 列表内容
3. 列表内容
```

1. 列表内容
2. 列表内容
3. 列表内容

### 3.3. 列表嵌套

- 上一级和下一级之间敲**3 个空格**即可

```markdown
- 一级无序列表内容
  - 二级无序列表内容
  - 三级无序列表内容
  - 四级无序列表内容
```

- 一级无序列表内容
  - 二级无序列表内容
  - 三级无序列表内容
    - 四级无序列表内容

### 3.4. 表格

```markdown
| 表头  | 表头  | 表头  |
| :---: | :---: | :---: |
| 内容  | 内容  | 内容  |
| 内容  | 内容  | 内容  |
```

| 表头  | 表头  | 表头  |
| :---: | :---: | :---: |
| 内容  | 内容  | 内容  |
| 内容  | 内容  | 内容  |

- 第二行分割表头和内容
- 有一个就行，为了对齐，多加了几个
- 文字默认居左
- -两边加：表示文字居中
- -右边加：表示文字居右

## 4. 代码、公式

### 4.1. 代码块

- 单行代码：代码之间分别用一个\`包起来

```markdown
`代码内容`
```

`代码内容`

- 代码块：代码之间分别用\ `\` \ `包起来，且两边的\` \ `\` 单独占一行

```markdown
代码
```

```python
labels = []
markers = ['o', 'd', 'r']
colors = ['red', 'blue', 'green']

for i in range(2):
  time = mix.Time[0+i*6, 6+i*6]
  normal = mix.Normal[0+i*6, 6+i*6]
  ldir = mix.LDIR[0+i*6, 6+i*6]

  ax.plot(time, normal, label=labels[i], marker=markers[i], color=colors[i])
  ax.plot(time, ldir, label=rlabels[i], marker=markers[i], color=colors[i], linestyle='.-')
```

### 4.2. 公式

- 行内

```markdown
$Γ(n) = (n-1)! \enspace \forall n \in \mathbb N$
```

$Γ(n) = (n-1)! \enspace ∀ n ∈ ℕ$

- 块级

```markdown
$$
x = \frac{-b ± \sqrt{b^2 - 4ac}}{2a}
$$
```

$$ x = \frac{-b ± \sqrt{b^2 - 4ac}}{2a} $$

## 5. 扩展语法

基于 markdown-it。

### 5.1. 上、下标

```markdown
OH^-^
KBrO~3~
```

OH^-^
KBrO~3~

### 5.2. 复选框

```markdown
- [ ]
- [x]
```

- [ ]
- [x]

### 5.3. 高亮

```markdown
==高亮==
```

==高亮==

### 5.4. 表情

目前，大多数的 Markdown 编辑器都支持了 emoji，其基本格式为，`:` 英文单词 `:`，如

```markdown
:sunflower:
:cat:
:bike:
:icecream:
:running:
:ski:
```

🌻
🐱
🚲
🍦
🏃
🎿

### 5.5. 文本绘图

Markdown 支持文本绘图，目前比较流行的有 Mermaid.js 和 PlantUML。其中，Mermaid.js 是完全 Markdown 风格的语言，可与 Markdown 文档做到无缝衔接。

作为极简主义的代表作之一，Markdown 未来的生态会越来越丰富。
