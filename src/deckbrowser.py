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

from anki.hooks import wrap

from aqt import gui_hooks
from aqt.deckbrowser import DeckBrowser, DeckBrowserContent
from .get_stats_html import get_html

from .utils import add_browser_search_link

def add_graphs_to_deckbrowser(deckbrowser:DeckBrowser, content:"DeckBrowserContent"):
    content.stats += f"{get_html()}"

def add_deckbrowser_hook():
    gui_hooks.deck_browser_will_render_content.append(add_graphs_to_deckbrowser)

def remove_deckbrowser_hook():
    gui_hooks.deck_browser_will_render_content.remove(add_graphs_to_deckbrowser)

def init_deckbrowser():
    gui_hooks.profile_did_open.append(add_deckbrowser_hook)
    gui_hooks.profile_will_close.append(remove_deckbrowser_hook)
    DeckBrowser._linkHandler = wrap(DeckBrowser._linkHandler, add_browser_search_link, "before")



