from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import uic  # Импортируем uic
import sys
import sqlite3


class coffee(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(851, 701)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 831, 591))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(320, 20, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.label.setFont(font)

        self.retranslateUi()

        self.setFixedSize(self.width(), self.height())
        self.db = sqlite3.connect('..\\data\\coffee.sqlite')
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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Название сорта"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Степень обжарки"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Молотый/в зернах"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Описание"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Цена"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Объем упаковки"))
        self.label.setText(_translate("Form", "КОФЕ"))


class addCoffee(QWidget):
    def __init__(self, root, per):
        super(addCoffee, self).__init__()
        self.root = root
        self.per = per  # Указатель обозначающий операцию с кофе
        self.cur = self.root.cur

        self.resize(416, 588)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(120, 76, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 10, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(4, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(52, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(53, 270, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(78, 190, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 196, 281, 20))
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(15, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(120, 280, 281, 211))
        self.plainTextEdit.setPlainText("")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(100, 530, 201, 31))
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(120, 157, 281, 22))
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 116, 281, 22))
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 237, 281, 22))
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.retranslateUi()

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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "Добавление кофе"))
        self.label_2.setText(_translate("Form", "Название:"))
        self.label_3.setText(_translate("Form", "Степень обжарки:"))
        self.label_4.setText(_translate("Form", "Тип кофе:"))
        self.label_5.setText(_translate("Form", "Описание:"))
        self.label_6.setText(_translate("Form", "Цена:"))
        self.label_7.setText(_translate("Form", "Объем упаковки:"))
        self.pushButton.setText(_translate("Form", "Добавить кофе"))
        self.comboBox.setItemText(0, _translate("Form", "Молотый"))
        self.comboBox.setItemText(1, _translate("Form", "В зернах"))
        self.comboBox_2.setItemText(0, _translate("Form", "Необжаренные зерна"))
        self.comboBox_2.setItemText(1, _translate("Form", "Светлая обжарка"))
        self.comboBox_2.setItemText(2, _translate("Form", "Средняя обжарка"))
        self.comboBox_2.setItemText(3, _translate("Form", "Темная обжарка"))
        self.comboBox_2.setItemText(4, _translate("Form", "Высшая обжарка"))
        self.comboBox_3.setItemText(0, _translate("Form", "125 гр"))
        self.comboBox_3.setItemText(1, _translate("Form", "250 гр"))
        self.comboBox_3.setItemText(2, _translate("Form", "500 гр"))
        self.comboBox_3.setItemText(3, _translate("Form", "1 кг"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = coffee()
    ex.show()
    sys.exit(app.exec_())
