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


from os.path import basename

from aqt.webview import AnkiWebView
from aqt import gui_hooks

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
    gui_hooks.webview_did_inject_style_into_page.append(add_graphs_to_congrats)
