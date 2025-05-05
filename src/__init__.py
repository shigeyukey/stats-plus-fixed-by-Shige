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

# from .webview import init_webview
from .deckbrowser import init_deckbrowser
from .overview import init_overview
from .congrats import init_congrats
# from .addon_manager import init_addon_manager




def init():
    # init_webview()
    init_deckbrowser()
    init_overview()
    init_congrats()
    # init_addon_manager()

