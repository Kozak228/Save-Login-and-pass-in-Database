# Form implementation generated from reading ui file 'Save_log_and_pass.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 554)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("фото/2906274.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: #A9A9A9;\n"
"}\n"
"QPushButton{\n"
"    background-color: black;\n"
"    color: yellow;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px dashed #00FA9A;\n"
"    color: #00FA9A;\n"
"}\n"
"QLineEdit{\n"
"    background-color: #DCDCDC;\n"
"    color:     #000080;\n"
"    border: 1px solid yellow; \n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px dashed #00FA9A;\n"
"}\n"
"QLabel{\n"
"    color: #FF4500;\n"
"}\n"
"QGroupBox{\n"
"    backgrond-color: #696969;\n"
"    color: #FF4500;\n"
"    border: 1px solid #0000CD;\n"
"}\n"
"QRadioButton{\n"
"    color: #FF4500;\n"
"}\n"
"QRadioButton:hover{\n"
"    color: #00FF00;\n"
"}\n"
"QTableWidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 black, stop:1 blue);\n"
"    border: 2px solid #FF4500;\n"
"    color: yellow;\n"
"}\n"
"QTableWidget::item {\n"
"    border: 5px solid rgba(68, 119, 170, 150);\n"
"    background-color:rgba(68, 119, 170, 125);\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section {\n"
"    background-color: rgba(128, 128, 128, 128);\n"
"}\n"
"QTableWidget::item:hover {\n"
"    border: 2px dashed #00FA9A;\n"
"    color: #00FA9A;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 531, 351))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(670, 510, 91, 31))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_FAQ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_FAQ.setGeometry(QtCore.QRect(190, 450, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_FAQ.setFont(font)
        self.pushButton_FAQ.setObjectName("pushButton_FAQ")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(550, 170, 221, 191))
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 100, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setChecked(False)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 60, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setChecked(False)
        self.radioButton_7.setObjectName("radioButton_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 370, 291, 181))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_pass.setGeometry(QtCore.QRect(40, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_pass.setFont(font)
        self.lineEdit_pass.setText("")
        self.lineEdit_pass.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.lineEdit_login = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_login.setGeometry(QtCore.QRect(40, 100, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setText("")
        self.lineEdit_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_id = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_id.setGeometry(QtCore.QRect(40, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setText("")
        self.lineEdit_id.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_id.setReadOnly(True)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_site = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_site.setGeometry(QtCore.QRect(40, 60, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_site.setFont(font)
        self.lineEdit_site.setText("")
        self.lineEdit_site.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_site.setObjectName("lineEdit_site")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_clear.setGeometry(QtCore.QRect(160, 20, 121, 31))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(550, 10, 221, 141))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_file_name = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_file_name.setGeometry(QtCore.QRect(10, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_file_name.setFont(font)
        self.lineEdit_file_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_file_name.setPlaceholderText("")
        self.lineEdit_file_name.setObjectName("lineEdit_file_name")
        self.pushButton_save_file = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_save_file.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.pushButton_save_file.setObjectName("pushButton_save_file")
        self.pushButton_clear_save_file_ = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_clear_save_file_.setGeometry(QtCore.QRect(120, 100, 91, 31))
        self.pushButton_clear_save_file_.setObjectName("pushButton_clear_save_file_")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 370, 141, 141))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_load = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_load.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_create = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_create.setGeometry(QtCore.QRect(10, 60, 121, 31))
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_drop = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_drop.setGeometry(QtCore.QRect(10, 100, 121, 31))
        self.pushButton_drop.setObjectName("pushButton_drop")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_clear.clicked.connect(self.lineEdit_id.clear) # type: ignore
        self.pushButton_clear.clicked.connect(self.lineEdit_site.clear) # type: ignore
        self.pushButton_clear.clicked.connect(self.lineEdit_login.clear) # type: ignore
        self.pushButton_clear.clicked.connect(self.lineEdit_pass.clear) # type: ignore
        self.pushButton_clear_save_file_.clicked.connect(self.lineEdit_file_name.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сохранение логина и пароля"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Site"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Login"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выйти"))
        self.pushButton_FAQ.setText(_translate("MainWindow", "?"))
        self.groupBox.setTitle(_translate("MainWindow", "Выбор функции"))
        self.radioButton.setText(_translate("MainWindow", "Показать все данные"))
        self.radioButton_2.setText(_translate("MainWindow", "Показать данные по сайту"))
        self.radioButton_5.setText(_translate("MainWindow", "Добавить новые данные"))
        self.radioButton_3.setText(_translate("MainWindow", "Обновить определённую\n"
"строку таблицы"))
        self.radioButton_4.setText(_translate("MainWindow", "Обновить логин и пароль"))
        self.radioButton_6.setText(_translate("MainWindow", "Удалить определённую\n"
"строку данных"))
        self.radioButton_7.setText(_translate("MainWindow", "Показать данные по логину"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ввод или выбор данных"))
        self.label_4.setText(_translate("MainWindow", "Site"))
        self.lineEdit_pass.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_login.setPlaceholderText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Id"))
        self.lineEdit_id.setPlaceholderText(_translate("MainWindow", "№"))
        self.label_2.setText(_translate("MainWindow", "Pass"))
        self.lineEdit_site.setPlaceholderText(_translate("MainWindow", "Site"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.pushButton_clear.setText(_translate("MainWindow", "Очистить поля"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Запись в файл данных таблицы"))
        self.label_5.setText(_translate("MainWindow", "Название файла без\n"
"расширения"))
        self.lineEdit_file_name.setText(_translate("MainWindow", "Save_datas_site_log_pass"))
        self.pushButton_save_file.setText(_translate("MainWindow", "Сохранить в файл"))
        self.pushButton_clear_save_file_.setText(_translate("MainWindow", "Очистить поле"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Действия в БД"))
        self.pushButton_load.setText(_translate("MainWindow", "Сделать запрос "))
        self.pushButton_create.setText(_translate("MainWindow", "Создать таблицу"))
        self.pushButton_drop.setText(_translate("MainWindow", "Удвлить таблицу"))
