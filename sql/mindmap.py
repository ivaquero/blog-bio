import pandas as pd
from graphviz import Digraph

mindmap = pd.read_csv("mindmap.csv")
layer0 = mindmap.query("Layer == 0")
layer1 = mindmap.query("Layer == 1").reset_index(drop=True)
layer2 = mindmap.query("Layer == 2").reset_index(drop=True)


def add_support(graph, item):
    if item.Support == "无":
        return
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
    graph = Digraph()
    graph.node(layer0.iloc[0].ID, layer0.iloc[0].Node, shape="box")
    add_support(graph, layer0.iloc[0])

    for i in range(layer1.shape[0]):
        item = layer1.iloc[i]
        graph.node(item.ID, item.Node, shape="box")
        graph.edge(layer0.iloc[0].ID, item.ID, label="包含")
        add_support(graph, item)
        layer2d = layer2[layer2.ID.str.startswith(item.ID)].reset_index(drop=True)
        for j in range(layer2d.shape[0]):
            item2 = layer2d.iloc[j]
            node2 = graph.node(item2.ID, label=item2.Node, shape="box")
            edge2 = graph.edge(item.ID, item2.ID, label="包含")
            add_support(graph, item2)

    graph.attr(rankdir="LR", ranksep="0.3", normalize="1")
    graph.format = "png"
    graph.render("mindmap")
    # graph.view()
