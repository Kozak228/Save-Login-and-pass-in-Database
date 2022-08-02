from Save_log_and_pass_GUI import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from PyQt6.QtCore import Qt

from re import sub
from urllib.parse import urlparse

from BD_connect import Database
from Write_file import write_file

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_site.setReadOnly(True)
        self.ui.lineEdit_login.setReadOnly(True)
        self.ui.lineEdit_pass.setReadOnly(True) 

        self.ui.tableWidget.setColumnWidth(0, 70)
        self.ui.tableWidget.setColumnWidth(1,150)
        self.ui.tableWidget.setColumnWidth(2,150)
        self.ui.tableWidget.setColumnWidth(3,150)

        self.ui.tableWidget.clicked.connect(self.table_value)
        self.ui.pushButton_exit.clicked.connect(QApplication.instance().quit)
        self.ui.pushButton_FAQ.clicked.connect(self.FAQ_vvod)
        self.ui.pushButton_create.clicked.connect(self.create_table)
        self.ui.pushButton_drop.clicked.connect(self.drop_table)
        self.ui.pushButton_load.clicked.connect(self.load_in_BD)
        self.ui.pushButton_save_file.clicked.connect(self.save_in_file)

        self.ui.radioButton.toggled.connect(lambda: self.btn_state(self.ui.radioButton))
        self.ui.radioButton_2.toggled.connect(lambda: self.btn_state(self.ui.radioButton_2))
        self.ui.radioButton_3.toggled.connect(lambda: self.btn_state(self.ui.radioButton_3))
        self.ui.radioButton_4.toggled.connect(lambda: self.btn_state(self.ui.radioButton_4))
        self.ui.radioButton_5.toggled.connect(lambda: self.btn_state(self.ui.radioButton_5))
        self.ui.radioButton_6.toggled.connect(lambda: self.btn_state(self.ui.radioButton_6))
        self.ui.radioButton_7.toggled.connect(lambda: self.btn_state(self.ui.radioButton_7))

        self.BD = Database()
        self.load_data_in_table()

    def load_in_BD(self):
        pattr = "w{3}."

        if self.ui.radioButton.isChecked():
            self.BD = Database()
            self.load_data_in_table()

            self.ui.lineEdit_id.setText("")
            self.ui.lineEdit_site.setText("")
            self.ui.lineEdit_login.setText("")
            self.ui.lineEdit_pass.setText("")

        if self.ui.radioButton_2.isChecked():
            site = self.ui.lineEdit_site.text()

            self.ui.lineEdit_id.setText("")
            self.ui.lineEdit_login.setText("")
            self.ui.lineEdit_pass.setText("")

            if site == "":
                self.msg("Error", "Поле 'site' должно быть заполнено!")
                site_bool = False
                self.ui.lineEdit_site.setStyleSheet("border: 2px solid red;")
            else:
                f = sub(pattr, "", f)
                if f[:8] == "https://" or f[:7] == "http://":
                    f = urlparse(f).netloc

                site_bool = True
                self.ui.lineEdit_site.setStyleSheet("border: 1px solid yellow;")

            if site_bool:
                er, spis = self.BD.Select_db_in_param(site, True)

                if er == "Er":
                    if len(spis) == 0:
                        self.msg("Information", f"Записи по '{site}' отсуствуют в БД!")
                    else:
                        self.spisok_all = spis
                        self.load_in_table_with_param(self.spisok_all)
                else:
                    self.msg(er, spis)
        
        if self.ui.radioButton_3.isChecked():
            ids = self.ui.lineEdit_id.text()
            site = self.ui.lineEdit_site.text()
            login = self.ui.lineEdit_login.text()
            password = self.ui.lineEdit_pass.text()

            if ids == "":
                self.msg("Error", "Поле 'id' должно быть заполнено!")
                ids_bool = False
                self.ui.lineEdit_id.setStyleSheet("border: 2px solid red;")
            else:
                ids = int(ids)
                ids_bool = True
                self.ui.lineEdit_id.setStyleSheet("border: 1px solid yellow;")

            if site == "":
                self.msg("Error", "Поле 'site' должно быть заполнено!")
                site_bool = False
                self.ui.lineEdit_site.setStyleSheet("border: 2px solid red;")
            else:
                f = sub(pattr, "", f)
                if f[:8] == "https://" or f[:7] == "http://":
                    f = urlparse(f).netloc
                site_bool = True
                self.ui.lineEdit_site.setStyleSheet("border: 1px solid yellow;")

            if login == "":
                self.msg("Error", "Поле 'login' должно быть заполнено!")
                login_bool = False
                self.ui.lineEdit_login.setStyleSheet("border: 2px solid red;")
            else:
                login_bool = True
                self.ui.lineEdit_login.setStyleSheet("border: 1px solid yellow;")

            if password == "":
                self.msg("Error", "Поле 'password' должно быть заполнено!")
                pass_bool = False
                self.ui.lineEdit_pass.setStyleSheet("border: 2px solid red;")
            else:
                pass_bool = True
                self.ui.lineEdit_pass.setStyleSheet("border: 1px solid yellow;")

            if ids_bool and site_bool and login_bool and pass_bool:
                er, msg = self.BD.Update_bd(ids, site, login, password)
                self.msg(er, msg)

                self.BD = Database()
                self.load_data_in_table()

        if self.ui.radioButton_4.isChecked():
            ids = self.ui.lineEdit_id.text()
            login = self.ui.lineEdit_login.text()
            password = self.ui.lineEdit_pass.text()

            self.ui.lineEdit_site.setText("")

            if ids == "":
                self.msg("Error", "Поле 'id' должно быть заполнено!")
                ids_bool = False
                self.ui.lineEdit_id.setStyleSheet("border: 2px solid red;")
            else:
                ids = int(ids)
                ids_bool = True
                self.ui.lineEdit_id.setStyleSheet("border: 1px solid yellow;")

            if login == "":
                self.msg("Error", "Поле 'login' должно быть заполнено!")
                login_bool = False
                self.ui.lineEdit_login.setStyleSheet("border: 2px solid red;")
            else:
                login_bool = True
                self.ui.lineEdit_login.setStyleSheet("border: 1px solid yellow;")

            if password == "":
                self.msg("Error", "Поле 'password' должно быть заполнено!")
                pass_bool = False
                self.ui.lineEdit_pass.setStyleSheet("border: 2px solid red;")
            else:
                pass_bool = True
                self.ui.lineEdit_pass.setStyleSheet("border: 1px solid yellow;")

            if ids_bool and login_bool and pass_bool:
                er, msg = self.BD.Update_bd_in_param(ids, login, password)
                self.msg(er, msg)

                self.BD = Database()
                self.load_data_in_table()

        if self.ui.radioButton_5.isChecked():
            site = self.ui.lineEdit_site.text()
            login = self.ui.lineEdit_login.text()
            password = self.ui.lineEdit_pass.text()

            self.ui.lineEdit_id.setText("")

            if site == "":
                self.msg("Error", "Поле 'site' должно быть заполнено!")
                site_bool = False
                self.ui.lineEdit_site.setStyleSheet("border: 2px solid red;")
            else:
                f = sub(pattr, "", f)
                if f[:8] == "https://" or f[:7] == "http://":
                    f = urlparse(f).netloc

                site_bool = True
                self.ui.lineEdit_site.setStyleSheet("border: 1px solid yellow;")

            if login == "":
                self.msg("Error", "Поле 'login' должно быть заполнено!")
                login_bool = False
                self.ui.lineEdit_login.setStyleSheet("border: 2px solid red;")
            else:
                login_bool = True
                self.ui.lineEdit_login.setStyleSheet("border: 1px solid yellow;")

            if password == "":
                self.msg("Error", "Поле 'password' должно быть заполнено!")
                pass_bool = False
                self.ui.lineEdit_pass.setStyleSheet("border: 2px solid red;")
            else:
                pass_bool = True
                self.ui.lineEdit_pass.setStyleSheet("border: 1px solid yellow;")

            if site_bool and login_bool and pass_bool:
                er, msg = self.BD.Insert_in_BD(site, login, password)
                self.msg(er, msg)

                self.BD = Database()
                self.load_data_in_table()

        if self.ui.radioButton_6.isChecked():
            ids = self.ui.lineEdit_id.text()

            self.ui.lineEdit_site.setText("")
            self.ui.lineEdit_login.setText("")
            self.ui.lineEdit_pass.setText("")

            if ids == "":
                self.msg("Error", "Поле 'id' должно быть заполнено!")
                ids_bool = False
                self.ui.lineEdit_id.setStyleSheet("border: 2px solid red;")
            else:
                ids_bool = True
                self.ui.lineEdit_id.setStyleSheet("border: 1px solid yellow;")
                ids = int(ids)
                
            if ids_bool:
                er, msg = self.BD.Remove_row(ids)
                self.msg(er, msg)

                self.BD = Database()
                self.load_data_in_table()

        if self.ui.radioButton_7.isChecked():
            login = self.ui.lineEdit_login.text()

            self.ui.lineEdit_id.setText("")
            self.ui.lineEdit_site.setText("")
            self.ui.lineEdit_pass.setText("")

            if login == "":
                self.msg("Error", "Поле 'login' должно быть заполнено!")
                login_bool = False
                self.ui.lineEdit_login.setStyleSheet("border: 2px solid red;")
            else:
                login_bool = True
                self.ui.lineEdit_login.setStyleSheet("border: 1px solid yellow;")

            if login_bool:
                er, spis = self.BD.Select_db_in_param(login, False)

                if er == "Er":
                    if len(spis) == 0:
                        self.msg("Information", f"Записи по '{login}' отсуствуют в БД!")
                    else:
                        self.spisok_all = spis
                        self.load_in_table_with_param(self.spisok_all)
                else:
                    self.msg(er, spis)

    def btn_state(self, b):
        if b.isChecked() and b.objectName() == "radioButton":
            self.ui.lineEdit_id.setStyleSheet("border: 1px solid yellow;")
            self.ui.lineEdit_site.setStyleSheet("border: 1px solid yellow;")
            self.ui.lineEdit_login.setStyleSheet("border: 1px solid yellow;")
            self.ui.lineEdit_pass.setStyleSheet("border: 1px solid yellow;")
            
            self.ui.lineEdit_site.setReadOnly(True)
            self.ui.lineEdit_login.setReadOnly(True)
            self.ui.lineEdit_pass.setReadOnly(True)    

        if b.isChecked() and b.objectName() == "radioButton_2":
            self.ui.lineEdit_id.setStyleSheet("border: 1px solid yellow;")
            self.ui.lineEdit_site.setStyleSheet("border: 2px solid green;")
            self.ui.lineEdit_login.setStyleSheet("border: 1px solid yellow;")
            self.ui.lineEdit_pass.setStyleSheet("border: 1px solid yellow;")

            self.ui.lineEdit_site.setReadOnly(False)
            self.ui.lineEdit_login.setReadOnly(True)
            self.ui.lineEdit_pass.setReadOnly(True)

        if b.isChecked() and b.objectName() == "radioButton_3":
            self.ui.lineEdit_id.setStyleSheet("border: 2px solid green;")
            self.ui.lineEdit_site.setStyleSheet("border: 2px solid green;")
            self.ui.lineEdit_login.setStyleSheet("border: 2px solid green;")
            self.ui.lineEdit_pass.setStyleSheet("border: 2px solid green;")

            self.ui.lineEdit_site.setReadOnly(False)
            self.ui.lineEdit_login.setReadOnly(False)
            self.ui.lineEdit_pass.setReadOnly(False)

        if b.isChecked() and b.objectName() == "radioButton_4":
            self.ui.lineEdit_id.setStyleSheet("border: 2px solid green;")
            self.ui.lineEdit_site.setStyleSheet("border: none")
            self.ui.lineEdit_login.setStyleSheet("border: 2px solid green;")
            self.ui.lineEdit_pass.setStyleSheet("border: 2px solid green;")

            self.ui.lineEdit_site.setReadOnly(True)
            self.ui.lineEdit_login.setReadOnly(False)
            self.ui.lineEdit_pass.setReadOnly(False)
        
        if b.isChecked() and b.objectName() == "radioButton_5":
            self.ui.lineEdit_id.setStyleSheet("border: 1px solid yellow;")
            self.ui.lineEdit_site.setStyleSheet("border: 2px solid green;")
            self.ui.lineEdit_login.setStyleSheet("border: 2px solid green;")
            self.ui.lineEdit_pass.setStyleSheet("border: 2px solid green;")

            self.ui.lineEdit_site.setReadOnly(False)
            self.ui.lineEdit_login.setReadOnly(False)
            self.ui.lineEdit_pass.setReadOnly(False)
            
        if b.isChecked() and b.objectName() == "radioButton_6":
            self.ui.lineEdit_id.setStyleSheet("border: 2px solid green;")
            self.ui.lineEdit_site.setStyleSheet("border: 1px solid yellow;")
            self.ui.lineEdit_login.setStyleSheet("border: 1px solid yellow;")
            self.ui.lineEdit_pass.setStyleSheet("border: 1px solid yellow;")

            self.ui.lineEdit_site.setReadOnly(True)
            self.ui.lineEdit_login.setReadOnly(True)
            self.ui.lineEdit_pass.setReadOnly(True)

        if b.isChecked() and b.objectName() == "radioButton_7":
            self.ui.lineEdit_id.setStyleSheet("border: 1px solid yellow;")
            self.ui.lineEdit_site.setStyleSheet("border: 1px solid yellow;")
            self.ui.lineEdit_login.setStyleSheet("border: 2px solid green;")
            self.ui.lineEdit_pass.setStyleSheet("border: 1px solid yellow;")

            self.ui.lineEdit_site.setReadOnly(True)
            self.ui.lineEdit_login.setReadOnly(False)
            self.ui.lineEdit_pass.setReadOnly(True)

    def load_in_table_with_param(self, spis):
        self.ui.tableWidget.setRowCount(len(spis))
            
        for i in range(len(spis)):
            for j in range(len(spis[i])):
                    item = QTableWidgetItem(str(spis[i][j]))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
                    self.ui.tableWidget.setItem(i, j, item)

    def save_in_file(self):
        filename = self.ui.lineEdit_file_name.text()

        if filename == "":
            self.msg("Error", "Поле для ввода имени файла должно быть заполнено!")
        else:
            filename = filename[:filename.find(".")] if filename.find(".") != -1 else filename

            reson, msg = write_file(self.spisok_all, filename)
            self.msg(reson, msg)

    def table_value(self):
        for i in self.ui.tableWidget.selectedItems():
            if i.column() == 0:
                self.ui.lineEdit_id.setText(i.text())
            if i.column() == 1:
                self.ui.lineEdit_site.setText(i.text())
            if i.column() == 2:
                self.ui.lineEdit_login.setText(i.text())
            if i.column() == 3:
                self.ui.lineEdit_pass.setText(i.text())            

    def create_table(self):
        reson, msg = self.BD.create_database()
        self.msg(reson, msg)

    def drop_table(self):
        reson, msg = self.BD.drop_database()
        self.msg(reson, msg)

    def load_data_in_table(self):
        reson, msg = self.BD.Select_db()

        if reson == "Error":
            self.msg(reson, msg)
        else:
            self.spisok_all, kol_rows_vyb, = self.BD.ret_data()
    
            self.ui.tableWidget.setRowCount(kol_rows_vyb)
            
            for i in range(len(self.spisok_all)):
                for j in range(len(self.spisok_all[i])):
                        item = QTableWidgetItem(str(self.spisok_all[i][j]))
                        item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
                        self.ui.tableWidget.setItem(i, j, item)

    def FAQ_vvod(self):
        self.msg("Information", "Для заполения полей, вам требуеться:\nПоле 'id' - нажать на соотвествующий столбец таблицы.\nПоле 'Site' - вставить ссылку с адресной строки браузера или нажать на соотвествующий столбец таблицы.\nДля заполнения остальных полей ввод вручную или нажать на соотвествующие столбцы таблицы.\nВ поля, которые нужно заполнить, подсветятся зелёным цветом.")

    def msg(self, reson, message):
        msg = QMessageBox()
        if reson == "Error": 
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

        if reson == "Information" or reson == "Uptate":
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()