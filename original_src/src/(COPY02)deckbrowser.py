
from typing import Any, Callable

from anki.hooks import wrap
from aqt import QDialog, Qt
import aqt

from aqt.gui_hooks import deck_browser_will_render_content, profile_did_open, profile_will_close
from aqt import gui_hooks
from aqt.deckbrowser import DeckBrowser, DeckBrowserContent
import requests

from .utils import make_graph_js, get_active_deckbrowser_graphs, add_browser_search_link

from anki.stats import CollectionStats


def add_graphs_to_deckbrowser(deckbrowser:DeckBrowser, content:"DeckBrowserContent"):
    # graph_js = make_graph_js(get_active_deckbrowser_graphs())

    # from aqt import mw
    # mw.stats_plus_custom = CustomDeckStats(mw)

    # content.stats += f"""
    # <div id="graphsSection"></div>
    # <html><body>{mw.stats_plus_custom.get_html()}</body></html>
    # """

    # from aqt import mw
    # mw.stats_plus_custom = CustomDeckStats(mw)

    # content.stats += f"""
    # <div id="graphsSection">{get_html()}</div>
    # """
    content.stats += f"""
    {get_html()}
    """


    # def html_callback(html):
    #     content.stats += f"""
    #     <div id="graphsSection"></div>
    #     <html><body>{html}</body></html>
    #     """
    #     print("")
    #     print(html)
    #     print("")
    # mw.stats_plus_custom.get_html(html_callback)



#     content.stats += f"""
# <div id="graphsSection"></div>
# <script>{graph_js}</script>
# """


def add_deckbrowser_hook():
    deck_browser_will_render_content.append(add_graphs_to_deckbrowser)

def remove_deckbrowser_hook():
    deck_browser_will_render_content.remove(add_graphs_to_deckbrowser)


def init_deckbrowser():
    profile_did_open.append(add_deckbrowser_hook)
    profile_will_close.append(remove_deckbrowser_hook)
    DeckBrowser._linkHandler = wrap(DeckBrowser._linkHandler, add_browser_search_link, "before")


from aqt.operations.deck import set_current_deck
from anki.decks import DeckId
import time
from aqt.webview import AnkiWebViewKind
from aqt.main import AnkiQt
from aqt.forms import stats

class CustomDeckStats(QDialog):
    """Custom deck stats."""

    def __init__(self, mw: AnkiQt) -> None:
        QDialog.__init__(self, mw, Qt.WindowType.Window)
        mw.garbage_collect_on_dialog_finish(self)
        self.mw = mw
        self.name = "deckStats"
        self.period = 0
        self.form = stats.Ui_Dialog()
        self.oldPos = None
        self.wholeCollection = False
        self.setMinimumWidth(700)
        f = self.form
        f.setupUi(self)
        f.groupBox.setVisible(False)
        f.groupBox_2.setVisible(False)


        # from aqt.deckchooser import DeckChooser

        # self.deck_chooser = DeckChooser(
        #     self.mw,
        #     f.deckArea,
        #     on_deck_changed=self.on_deck_changed,
        # )

        # gui_hooks.stats_dialog_will_show(self)

        # self.form.web.set_kind(AnkiWebViewKind.DECK_STATS)
        # self.form.web.hide_while_preserving_layout()

        # self.show()
        # self.refresh()
        # self.form.web.set_bridge_command(self._on_bridge_cmd, self)
        # self.activateWindow()

    # def reject(self) -> None:
    #     self.deck_chooser.cleanup()
    #     self.form.web.cleanup()
    #     self.form.web = None
    #     aqt.dialogs.markClosed("NewDeckStats")
    #     QDialog.reject(self)

    def closeWithCallback(self, callback: Callable[[], None]) -> None:
        self.reject()
        callback()

    def on_deck_changed(self, deck_id: int) -> None:
        set_current_deck(parent=self, deck_id=DeckId(deck_id)).success(
            lambda _: self.refresh()
        ).run_in_background()

    def _on_bridge_cmd(self, cmd: str) -> bool:
        if cmd.startswith("browserSearch"):
            _, query = cmd.split(":", 1)
            browser = aqt.dialogs.open("Browser", self.mw)
            browser.search_for(query)

        return False

def get_html() -> None:

    from aqt import mw, QUrl
    from aqt.theme import theme_manager
    from anki.utils import hmr_mode

    # self.set_open_links_externally(True)
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

    # return f'<iframe src="{url}" width="100%" height="1000px"  style="border:none;"></iframe>'
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

