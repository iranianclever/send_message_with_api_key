# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from send_message import SendMessage


class Ui_MainWindow(object):
    """ Qt5 create widget elements """

    def __init__(self):
        """ Initialization """
        # Create object from send message class
        self.send_message = SendMessage()
        # get api key
        self.api_key = self.send_message.API_key
        # New api key from input
        self.new_api_key = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 20))
        self.label.setObjectName("label")
        self.api_key_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.api_key_line_edit.setGeometry(QtCore.QRect(10, 40, 781, 26))
        self.api_key_line_edit.setObjectName("api_key_line_edit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(17, 80, 771, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(537, 120, 251, 20))
        self.label_3.setObjectName("label_3")
        self.name_contact_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_contact_line_edit.setGeometry(
            QtCore.QRect(532, 150, 261, 26))
        self.name_contact_line_edit.setObjectName("name_contact_line_edit")
        # Set alignment (Direction, right to left)
        self.name_contact_line_edit.setAlignment(QtCore.Qt.AlignRight)
        self.number_contact_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.number_contact_line_edit.setGeometry(
            QtCore.QRect(240, 150, 261, 26))
        self.number_contact_line_edit.setObjectName("number_contact_line_edit")
        # Set alignment (Direction, right to left)
        self.number_contact_line_edit.setAlignment(QtCore.Qt.AlignRight)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(245, 120, 251, 20))
        self.label_4.setObjectName("label_4")
        self.save_contact_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.save_contact_radio.setGeometry(QtCore.QRect(680, 190, 108, 22))
        self.save_contact_radio.setChecked(True)
        self.save_contact_radio.setObjectName("save_contact_radio")
        self.modify_contact_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.modify_contact_radio.setGeometry(QtCore.QRect(530, 190, 108, 22))
        self.modify_contact_radio.setObjectName("modify_contact_radio")
        self.remove_contact_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.remove_contact_radio.setGeometry(QtCore.QRect(370, 190, 108, 22))
        self.remove_contact_radio.setObjectName("remove_contact_radio")
        self.ok_contact_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_contact_button.setGeometry(QtCore.QRect(640, 230, 151, 26))
        self.ok_contact_button.setObjectName("ok_contact_button")
        self.clear_contact_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_contact_button.setGeometry(QtCore.QRect(510, 230, 121, 26))
        self.clear_contact_button.setObjectName("clear_contact_button")
        self.list_contact_list_view = QtWidgets.QListView(self.centralwidget)
        self.list_contact_list_view.setGeometry(
            QtCore.QRect(465, 300, 331, 251))
        self.list_contact_list_view.setObjectName("list_contact_list_view")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 270, 321, 20))
        self.label_5.setObjectName("label_5")
        self.message_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.message_text_edit.setGeometry(QtCore.QRect(10, 300, 391, 111))
        self.message_text_edit.setObjectName("message_text_edit")
        # Set alignment (Direction, right to left)
        self.message_text_edit.setAlignment(QtCore.Qt.AlignRight)
        self.send_message_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_message_button.setGeometry(QtCore.QRect(10, 420, 391, 31))
        self.send_message_button.setObjectName("send_message_button")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 340, 51, 18))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 350, 51, 18))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 360, 51, 18))
        self.label_8.setObjectName("label_8")
        self.log_list_view = QtWidgets.QListView(self.centralwidget)
        self.log_list_view.setGeometry(QtCore.QRect(10, 490, 391, 61))
        self.log_list_view.setObjectName("log_list_view")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 270, 391, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 460, 391, 20))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Set api key to input
        self.api_key_line_edit.setText(self.api_key)

        # Create model for list view contact
        self.model = QtGui.QStandardItemModel()
        self.list_contact_list_view.setModel(self.model)

        # Create model for list view log
        self.model_log = QtGui.QStandardItemModel()
        self.log_list_view.setModel(self.model_log)

        self.retranslateUi(MainWindow)
        self.ok_contact_button.clicked.connect(self.action_contact)
        self.clear_contact_button.clicked.connect(self.clear_inputs)
        self.send_message_button.clicked.connect(self.send)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.list_contact_show()

    def send(self):
        """ Sending message """
        # Get api key from file
        api_file = self.send_message.get_api_key()
        # Get api key from input
        api_input = self.api_key_line_edit.text()

        # Check api key is none or no
        if self.send_message.API_key == None or api_file != api_input:
            # Replace new api key to file use this
            self.send_message.save_api_key(api_input)

        # Get message from text edit message
        message = self.message_text_edit.toPlainText()
        # Sending message
        status = self.send_message.send(message)

        # Append log to view list
        for state, log in status.items():
            # Concat state and log
            state_log = '{} {}'.format(state, log)
            # Convert type of state_log
            item = QtGui.QStandardItem(state_log)
            # Set log to item
            self.model_log.appendRow(item)

    def list_contact_show(self):
        """ Set list contact numbers """
        # Clear list view contact
        self.model.clear()
        # Return persons to persons
        persons = self.send_message.return_persons()
        # Iterating from person, name and number
        for name, number in persons.items():
            # Concat name and number to one string
            name_number = '{} {}'.format(name, number)
            # Convert type of name
            item = QtGui.QStandardItem(name_number)
            # Set name item
            self.model.appendRow(item)


    def action_contact(self):
        """ Save, modify, remove contact """

        # Check save status of contact number
        if self.save_contact_radio.isChecked():
            name = self.name_contact_line_edit.text()
            number = self.number_contact_line_edit.text()
            self.send_message.add_number(name, number)

        # Check modifying status
        elif self.modify_contact_radio.isChecked():
            name = self.name_contact_line_edit.text()
            number = self.number_contact_line_edit.text()
            self.send_message.modify_number(name, number)

        # Check remove status
        elif self.remove_contact_radio.isChecked():
            name = self.name_contact_line_edit.text()
            self.send_message.remove_number(name)

        # Add change to list view contact
        self.list_contact_show()

        # Clear inputs
        self.clear_inputs()

    def clear_inputs(self):
        """ Clears inputs """
        self.name_contact_line_edit.setText('')
        self.number_contact_line_edit.setText('')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "آبتین | ارسال پیامک"))
        self.label.setText(_translate("MainWindow", "API Key"))
        self.label_2.setText(_translate(
            "MainWindow", "اطلاعات افراد جهت ارسال پیامک"))
        self.label_3.setText(_translate("MainWindow", "نام مخاطب"))
        self.label_4.setText(_translate("MainWindow", "شماره مخاطب"))
        self.save_contact_radio.setText(
            _translate("MainWindow", "ذخیره مخاطب"))
        self.modify_contact_radio.setText(
            _translate("MainWindow", "اصلاح کردن"))
        self.remove_contact_radio.setText(
            _translate("MainWindow", "حذف مخاطب"))
        self.ok_contact_button.setText(_translate("MainWindow", "اعمال کردن"))
        self.clear_contact_button.setText(
            _translate("MainWindow", "خالی کردن"))
        self.label_5.setText(_translate("MainWindow", "لیست مخاطبین"))
        self.send_message_button.setText(
            _translate("MainWindow", "ارسال پیام"))
        self.label_6.setText(_translate("MainWindow", "-------->>"))
        self.label_7.setText(_translate("MainWindow", "-------->>"))
        self.label_8.setText(_translate("MainWindow", "-------->>"))
        self.label_9.setText(_translate("MainWindow", "متن پیام"))
        self.label_10.setText(_translate(
            "MainWindow", "گزارش پیام های ارسالی"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
