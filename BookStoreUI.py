# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookStoreUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from BookStore import Book, Inventory, Cart
import openpyxl


class Ui_MainWindow(object):

    def fillTable(self):
        self.tableWidget.setRowCount(cart.amount_of_books)
        self.tableWidget.setColumnCount(len(cart.books[0].data))

        for row in range(self.tableWidget.rowCount()):
            book = cart.books[row]
            for col in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(
                    row, col, QtWidgets.QTableWidgetItem(book.data[col]))

    def addItemsToComboBoxes(self):
        if cart.allIsbns() != []:
            self.searchIsbnBox.addItems(cart.allIsbns())
            self.searchBookBox.addItems(cart.allBookNames())
            self.searchAuthorBox.addItems(cart.allAuthors())
            self.searchPublisherBox.addItems(cart.allPublishers())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 747)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1061, 741))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.searchGroupBox.setObjectName("searchGroupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.searchGroupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 511, 711))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 3)
        self.searchIsbnBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.searchIsbnBox.setObjectName("searchIsbnBox")
        self.gridLayout.addWidget(self.searchIsbnBox, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.searchAuthorBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.searchAuthorBox.setObjectName("searchAuthorBox")
        self.gridLayout.addWidget(self.searchAuthorBox, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.searchBookBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.searchBookBox.setObjectName("searchBookBox")
        self.gridLayout.addWidget(self.searchBookBox, 1, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.searchPublisherBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.searchPublisherBox.setObjectName("searchPublisherBox")
        self.gridLayout.addWidget(self.searchPublisherBox, 3, 1, 1, 2)
        self.searchButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 4, 1, 1, 1)
        self.horizontalLayout.addWidget(self.searchGroupBox)
        self.billingGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.billingGroupBox.setObjectName("billingGroupBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.billingGroupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 511, 711))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkoutButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.checkoutButton.setStyleSheet(
            "background-color: rgb(154, 154, 154);color: rgb(255, 255, 255);")
        self.checkoutButton.setObjectName("checkoutButton")
        self.gridLayout_2.addWidget(self.checkoutButton, 17, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 1, 1, 1)
        self.billingTotalBox = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.billingTotalBox.setReadOnly(True)
        self.billingTotalBox.setObjectName("billingTotalBox")
        self.gridLayout_2.addWidget(self.billingTotalBox, 6, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 1, 1, 1)
        self.billingIsbnBox = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.billingIsbnBox.setObjectName("billingIsbnBox")
        self.gridLayout_2.addWidget(self.billingIsbnBox, 4, 2, 1, 1)
        self.addToCartButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.addToCartButton.setObjectName("addToCartButton")
        self.gridLayout_2.addWidget(self.addToCartButton, 14, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.removeFromCartButton = QtWidgets.QPushButton(
            self.gridLayoutWidget_2)
        self.removeFromCartButton.setObjectName("removeFromCartButton")
        self.gridLayout_2.addWidget(self.removeFromCartButton, 15, 1, 1, 2)
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 18, 1)
        self.billingNameOfRecipientBox = QtWidgets.QLineEdit(
            self.gridLayoutWidget_2)
        self.billingNameOfRecipientBox.setObjectName(
            "billingNameOfRecipientBox")
        self.gridLayout_2.addWidget(self.billingNameOfRecipientBox, 2, 2, 1, 1)
        self.clearCartButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.clearCartButton.setObjectName("clearCartButton")
        self.gridLayout_2.addWidget(self.clearCartButton, 16, 1, 1, 2)
        self.bill_id_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bill_id_label.setObjectName("bill_id_label")
        self.gridLayout_2.addWidget(self.bill_id_label, 0, 1, 1, 1)
        self.billingIdBox = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.billingIdBox.setReadOnly(True)
        self.billingIdBox.setObjectName("billingIdBox")
        self.gridLayout_2.addWidget(self.billingIdBox, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.billingGroupBox)
# Dev Added Funcitons
        self.addItemsToComboBoxes()
        self.fillTable()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchGroupBox.setTitle(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "ISBN: "))
        self.label_3.setText(_translate("MainWindow", "Author:"))
        self.label_2.setText(_translate("MainWindow", "Book:"))
        self.label_4.setText(_translate("MainWindow", "Publisher:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.billingGroupBox.setTitle(_translate("MainWindow", "Billing"))
        self.checkoutButton.setText(_translate("MainWindow", "Checkout"))
        self.label_6.setText(_translate("MainWindow", "ISBN:"))
        self.label_7.setText(_translate("MainWindow", "Total:"))
        self.addToCartButton.setText(_translate("MainWindow", "Add To Cart"))
        self.label_5.setText(_translate("MainWindow", "Name of Recipient:"))
        self.removeFromCartButton.setText(
            _translate("MainWindow", "Remove From Cart"))
        self.clearCartButton.setText(_translate("MainWindow", "Clear Cart"))
        self.bill_id_label.setText(_translate("MainWindow", "Bill Id: "))


if __name__ == "__main__":
    import sys
# XL Connection

# BookStore Object Creation
    cart = Cart()
    cart.getInventory()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
# Saving Changes
    cart.updateInventory()

    sys.exit(app.exec_())
