"""
依赖安装方法如下，推荐度由高到低

安装方法 1
mamba install pandas python-graphviz
安装方法 2
conda install pandas python-graphviz
安装方法 3
pip install pandas graphviz

运行
python -u mindmap.py
或
$(which python) -u mindmap.py
"""

import pandas as pd
from graphviz import Digraph

# 读取文件
mindmap = pd.read_csv("mindmap.csv")
# 获取每层元素
layer0 = mindmap.query("Layer == 0")
layer1 = mindmap.query("Layer == 1").reset_index(drop=True)
layer2 = mindmap.query("Layer == 2").reset_index(drop=True)


# 添加支持项
def add_support(graph, item):
    # 无支持项，则跳过
    if item.Support == "无":
        return
    # 有支持项，则根据支持项类型，选择 Node 图形
    shape = "note" if item.Support.endswith("实例") else "box"
    graph.node(item.ID + "s", label=item.Support, shape=shape)
    graph.edge(
        item.ID,
        item.ID + "s",
        label="支持",
        constraint="true",
        arrowhead="none",
        arrowtail="normal",
        dir="both",
    )


if __name__ == "__main__":
    # 创建有向图对象
    graph = Digraph()
    # 添加中心节点
    graph.node(layer0.iloc[0].ID, layer0.iloc[0].Node, shape="box")
    add_support(graph, layer0.iloc[0])

    # 添加第一层节点
    for i in range(layer1.shape[0]):
        item = layer1.iloc[i]
        graph.node(item.ID, item.Node, shape="box")
        graph.edge(layer0.iloc[0].ID, item.ID, label="包含")
        add_support(graph, item)
        # 第二层节点条件：ID 与第一层节点相同
        cond = layer2.ID.str.startswith(item.ID)
        # 匹配第二层节点
        layer2d = layer2[cond].reset_index(drop=True)
        # 添加第二层节点
        for j in range(layer2d.shape[0]):
            item2 = layer2d.iloc[j]
            graph.node(item2.ID, label=item2.Node, shape="box")
            graph.edge(item.ID, item2.ID, label="包含")
            add_support(graph, item2)

    # 布局
    graph.attr(rankdir="LR", ranksep="0.3", normalize="1")
    # 输出格式
    graph.format = "png"
    # 输出
    graph.render("mindmap")
    # graph.view()
