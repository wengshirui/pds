# 项目入口
from client.getDataBases import Stats
from PyQt5.QtWidgets import QApplication

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
