from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox

# 学习动态加载ui 以及对ui里面widget命名
class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi(r"./ui/day1.ui")
        self.ui.pushButton.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.ui.plainTextEdit.toPlainText()

        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')

            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.ui,
                          '统计结果',
                          f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                          )


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
