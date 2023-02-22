from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox


# 学习动态加载ui 以及对ui里面widget命名
class Postman:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi(r"./ui/postman.ui")


app = QApplication([])
stats = Postman()
stats.ui.show()
app.exec_()
