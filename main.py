from PyQt5.QtWidgets import *
from PyQt5 import uic  # Импортируем uic
import sys
import sqlite3


class coffee(QWidget):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect('coffee.sqlite')
        self.cur = self.db.cursor()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.coffee = self.cur.execute('select * from coffee').fetchall()
        for i, row in enumerate(self.coffee):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def closeEvent(self, event):
        self.db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = coffee()
    ex.show()
    sys.exit(app.exec_())
