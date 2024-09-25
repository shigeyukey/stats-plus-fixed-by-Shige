from anki.hooks import wrap

from aqt.gui_hooks import overview_will_render_content
from aqt.overview import Overview, OverviewContent

from .utils import make_graph_js, add_browser_search_link
from .get_stats_html import get_html

def add_graphs_to_overview(self, content:OverviewContent):
    content.table += f"{get_html()}"


def init_overview():
    overview_will_render_content.append(add_graphs_to_overview)
    Overview._linkHandler = wrap(Overview._linkHandler, add_browser_search_link, "before")
