from aqt.gui_hooks import webview_will_set_content
from aqt.deckbrowser import DeckBrowser
from aqt.overview import Overview
from aqt.utils import showText
from aqt.webview import WebContent

def add_js_libraries(web_content:WebContent, context):
    if isinstance(context, (DeckBrowser, Overview)):
        web_content.js.extend(
            [
                "js/vendor/protobuf.min.js",
                "pages/graphs.js",
                # "js/vendor/jquery.min.js",
                # "js/vendor/plot.js",
            ]
        )

        web_content.css.append(
            "pages/graphs.css",

        )

def init_webview():
    pass
    # webview_will_set_content.append(add_js_libraries)
