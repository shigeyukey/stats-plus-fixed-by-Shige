from typing import Any

from anki.hooks import wrap

from aqt.gui_hooks import deck_browser_will_render_content, profile_did_open, profile_will_close
from aqt.deckbrowser import DeckBrowser, DeckBrowserContent

from .utils import make_graph_js, get_active_deckbrowser_graphs, add_browser_search_link

def add_graphs_to_deckbrowser(self, content:"DeckBrowserContent"):
    graph_js = make_graph_js(get_active_deckbrowser_graphs())
    from aqt import mw
    mw.web.load_sveltekit_page("graphs")

    content.stats += f"""
<div id="graphsSection"></div>
<script>{graph_js}</script>
"""


def add_deckbrowser_hook():
    deck_browser_will_render_content.append(add_graphs_to_deckbrowser)


def remove_deckbrowser_hook():
    deck_browser_will_render_content.remove(add_graphs_to_deckbrowser)


def init_deckbrowser():
    profile_did_open.append(add_deckbrowser_hook)
    profile_will_close.append(remove_deckbrowser_hook)
    DeckBrowser._linkHandler = wrap(DeckBrowser._linkHandler, add_browser_search_link, "before")



# anki.graphs(document.getElementById("graphsSection"), [
#     anki.CalendarGraph,
# anki.FutureDue,
# ], {
#     search: ``,
#     days: 0,
# })


# from aqt.utils import tooltip
# tooltip(graph_js, 10000)
# print("")
# print("")
# print(graph_js)
# print("")
# print("")