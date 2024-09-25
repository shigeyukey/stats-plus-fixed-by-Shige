from typing import List, Any

from aqt import mw, dialogs

# from .graphs import get_library


def make_graph_css() -> str:
    return f"""
const graphsStyle = document.createElement("link");
graphsStyle.rel = "stylesheet"
graphsStyle.href = "graphs.css"
document.head.appendChild(graphsStyle)
"""


def make_graph_js(graphs: List[str], query: str = "") -> str:
    graph_string = ",\n".join(graphs)

    return f"""
anki.graphs(document.getElementById("graphsSection"), [
    {graph_string},
], {{
    search: `{query}`,
    days: 0,
}})
"""


class ProfileConfig:
    """Can be used for profile-specific settings"""

    def __init__(self, keyword: str, default: Any):
        self.keyword = keyword
        self.default = default

    @property
    def value(self) -> Any:
        return mw.pm.profile.get(self.keyword, self.default)

    @value.setter
    def value(self, new_value: Any):
        mw.pm.profile[self.keyword] = new_value

    def remove(self):
        try:
            del mw.pm.profile[self.keyword]
        except KeyError:
            # same behavior as Collection.remove_config
            pass


default_graphs = [
    ["CalendarGraph", True],
    ["FutureDue", True],
]



def add_browser_search_link(self, cmd: str) -> Any:
    if cmd.startswith("browserSearch"):
        _, query = cmd.split(":", 1)
        browser = dialogs.open("Browser", self.mw)
        browser.search_for(query)
