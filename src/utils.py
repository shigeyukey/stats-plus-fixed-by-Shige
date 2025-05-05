# Copyright (C) Henrik Giesel 2021 <https://github.com/hgiesel>
#   Ankiweb <https://ankiweb.net/shared/info/1009670238> Github <https://github.com/hgiesel/anki_stats_plus>
# Copyright (C) Shigeyuki 2024 - 2025 <http://patreon.com/Shigeyuki>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
