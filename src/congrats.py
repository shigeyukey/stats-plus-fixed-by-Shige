from os.path import basename

from aqt.webview import AnkiWebView
from aqt.gui_hooks import webview_did_inject_style_into_page

from .get_stats_html import get_html


def add_graphs_to_congrats(webview: AnkiWebView):
    page = basename(webview.page().url().path())
    print(page)

    if page != "congrats":
        return

    # webview.eval(f"{get_html()}")
    webview.eval(
        f"""
    const iframeContainer = document.createElement("div")
    iframeContainer.innerHTML = `{get_html()}`
    document.body.appendChild(iframeContainer)
    """
    )

def init_congrats():
    webview_did_inject_style_into_page.append(add_graphs_to_congrats)
