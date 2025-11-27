---
title: 搭建 Typst 舒适写作环境（VSCode）
zhihu-url: https://zhuanlan.zhihu.com/p/642509853
zhihu-title-image: images/vscode/typst.png
zhihu-tags: Visual Studio Code, Rust, 排版软件
---

# 搭建 Typst 舒适写作环境

Typst 是一个 Rust 编写的新一代排版软件，是当下 LaTeX 最有力的竞争者。其环境配置非常简单。

## 1. 安装

### 1.1. 软件

对 macOS/Linux 用户，可以使用 Homebrew 安装

```sh
brew install typst
```

Windows 用户，可以使用 Scoop 安装

```sh
scoop install typst git
```

> Scoop 安装采用如下命令
>
> ```powershell
> irm get.scoop.sh -outfile 'install.ps1'
> .\install.ps1 -ScoopDir 'C:\Scoop' -NoProxy
> ```

### 1.2. 第三方库

为保证正常编译，请参考 typst-packages 上的说明，在如下路径下克隆 typst-packages 仓库，即先使用 `cd` 命令到对应路径，然后克隆

- Linux：
  - `$XDG_DATA_HOME`
  - `~/.local/share`
- macOS: `~/Library/Application Support`
- Windows：`%APPDATA%`

```sh
cd [above-path]
git clone --depth 1 --branch main https://github.com/typst/packages typst
```

## 2. 主要扩展

在 VSCode 中的扩展商店里搜索并安装扩展 Tinymist

![typst](images/vscode/vscode-typst.png)

## 3. 辅助扩展

### 3.1. Unicode

Typst 写 LaTeX 公式时，有时不如 Markdown 那么方便，这时可以使用扩展

- Unicode Math Input

![unicode](images/vscode/vscode-unicode.png)

### 3.2. Emoji

除了 Unicode，Typst 中的 Emoji 也存在相似的问题，同样通过上述扩展

通过敲击 `\:`，即可完成相应的转义输入。

## 4. 效果

![typst-unicode](images/vscode/typst.png)

## 5. 格式化

Typst Preview 的作者开发了一个 Typst 十分易用的格式化器，[typstyle](https://github.com/Enter-tainer/typstyle)，其在 Tinymist Typst 有集成接口。

对 macOS/Linux 用户，可以使用 Homebrew 安装

```sh
brew install typstyle
```

Windows 用户，可以使用 Scoop 安装

```sh
scoop install typstyle
```

然后，在`settings.json`中，加入

```json
{
  "[typst]": {
    "editor.defaultFormatter": "myriad-dreamin.tinymist"
  },
  "tinymist.completion.triggerOnSnippetPlaceholders": true,
  "tinymist.exportPdf": "onDocumentHasTitle",
  "tinymist.formatterMode": "typstyle",
  "tinymist.lint.enabled": true,
  "tinymist.outputPath": "$root/articles/$name",
  "tinymist.preview.cursorIndicator": true,
}
```
