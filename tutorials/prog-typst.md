---
title: 搭建 Typst 舒适写作环境（VSCode）
zhihu-url: https://zhuanlan.zhihu.com/p/642509853
zhihu-title-image: images/vscode/typst2.png
zhihu-tags: Visual Studio Code, Rust, 排版软件
---

# 搭建 Typst 舒适写作环境

Typst 是一个 Rust 编写的新一代排版软件，是当下 LaTeX 最有力的竞争者。

## 1. 主要扩展

在 VSCode 中的扩展商店里搜索并安装如下扩展

- Typst LSP
- Typst Preview

![typst](images/vscode/typst.png)

## 2. 辅助扩展

### 2.1. Unicode

Typst 写 LaTeX 公式时，有时不如 Markdown 那么方便，这时可以使用扩展

- Unicode Latex

![unicode](images/vscode/unicode.png)

通过敲击 `\`，即可完成相应的转义输入。

在 `settings.json` 中添加如下配置，使之生效

```json
{
    "unicode-latex.extensions": [
        "typst",
    ],
}
```

### 2.2. Emoji

除了 Unicode，Typst 中的 Emoji 也存在相似的问题，这里推荐安装扩展

- emoji-intellisense

通过敲击 `:`，即可完成相应的转义输入。

## 3. 效果

![typst2](images/vscode/typst2.png)
