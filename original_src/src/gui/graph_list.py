from typing import List, Tuple

from aqt import Qt, QWidget, QListWidget, QListWidgetItem

try:
    from .forms_qt6.graph_list import Ui_GraphList # Qt6
except ImportError:
    from .forms.graph_list_ui import Ui_GraphList # Qt5

from ..src.graphs import get_display_name, get_name_from_display_name

list_item_flags = (
    Qt.ItemFlag.ItemIsEnabled
    | Qt.ItemFlag.ItemIsSelectable
    | Qt.ItemFlag.ItemIsDragEnabled
    | Qt.ItemFlag.ItemIsDropEnabled
    | Qt.ItemFlag.ItemIsUserCheckable
    | Qt.ItemFlag.ItemNeverHasChildren
)

class GraphList(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.ui = Ui_GraphList()
        self.ui.setupUi(self)

        self.ui.list.clear()

    def setupUi(self, items: List[Tuple[str, bool]]):
        for name, enabled in items:
            widget_item = QListWidgetItem(self.ui.list)
            widget_item.setText(get_display_name(name))
            widget_item.setFlags(widget_item.flags() & list_item_flags)
            widget_item.setCheckState(Qt.CheckState.Checked if enabled else Qt.CheckState.Unchecked)
            self.ui.list.addItem(widget_item)

    def exportData(self) -> List[Tuple[str, bool]]:
        data = []

        count = self.ui.list.count()
        index = 0

        while index < count:
            item = self.ui.list.item(index)
            data.append(
                [
                    get_name_from_display_name(item.text()),
                    item.checkState() == Qt.CheckState.Checked,
                ]
            )

            index += 1

        return data



# list_item_flags = (
#     Qt.ItemIsEnabled
#     | Qt.ItemIsSelectable
#     | Qt.ItemIsDragEnabled
#     | Qt.ItemIsDropEnabled
#     | Qt.ItemIsUserCheckable
#     | Qt.ItemNeverHasChildren
# )

# class GraphList(QWidget):
#     def __init__(self, parent):
#         super().__init__(parent=parent)

#         self.ui = Ui_GraphList()
#         self.ui.setupUi(self)

#         self.ui.list.clear()

#     def setupUi(self, items: List[Tuple[str, bool]]):
#         for name, enabled in items:
#             widget_item = QListWidgetItem(self.ui.list)
#             widget_item.setText(get_display_name(name))
#             widget_item.setFlags(widget_item.flags() & list_item_flags)
#             widget_item.setCheckState(Qt.Checked if enabled else Qt.Unchecked)
#             self.ui.list.addItem(widget_item)

#     def exportData(self) -> List[Tuple[str, bool]]:
#         data = []

#         count = self.ui.list.count()
#         index = 0

#         while index < count:
#             item = self.ui.list.item(index)
#             data.append(
#                 [
#                     get_name_from_display_name(item.text()),
#                     item.checkState() == Qt.Checked,
#                 ]
#             )

#             index += 1

#         return data
