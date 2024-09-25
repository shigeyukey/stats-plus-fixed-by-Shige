from typing import List, Tuple, Optional

from dataclasses import dataclass


@dataclass(frozen=True)
class Graph:
    """Class for keeping track of an item in inventory."""

    library: str
    name: str
    display_name: str


anki_graphs = [
    Graph("anki", "TodayStats", "Today Stats"),
    Graph("anki", "FutureDue", "Future Due Graph"),
    Graph("anki", "CalendarGraph", "Calendar Graph"),
    Graph("anki", "ReviewsGraph", "Reviews Graph"),
    Graph("anki", "CardCounts", "Card Counts"),
    Graph("anki", "IntervalsGraph", "Review Intervals"),
    Graph("anki", "EaseGraph", "Card Ease Graph"),
    Graph("anki", "HourGraph", "Hourly Breakdown"),
    Graph("anki", "ButtonsGraph", "Answer Buttons Graph"),
    Graph("anki", "AddedGraph", "Added Graph"),
]



addon_graphs = [
    # TO ADD-ON DEVELOPERS:
    # please insert extra graphs in here


    # Graph("anki", "StabilityGraph","Stability Graph"),
    # Graph("anki", "DifficultyGraph","Difficulty Graph"),
    # Graph("anki", "RetrievabilityGraph","Retrievability Graph"),
    # Graph("anki", "RangeBox","Range Box"),
    # Graph("anki", "RevlogRange","Revlog Range"),


]


def get_available_graphs() -> List[Graph]:
    return anki_graphs + addon_graphs


def get_graph(name: str) -> Optional[Graph]:
    available_graphs = get_available_graphs()
    filtered = filter(lambda graph: graph.name == name, available_graphs)

    try:
        graph = next(filtered)
    except:
        graph = None

    return graph


def get_graph_by_display_name(display_name: str) -> Optional[Graph]:
    available_graphs = get_available_graphs()
    filtered = filter(lambda graph: graph.display_name == display_name, available_graphs)

    try:
        graph = next(filtered)
    except:
        graph = None

    return graph


def get_library(name: str) -> Optional[str]:
    if graph := get_graph(name):
        return graph.library

    return None


def get_display_name(name: str) -> Optional[str]:
    if graph := get_graph(name):
        return graph.display_name

    return None


def get_name_from_display_name(display_name: str) -> Optional[str]:
    if graph := get_graph_by_display_name(display_name):
        return graph.name

    return None


def update_graphs(graphs: List[Tuple[str, bool]]) -> List[Tuple[str, bool]]:
    available_graphs = get_available_graphs()

    names = []
    for graph in graphs:
        names.append(graph[0])

    available_names = []
    for graph in available_graphs:
        available_names.append(graph.name)

    names_available = []
    for name in names:
        names_available.append(name in available_names)

    graphs_available = []
    for graph in graphs:
        if names_available[graphs.index(graph)]:
            graphs_available.append(graph)

    names_additional = []
    for name in available_names:
        if name not in names:
            names_additional.append(name)

    graphs_additional = []
    for name in names_additional:
        graphs_additional.append([name, False])

    return graphs_available + graphs_additional
