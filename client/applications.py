from PyQt5.QtWidgets import QTableWidgetItem, QApplication


def get_application_list(ui):
    ui.applications.insertRow(0)  # 在表格中要显示内容要先塞一个值
    # 微博
    item0 = QTableWidgetItem('微博')
    item1 = QTableWidgetItem('https://m.weibo.cn/api/container/getIndex')
    item2 = QTableWidgetItem('1220078652')
    item5 = QTableWidgetItem('同步')
    ui.applications.setItem(0, 0, item0)
    ui.applications.setItem(0, 1, item1)
    ui.applications.setItem(0, 2, item2)
    ui.applications.setItem(0, 5, item5)
