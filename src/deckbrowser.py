
from anki.hooks import wrap

from aqt.gui_hooks import deck_browser_will_render_content, profile_did_open, profile_will_close
from aqt.deckbrowser import DeckBrowser, DeckBrowserContent
from .get_stats_html import get_html

from .utils import make_graph_js, add_browser_search_link

def add_graphs_to_deckbrowser(deckbrowser:DeckBrowser, content:"DeckBrowserContent"):
    content.stats += f"{get_html()}"

def add_deckbrowser_hook():
    deck_browser_will_render_content.append(add_graphs_to_deckbrowser)

def remove_deckbrowser_hook():
    deck_browser_will_render_content.remove(add_graphs_to_deckbrowser)

def init_deckbrowser():
    profile_did_open.append(add_deckbrowser_hook)
    profile_will_close.append(remove_deckbrowser_hook)
    DeckBrowser._linkHandler = wrap(DeckBrowser._linkHandler, add_browser_search_link, "before")



