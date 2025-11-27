---
title: 搭建 Python 轻量级编写环境（VSCode | JupyterLab）
zhihu-url: https://zhuanlan.zhihu.com/p/147336202
zhihu-title-image: images/vscode/jupyter.png
zhihu-tags: Visual Studio Code, Python, Jupyter Notebook
---

# 搭建 Python 轻量级编写环境

## 1. 安装运行时

### 1.1. Conda -> Mamba

Conda 是服务于 Python 和 R 的多语言包管理器，其解决了 Python 原生包管理器 Pip 的依赖冲突问题，极大地方便了 Python 环境的管理。Mamba 是 Conda 的 C++ 版本，默认并行下载，效率比 Conda 更上一个台阶。

这里推荐安装 Miniforge，基于 Mamba 的最小安装版本，只包含环境管理功能。前往[清华源](https://mirrors.tuna.tsinghua.edu.cn/)，进入[对应页面](https://mirrors.tuna.tsinghua.edu.cn/github-release/conda-forge/miniforge/LatestRelease/)，下载安装程序

### 1.2. 手动安装

- 对 Windows 用户

下载 [Windows 系统安装包](https://mirrors.tuna.tsinghua.edu.cn/github-release/conda-forge/miniforge/LatestRelease/Miniforge3-Windows-x86_64.exe)，安装一路向下，不要做任何改动，直至安装完成。

- 对 macOS 用户

下载 [MacOS 系统安装包](https://mirrors.tuna.tsinghua.edu.cn/github-release/conda-forge/miniforge/LatestRelease/Miniforge3-MacOSX-arm64.sh)，然后到对应路径，输入

```sh
sh Miniforge3-MacOSX-arm64.sh
```

### 1.3. 包管理器安装

对 Windows 用户，使用 Scoop

```powershell
scoop install miniforge
# 或国内镜像
scoop install scoopforge/extras-cn/miniforge-cn
```

对 macOS 用户，有 Homebrew

```sh
brew install miniforge
# 或国内镜像
brew install brewforge/chinese/miniforge-cn
```

## 2. 管理环境

### 2.1. 配置文件

mamba 配置文件为 `.condarc`。其位置如下：

- Windows：`~\.condarc`
- macOS 和 Linux：`~/.condarc`

打开对应终端环境

- Windows 用户：Miniforge Prompt
- MacOS 用户：终端（Terminal）

输入

```sh
code .condarc
```

在 `.condarc` 中写入

```yaml
# 频道
channels:
  - conda-forge
# 使用镜像
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

# 地址
envs_dirs:
  - ~/.conda/envs
pkgs_dirs:
  - ~/.conda/pkgs

# 将 pip 作为 Python 的依赖
add_pip_as_python_dependency: true
# 安装按照频道的顺序
channel_priority: flexible
# 生成错误报告
report_errors: false
# ssl 验证
ssl_verify: false
# 显示频道具体链接
show_channel_urls: true
# 错误回滚
rollback_enabled: true
# 重试
remote_max_retries: 3
```

### 2.2. 常用环境操作

mamba 常用操作可使用命令 `mamba -h` 和 `mamba config -h` 查看，这里列出几个常用命令：

```sh
# 创建
mamba create -n [env_name]
# 删除
mamba env remove -n [env_name]
# 参照配置文件更新
mamba env update --file [file.yml]
# 环境列表
mamba env list
# mamba 信息
mamba info
```

### 2.3. 创建环境

接下来，需要创建虚拟环境，也就是自己的工作区，可简单理解为系统登录时的用户。基本命令需指定**环境名称**和**Python 版本**：

```sh
# 基本格式
mamba create -n [env_name] [python= version]
# 例子
mamba create -n my_python python=3.12
```

安装完毕后，进入环境：

```sh
# 进入
mamba active my_python
# 退出
mamba deactivate
```

## 3. 包管理

### 3.1. 常用包操作

```sh
# 安装
mamba install [package_name]
# 删除
mamba uninstall [package_name]
# 更新
mamba update [package_name]
# 更新所有包
mamba update --all
# 搜索
mamba search [package_name]
# 已安装列表
mamba list
```

### 3.2. 安装包

为使用 VSCode 的 Jupyter，还需要安装 `ipykernel`

```sh
mamba install ipykernel
```

## 4. VSCode

### 4.1. 安装扩展

- Python
- Jupyter
- Ruff

![python](images/vscode/vscode-python.png)

扩展安装完毕，新建 `.ipynb` 文件，即可开启 Python 之旅。

![alt text](images/vscode/vscode-python-ruff.png)

### 4.2. 配置扩展

相关配置如下

```json
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    }
  },
  "ruff.configuration": "pyproject.toml",
}
```

## 5. 项目管理

项目根目录下的 `pyproject.toml` 可采用如下编写

```toml
[project]
    requires-python = ">=3.11"

[tool.ruff]
    fix = true
    fix-only = true
    target-version = "py311"
    line-length = 88

[tool.ruff.format]
    # Enable reformatting of code snippets in docstrings
    docstring-code-format = true
    # Format all docstring code snippets with a line length of 60
    docstring-code-line-length = 60
    # Use `\n` line endings for all files
    line-ending = "lf"
    # Prefer single quotes over double quotes
    quote-style = "double"
    skip-magic-trailing-comma = true

[tool.ruff.lint]
    extend-select = [
        "E",    # pycodestyle errors
        "W",    # pycodestyle warnings
        "F",    # pyflakes
        "B",    # flake8-bugbear
        "C4",   # flake8-comprehensions
        "EM",   # flake8-errmsg
        "FA",   # flake8-future-annotations
        "G",    # flake8-logging-format
        "INT",  # flake8-gettext
        "PIE",  # flake8-pie
        "PT",   # flake8-pytest-style
        "PYI",  # flake8-pyi
        "Q",    # flake8-quotes
        "RET",  # flake8-return
        "RSE",  # flake8-raise
        "SLOT", # flake8-slots
        "T10",  # flake8-debugger
        "YTT",  # flake8-2020
        "DTZ",  # naive datetime
        "I",    # import sorting
        "ISC",  # string concatenation
        "NPY",  # numpy specific rules
        "PERF", # perflint
        "RUF",  # ruff
        "S",    # security
        "SIM",  # simplify
        "T10",  # debugger
        "TCH",  # type-checking imports
        "TID",  # tidy imports
        "UP",   # upgrade
    ]
    fixable = ["ALL"]
    ignore = [
        "B905",   # `zip()` without an explicit `strict=` parameter
        "EM101",  # exception must not use a string literal
        "EM102",  # exception must not use an f-string literal
        "ISC001", # conflicts with formatter
        "NPY002", # replace legacy `np.random.random`
        "E501",   # line too long
        "E741",
        "F403",
        "F405",
        "RUF001", # string contains ambiguous character (such as greek letters)
        "RUF002", # docstring contains ambiguous character (such as greek letters)
        "RUF003",
    ]
    unfixable = []

[tool.ruff.lint.pydocstyle]
    convention = "numpy"

[tool.ruff.lint.isort]
    case-sensitive = true
    combine-as-imports = true
    force-wrap-aliases = true
    order-by-type = true
```

## 6. WSL2

Windows 下的 Python 环境经常会给人带来一系列的困扰，如，时隐时现的各种因为环境变量导致的奇怪报错，Conda 库更新不到最新的版本，还有诸如 XGBoost 等库压根儿就不提供 Win 版等。现在，WSL2（Windows Subsystem Linux 2）的出现，让我们有了一种新的选择。WSL2 是一个 Windows 的内置虚拟机，可运行 Linux 环境，一旦有了 Linux 环境，后面的配置不必多说。

### 6.1. 安装 WSL2

在控制面板 -> 程序和功能 -> Windows 功能窗口中勾选适用于 Linux 的 Windows 子系统 功能，点击确定，并按照提示重启电脑。

![WSL2](images/wsl2/wsl2.png)

在 Windows 应用商店搜索 WSL，选择自己想要的 Linux 发行版，点击下载安装即可。这里选择的是 Ubuntu 20.04。

![Ubuntu](images/wsl2/app.png)

由于版本问题，好多人的的子系统还停留在 WSL，而非 WSL2。对于升级，输入如下命令

```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --set-version Ubuntu-20.04 2
```

中间需要下载一个 [WSL2-kernel](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

若之前没有用过 WSL，则首先需要安装 Windows 10 的 WSL 功能：

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

这部分详情见 [WSL2](https://docs.microsoft.com/en-us/windows/wsl/wsl2-kernel)

### 6.2. 调试 Linux

- 版本

安装完成后，使用微软自家的 Windows-Terminal 打开一个 Ubuntu 标签，待其初始化完成。通过如下命令查看版本

```powershell
wsl -l -v
```

![WSL2 version](images/wsl2/version.png)

- 设置 WSL2 为默认版本

```powershell
wsl --set-default-version 2
```

- 卸载

```powershell
wslconfig /u Ubuntu-20.04
```

- 初始化

输入以下命令，为 root 用户设置密码。

```sh
sudo passwd root
```

当然，你也可使用如下命令，创建新用户

```sh
sudo adduser username
```

### 6.3. Miniforge

- 下载安装

```sh
wget -c https://mirrors.tuna.tsinghua.edu.cn/github-release/conda-forge/miniforge/LatestRelease/Miniforge3-Linux-x86_64.sh
bash Miniforge3-25.3.1-0-Linux-x86_64.sh
```

有关 mamba 的具体使用，这里不再赘述。

### 6.4. Jupyter

这里可以选择安装 JupyterLab

```python
mamba install jupyterlab
```

关键是第二步，让 Jupyter 自动打开宿主浏览器。打开配置文件 `jupyter_notebook_config.py`。

```sh
vi ~/.jupyter/jupyter_notebook_config.py
```

若无，由如下命令生成

```sh
jupyter notebook --generate-config
```

修改下面这如下一行

```python
c.NotebookApp.use_redirect_file = False
```

退回到主界面，在 `~/.bashrc` 或 `~/.zshrc` 文件末尾添加，指定默认浏览器地址，其中，`/mnt/` 之后的部分是你默认浏览器的在 Windows 上的地址

```sh
export BROWSER="/mnt/c/'program files (x86)'/microsoft/edge/application/msedge.exe"
```

使用 `source` 刷新后，就可愉快地使用 Linux 版的 Python 了。

![JupyterLab](images/jupyter/jupyter-python.png)
