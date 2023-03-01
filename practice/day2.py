import time

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTextBrowser
from PyQt5.QtCore import pyqtSignal, QObject  # 最稳妥，官方信息发送入口

from threading import Thread


class MySignals(QObject):
    text_print = pyqtSignal(QTextBrowser, str)


global_ms = MySignals()


# 学习动态加载ui 以及对ui里面widget命名
class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi(r"./ui/day2.ui")
        self.ui.pushButton.clicked.connect(self.sendMsg)

        # 还是为了发信息
        global_ms.text_print.connect(self.printToGui)

    def printToGui(self, fb, text):
        fb.append(str(text))
        fb.ensureCursorVisible()

    def sendMsg(self):
        t = Thread(target=self.task)  # 简单的线程知识，避免一次发送信息
        t.start()
        # for i in range(1, 10):
        #     print(i)
        #     self.ms.text_print.emit(f'尝试发送信息{i}')
        #     time.sleep(1)

    def task(self):
        for i in range(1, 10):
            print(i)
            global_ms.text_print.emit(self.ui.textBrowser, f'输出内容{i}')
            # self.ui.textBrowser.append(f'尝试发送信息{i}')
            time.sleep(1)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
