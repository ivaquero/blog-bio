---
title: Markdown 基本语法
zhihu-url: https://zhuanlan.zhihu.com/p/139141155
zhihu-title-image: images/vscode/md-preview.png
zhihu-tags: Markdown, Visual Studio Code
---

# Markdown 基本语法

Markdown 是一种轻量级的标记语言（markup language），由 John Gruber（1973～）与 Aaron Swartz（1986～2013）于 2004 年创造，被网站用于编写说明文件（README）、技术文档或在论坛上发布信息。由于其语法简单，易于读写，且编写出的作品简洁美观，目前也被越来越多的人群用于日常写作、发布电子书甚至书写电子邮件。可以说，Markdown 是极简主义（minimalism）的代表作品。

简单说，Markdown 有如下优势：

- 语法简单，易于学习
- 简洁美观，可读性好
- 兼容 HTML/CSS，可添加丰富的样式
- 易于部署

## 1. 通用格式

### 1.1. 标题

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
```

**这是加粗的文字**

```markdown
*这是倾斜的文字*
```

*这是倾斜的文字*

```markdown
***这是斜体加粗的文字***
```

***这是斜体加粗的文字***

```markdown
~~这是加删除线的文字~~
```

~~这是加删除线的文字~~

### 1.3. 分割线

```markdown
---
---
```

---

### 1.4. 引用

- 在引用的文字前加>即可
- 引用也可嵌套，如>>，>>>

```markdown
> 这是引用的内容
```

> 这是引用的内容

## 2. 代码、公式

### 2.1. 行内代码

```markdown
这是`行内代码`。
```

这是`行内代码`。

### 2.2. 块级代码

```python
import functools


@functools.lru_cache
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    print(fibonacci(4))
```

### 2.3. 行内公式

```markdown
这是行内公式 $\Gamma(n) = (n-1)! \quad ∀ n ∈ \mathbb{N}$。
```

这是行内公式 $\Gamma(n) = (n-1)! \quad ∀ n ∈ \mathbb{N}$。

### 2.4. 块级公式

```markdown
$$
x = \frac{-b ± \sqrt{b^2 - 4ac}}{2a}
$$
```

$$
x = \frac{-b ± \sqrt{b^2 - 4ac}}{2a}
$$

$$
\int_{0}^{\infty} x^2 dx
$$

## 3. 列表

### 3.1. 无序列表

```markdown
- 列表内容
```

- 无序列表

### 3.2. 有序列表

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

## 4. 表格

```markdown
| 表头 | 表头 | 表头 |
|:----:|:----:|:----:|
| 内容 | 内容 | 内容 |
| 内容 | 内容 | 内容 |
```

| 表头 | 表头 | 表头 |
|:----:|:----:|:----:|
| 内容 | 内容 | 内容 |
| 内容 | 内容 | 内容 |

- 第二行分割表头和内容
- 文字默认居左
- `:-:`：表示文字居中
- `:--`：表示文字居左
- `--:`：表示文字居右

## 5. 链接

### 5.1. 跳转

```markdown
[跳转到通用格式](#1-通用格式)
```

[跳转到通用格式](#1-通用格式)

### 5.2. 图片

![图片 alt](图片地址 ''图片 title'')

- 图片 alt 就是显示在图片下面的文字，相当于对图片内容的解释
- 图片 title 是图片的标题，当鼠标移到图片上时显示的内容。title 可加可不加

```markdown
![知乎](https://pic2.zhimg.com/80/v2-48bbd284deacef0b5896427e660b2a51_1440w.png "知乎")
```

![知乎](https://pic2.zhimg.com/80/v2-48bbd284deacef0b5896427e660b2a51_1440w.png "知乎")

### 5.3. 超链接

```markdown
[百度](http:/baidu.com)
```

[百度](http:/baidu.com)

## 6. 扩展语法

基于 markdown-it。

### 6.1. 复选框

```markdown
- [ ]
- [x]
```

- [ ]
- [x]

### 6.2. 脚注

```markdown
2004 年，Wolfram 的研究助理 Matthew Cook 证明了初等 CA 中的规则 110 是通用的 [^1]，即，任何计算机可完成的任何计算都可由该 CA 完成。

[^1]: Cook, M. "Universality in Elementary Cellular Automata." Complex Systems 15, 1-40, 2004.
```

2004 年，Wolfram 的研究助理 Matthew Cook 证明了初等 CA 中的规则 110 是通用的 [^1]，即，任何计算机可完成的任何计算都可由该 CA 完成。

[^1]: Cook, M. "Universality in Elementary Cellular Automata." Complex Systems 15, 1-40, 2004.

### 6.3. 高亮

```markdown
==高亮==
```

==高亮==

### 6.4. 上、下标

```markdown
OH^-^
KBrO~3~
```

OH^-^
KBrO~3~

### 6.5. 表情

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

### 6.6. 文本绘图

Markdown 支持文本绘图，目前比较流行的有 Mermaid.js 和 PlantUML。其中，Mermaid.js 是完全 Markdown 风格的语言，可与 Markdown 文档做到无缝衔接。

作为极简主义的代表作之一，Markdown 未来的生态会越来越丰富。

## 7. 对接前端

### 7.1. HTML

### 7.2. JavaScript

- 示意图
  - [mermaid.js](https://mermaid.js.org/intro/)
- 幻灯片
  - [slidev.js](https://sli.dev/resources/theme-gallery)
  - [reveal.js](https://revealjs.com/)
