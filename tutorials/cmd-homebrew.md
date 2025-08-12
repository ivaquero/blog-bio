---
title: 搭建 macOS/Linux 统一开发环境（Homebrew）
zhihu-url: https://zhuanlan.zhihu.com/p/144608732
zhihu-title-image: images/cmd/brew.jpg
zhihu-tags: Homebrew, Linux, macOS
---

# 搭建 macOS/Linux 统一开发环境

## Homebrew 简介

相比于 Windows，macOS 的软件管理在大多数时候都相对简单，解压安装即可，且，安装路径都统一在 `Applications` 文件夹下。但涉及到一些含有依赖（dependency）的开发软件，如 MySQL 等，有时就会麻烦很多，加之 macOS 长期受人诟病的窗口管理，一旦文件夹层级过多，操作起来分成不方便。Homebrew 是一款 macOS 平台下的包管理工具，拥有安装、卸载、更新、查看、搜索等诸多实用的功能。简单的一条命令，就可实现包管理，自动处理相应依赖，所有的文件都会被统一安放在几个指定的文件夹里，几乎不用额外关心。

Homebrew 同样适用于 Linux，也就是说，在 Windows Subsystem Linux（WSL）中，同样可使用 Homebrew。

相比于 Linux 原生的包管理器，Homebrew 不需要管理员权限，这对很多使用云主机以及没有管理员权限的公共电脑工作人有着巨大的优势。

1. 不需要额外添加各种源
2. 可管理服务
3. 不需要频繁使用管理员权限
4. 更重要的是命令简洁统一。如 `apt-get install` 是安装，卸载却变成了 `apt-get remove`，而非 `apt-get uninstall`，反直觉。

> 详细介绍，可前往 [Homebrew 官网](https://brew.sh/)

## Homebrew 的安装

Homebrew 需要在 macOS 上预先安装 Xcode 命令行工具。

```bash
xcode-select --install
```

若出现问题，可直接前往官网，下载对应的 Command Line，下载地址为 [XCode](https://developer.apple.com/download/more/)

安装 Homebrew

```bash
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh/bin/bash -c | sh
```

国内源

```bash
curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh | sh
```

卸载方法类似：

```bash
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall | sh
```

## Homebrew 的使用

### 基本操作

```bash
# 安装
brew install [package_name]
# 卸载
brew uninstall [package_name]
# 升级自身
brew update
# 升级
brew upgrade [package_name]
# 升级全部
brew upgrade
# 查看已安装列表
brew list
# 查看可升级列表
brew outdated
# 查找
brew search [package_name]
# 清理缓存
brew cleanup
# 查看信息
brew info
# 自身诊断
brew doctor
# 获取缓存路径
brew --cache
```

### Tap 的加载

Tap 可看作是 Homebrew 的软件源，是其外在延申。Homebrew 的官方 Tap 包含了大量的基于图形用户界面（GUI）的软件，有大量的维护者，故一般常用软件，无论中英文，都可在其中找到。Tap 使用 `brew tap` 命令进行加载。

```bash
# 官方源
brew tap homebrew/homebrew-cask
# 官方未收录的中文软件
brew tap brewforge/chinese
# 官方未收录的国际软件
brew tap brewforge/extras
```

欲查询安装脚本的详细信息，可前往 [Homebrew Formulae](https://formulae.brew.sh/)

Homebrew 允许用户建立自己的 Tap，如添加我建立的 [homebrew-chinese](https://github.com/brewforge/homebrew-chinese)：

```bash
brew tap brewforge/chinese
```

> 这个库收录了一些官方库里没有的国产软件，如每日英语听力、每日法语听力、每日西语听力，WPS 国内版，和开源软件的国内镜像版本，如 Miniforge。

|      App 名       |     Cask 名     | 原创 | 自动更新 |
|:-----------------:|:---------------:|:----:|:--------:|
|  M3U8-Downloader  | m3u8-downloader |  √   |    √     |
| Miniforge 清华源  | `miniforge-cn`  |  √   |    √     |
| WPS Office 国内版 | `wpsoffice-cn`  |  √   |    √     |
|   每日法语听力    |    `ting-fr`    |  √   |    √     |
|   每日英语听力    |    `ting-en`    |  √   |    √     |
|   每日西语听力    |    `ting-es`    |  √   |    √     |
|     西语助手      |   `eshelper`    |  √   |    √     |

### Cask 的使用

Cask 的使用与 Homebrew 本身大同小异，只需将 `brew` 变为 `brew --cask` 即可。这里有两处需要注意：

- Cask 中软件的搜索依然是 `brew search` ；
- Cask 中软件的升级很多时候需要使用贪婪模式，即 `brew upgrade --cask --greedy` ；

### Services 的使用

Homebrew 绑定了 Services 工具包，可非常便捷地管理系统服务：

```bash
# 开启
brew services start mysql
# 停止
brew services stop mysql
# 重启
brew services restart mysql
# 列出当前的状态
brew services list
```

## 其他

### 报错

对于更新失败等一般报错，使用自带的重置功能：

```bash
# 一般报错
brew update-reset && brew update
# Error: parent directory is world writable but not sticky
sudo chmod +t /private/tmp/
```

对于复杂报错，进入 Homebrew 所在目录，强制重置：

```bash
cd /usr/local/Homebrew
sudo git reset --hard
sudo git clean -df
brew update
sudo git stash
```
