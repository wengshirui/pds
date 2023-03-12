# 项目入口
import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QApplication
from storage.databases import getDataList

ffpath = os.path.dirname(os.path.dirname(__file__))
# print(ffpath)

ui = f'{ffpath}/ui/main.ui'


# print(ui)

# 学习动态加载ui 以及对ui里面widget命名
class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi(ui)
        self.ui.getList.clicked.connect(self.showDataTable)

    def showDataTable(self):
        r_list = getDataList()
        for i in r_list:
            print(i)
            if i != 'admin':
                self.ui.databases.insertRow(0)
                item = QTableWidgetItem()
                item.setText(i)
                self.ui.databases.setItem(0, 1, item)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
