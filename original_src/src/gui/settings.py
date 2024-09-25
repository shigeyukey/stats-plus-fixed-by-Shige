from typing import List, Tuple

from aqt import QDialog

try:
    from .forms_qt6.settings import Ui_Settings # Qt6
except ImportError:
    from .forms.settings_ui import Ui_Settings # Qt5

class Settings(QDialog):
    def __init__(self, addons, callback):
        super().__init__(parent=addons)

        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.cb = callback

    def setupUi(
        self,
        graphs_deckbrowser: List[Tuple[str, bool]],
        graphs_overview: List[Tuple[str, bool]],
        graphs_congrats: List[Tuple[str, bool]],
    ):
        self.ui.deckBrowser.setupUi(graphs_deckbrowser)
        self.ui.deckOverview.setupUi(graphs_overview)
        self.ui.congratsPage.setupUi(graphs_congrats)

    def accept(self):
        self.cb(
            self.ui.deckBrowser.exportData(),
            self.ui.deckOverview.exportData(),
            self.ui.congratsPage.exportData(),
        )

        super().accept()
