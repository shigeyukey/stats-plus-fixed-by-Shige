from .webview import init_webview
from .deckbrowser import init_deckbrowser
from .overview import init_overview
from .congrats import init_congrats
from .addon_manager import init_addon_manager


def init():
    init_webview()
    init_deckbrowser()
    init_overview()
    init_congrats()
    init_addon_manager()
