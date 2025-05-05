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
