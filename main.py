from PyQt5.QtWidgets import *
from PyQt5 import uic  # Импортируем uic
import sys
import sqlite3


class coffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.setFixedSize(self.width(), self.height())
        self.db = sqlite3.connect('coffee.sqlite')
        self.cur = self.db.cursor()
        self.setupUI()

        self.btn_add.clicked.connect(self.open_add_widnow)
        self.btn_edit.clicked.connect(self.open_edit_widnow)
        self.tableWidget.cellPressed[int, int].connect(self.clickedRow)

    def setupUI(self):
        self.setWindowTitle('Кофе')
        self.btn_add = QPushButton(self)
        self.btn_add.setText('Добавить кофе')
        self.btn_add.adjustSize()
        self.btn_add.move(100, 50)
        self.btn_edit = QPushButton(self)
        self.btn_edit.setText('Редактировать кофе')
        self.btn_edit.adjustSize()
        self.btn_edit.setEnabled(False)
        self.btn_edit.move(625, 50)
        self.coffee = self.cur.execute('select * from coffee').fetchall()
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(self.coffee):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def clickedRow(self, x, y):
        self.btn_edit.setEnabled(True)
        self.x = x

    def updateTable(self):
        self.tableWidget.setRowCount(0)
        self.coffee = self.cur.execute('select * from coffee').fetchall()
        for i, row in enumerate(self.coffee):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def open_add_widnow(self):
        self.addCoffee = addCoffee(self, '1')
        self.addCoffee.show()

    def open_edit_widnow(self):
        self.editCoffee = addCoffee(self, '2')
        self.editCoffee.show()

    def closeEvent(self, event):
        self.db.close()


class addCoffee(QWidget):
    def __init__(self, root, per):
        super(addCoffee, self).__init__()
        self.root = root
        self.per = per  # Указатель обозначающий операцию с кофе
        self.cur = self.root.cur
        uic.loadUi('addEditCoffeeForm.ui', self)  # Загружаем дизайн
        self.setupUI()

        self.pushButton.clicked.connect(self.DB)

    def setupUI(self):
        if self.per == '1':
            self.setWindowTitle('Добавление кофе')
            self.label.setText('Добавление кофе')
            self.label.adjustSize()
        elif self.per == '2':
            self.setWindowTitle('Редактирование кофе')
            self.label.setText('Редактирование кофе')
            self.label.adjustSize()
            self.lineEdit.setText(self.root.tableWidget.item(self.root.x, 1).text())
            self.comboBox_2.setCurrentText(self.root.tableWidget.item(self.root.x, 2).text())
            self.comboBox.setCurrentText(self.root.tableWidget.item(self.root.x, 3).text())
            self.lineEdit_4.setText(self.root.tableWidget.item(self.root.x, 5).text())
            self.comboBox_3.setCurrentText(self.root.tableWidget.item(self.root.x, 6).text())
            self.plainTextEdit.setPlainText(self.root.tableWidget.item(self.root.x, 4).text())
        self.label.move(self.width() // 2 - self.label.width() // 2, self.label.y())

    def DB(self):
        if self.per == '1':
            name = self.lineEdit.text()
            level = self.comboBox_2.currentText()
            type_coffee = self.comboBox.currentText()
            price = self.lineEdit_4.text()
            volume = self.comboBox_3.currentText()
            description = self.plainTextEdit.toPlainText()
            self.cur.execute('INSERT INTO coffee (name, level, ground_grains, description, price, volume)'
                             'values (?, ?, ?, ?, ?, ?)', (name,  level, type_coffee, description, price, volume))
        elif self.per == '2':
            name = self.lineEdit.text()
            level = self.comboBox_2.currentText()
            type_coffee = self.comboBox.currentText()
            price = self.lineEdit_4.text()
            volume = self.comboBox_3.currentText()
            description = self.plainTextEdit.toPlainText()
            self.cur.execute('update coffee set name=?, level=?, ground_grains=?,'
                             ' description=?, price=?, volume=? where ID = ?',
                             (name, level, type_coffee, description, price, volume,
                              self.root.tableWidget.item(self.root.x, 0).text()))
        self.root.db.commit()
        self.root.updateTable()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = coffee()
    ex.show()
    sys.exit(app.exec_())
