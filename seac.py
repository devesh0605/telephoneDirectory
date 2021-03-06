# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seaf.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 604)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.sef = QtWidgets.QLineEdit(Form)
        self.sef.setObjectName("sef")
        self.verticalLayout.addWidget(self.sef)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.display)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fn = QtWidgets.QPlainTextEdit(Form)
        self.fn.setReadOnly(True)
        self.fn.setObjectName("fn")
        self.horizontalLayout_2.addWidget(self.fn)
        self.ln = QtWidgets.QPlainTextEdit(Form)
        self.ln.setReadOnly(True)
        self.ln.setObjectName("ln")
        self.horizontalLayout_2.addWidget(self.ln)
        self.co = QtWidgets.QPlainTextEdit(Form)
        self.co.setReadOnly(True)
        self.co.setObjectName("co")
        self.horizontalLayout_2.addWidget(self.co)
        self.ad = QtWidgets.QPlainTextEdit(Form)
        self.ad.setReadOnly(True)
        self.ad.setObjectName("ad")
        self.horizontalLayout_2.addWidget(self.ad)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                                                          Search by Contact Number"))
        self.sef.setPlaceholderText(_translate("Form", "Enter contact number"))
        self.pushButton.setText(_translate("Form", "Search"))
        self.label_4.setText(_translate("Form", "        First Name"))
        self.label_3.setText(_translate("Form", "       Last Name"))
        self.label_2.setText(_translate("Form", "         Contact"))
        self.label_5.setText(_translate("Form", "         Address"))

    def display(self):
        x=self.sef.text()
        if x.isnumeric():
            import retrieve
            if retrieve.bycontact(x) == 0:
                self.fn.setPlainText('Sorry')
                self.ln.setPlainText('No')
                self.co.setPlainText('Entries')
                self.ad.setPlainText('Found')
            else:
                self.fn.setPlainText(retrieve.bycontact(x)[0])
                self.ln.setPlainText(retrieve.bycontact(x)[1])
                self.co.setPlainText(retrieve.bycontact(x)[2])
                self.ad.setPlainText(retrieve.bycontact(x)[3])
        else:
            self.fn.setPlainText('Enter')
            self.ln.setPlainText('Valid')
            self.co.setPlainText('Contact')
            self.ad.setPlainText('Number')








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
