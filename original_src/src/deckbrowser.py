
from typing import Any, Callable

from anki.hooks import wrap
from aqt import QDialog, Qt
import aqt

from aqt.gui_hooks import deck_browser_will_render_content, profile_did_open, profile_will_close
from aqt.deckbrowser import DeckBrowser, DeckBrowserContent

from .utils import make_graph_js, get_active_deckbrowser_graphs, add_browser_search_link

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

from aqt import mw, QUrl
from aqt.theme import theme_manager
from anki.utils import hmr_mode

def get_html() -> None:
    if theme_manager.night_mode:
        extra = "#night"
    else:
        extra = ""

    if hmr_mode:
        server = "http://127.0.0.1:5173/"
    else:
        server = mw.serverURL()

    url = QUrl(f"{server}{'graphs'}{extra}").toString()

    zoom_scale = 0.8
    width_percentage = 100 / zoom_scale
    height_px = 1000 / zoom_scale

    return f'''
    <div style="width: {width_percentage}%; height: 1000px; overflow: hidden;">
    <iframe src="{url}" width="100%" height="{height_px}px" style="border:none;"></iframe>
    </div>
    <style>
        iframe {{
            transform: scale({zoom_scale});
            transform-origin: 0 0;
        }}
    </style>
    '''

