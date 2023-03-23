# 项目入口
import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QApplication
from storage.databases import getDataList
from client.index import get_readme
from client.applications import get_application_list

fpath = os.path.dirname(__file__)
print(fpath)

ui = f'{fpath}/ui/main.ui'


# 首页展示项目的readme
# 数据库展示本地数据库
# 应用展示授权的应用
# 关于我们展示啥呢，捐钱？好好写代码让自己静下心
# 操作日志就是展示数据库或者系统的操作日志，谁什么时间干了什么事情

# 学习动态加载ui 以及对ui里面widget命名
class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi(ui)
        self.ui.getList.clicked.connect(self.showDataTable)
        self.ui.readme.setHtml(get_readme())
        item1 = QTableWidgetItem()
        item1.setText('test')
        get_application_list(self.ui)

    def showDataTable(self):
        r_list = getDataList()
        for i in r_list:
            print(i)
            if i != 'admin':
                self.ui.databases.insertRow(0)
                item = QTableWidgetItem()
                item.setText(i)
                self.ui.databases.setItem(0, 1, item)



        # 163邮箱


    def set_item(self, param):
        for k, v in param:
            print(k, v)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
