# Form implementation generated from reading ui file 'C:\Users\shigg\AppData\Roaming\Anki2\addons21\stats plus fork by Shige\anki_stats_plus-master\designer\graph_list.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GraphList(object):
    def setupUi(self, GraphList):
        GraphList.setObjectName("GraphList")
        GraphList.resize(518, 242)
        self.verticalLayout = QtWidgets.QVBoxLayout(GraphList)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list = QtWidgets.QListWidget(parent=GraphList)
        self.list.setDragEnabled(True)
        self.list.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.InternalMove)
        self.list.setAlternatingRowColors(True)
        self.list.setMovement(QtWidgets.QListView.Movement.Snap)
        self.list.setProperty("isWrapping", False)
        self.list.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.list.setLayoutMode(QtWidgets.QListView.LayoutMode.SinglePass)
        self.list.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.list.setSelectionRectVisible(True)
        self.list.setObjectName("list")
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.list.addItem(item)
        self.verticalLayout.addWidget(self.list)

        self.retranslateUi(GraphList)
        QtCore.QMetaObject.connectSlotsByName(GraphList)

    def retranslateUi(self, GraphList):
        _translate = QtCore.QCoreApplication.translate
        GraphList.setWindowTitle(_translate("GraphList", "Form"))
        self.list.setSortingEnabled(False)
        __sortingEnabled = self.list.isSortingEnabled()
        self.list.setSortingEnabled(False)
        item = self.list.item(0)
        item.setText(_translate("GraphList", "Added Graph"))
        item = self.list.item(1)
        item.setText(_translate("GraphList", "Answer Buttons"))
        item = self.list.item(2)
        item.setText(_translate("GraphList", "Calendar Graph"))
        item = self.list.item(3)
        item.setText(_translate("GraphList", "Card Counts"))
        item = self.list.item(4)
        item.setText(_translate("GraphList", "Card Ease Graph"))
        item = self.list.item(5)
        item.setText(_translate("GraphList", "Future Due"))
        item = self.list.item(6)
        item.setText(_translate("GraphList", "Hourly Breakdown"))
        item = self.list.item(7)
        item.setText(_translate("GraphList", "Review Intervals"))
        item = self.list.item(8)
        item.setText(_translate("GraphList", "Reviews Graph"))
        item = self.list.item(9)
        item.setText(_translate("GraphList", "Today Stats"))
        self.list.setSortingEnabled(__sortingEnabled)
