# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.search = QtWidgets.QPushButton(Form)
        self.search.setObjectName("search")
        self.verticalLayout.addWidget(self.search)
        self.search.clicked.connect(self.searchfunc)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.update = QtWidgets.QPushButton(Form)
        self.update.setObjectName("update")
        self.verticalLayout.addWidget(self.update)
        self.update.clicked.connect(self.updatefunc)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.insert = QtWidgets.QPushButton(Form)
        self.insert.setObjectName("insert")
        self.verticalLayout.addWidget(self.insert)
        self.insert.clicked.connect(self.insertfunc)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.delete_2 = QtWidgets.QPushButton(Form)
        self.delete_2.setObjectName("delete_2")
        self.verticalLayout.addWidget(self.delete_2)
        self.delete_2.clicked.connect(self.deletefunc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "C.R.U.D Directory"))
        self.search.setText(_translate("Form", "Search"))
        self.update.setText(_translate("Form", "Update"))
        self.insert.setText(_translate("Form", "Insert"))
        self.delete_2.setText(_translate("Form", "Delete"))

    def searchfunc(self):
        from screen2 import Ui_Form
        Dialog = QtWidgets.QDialog()
        ui = Ui_Form()
        ui.setupUi(Dialog)
        ret = Dialog.exec()

    def updatefunc(self):
        from updation import Ui_Form
        Dialog = QtWidgets.QDialog()
        ui = Ui_Form()
        ui.setupUi(Dialog)
        ret = Dialog.exec()

    def insertfunc(self):
        from addgui import Ui_Form
        Dialog = QtWidgets.QDialog()
        ui = Ui_Form()
        ui.setupUi(Dialog)
        ret = Dialog.exec()

    def deletefunc(self):
        from deleted import Ui_Form
        Dialog = QtWidgets.QDialog()
        ui = Ui_Form()
        ui.setupUi(Dialog)
        ret = Dialog.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
