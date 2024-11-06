import datetime
import sqlite3
import sys

import pymorphy3
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox, QTableWidgetItem, \
    QPlainTextEdit, QPushButton, QLabel

from form_pys import choose_number_people, dialog_change_profile, hotel_description
from form_pys import list_hotels, log_in, main_window, profile, register, calendar_dialog, confirm_booking

DESCRIPTIONS_ROOM = {'Стандартный номер': 'Уютный и комфортабельный стандартный номер с удобной мебелью и современной'
                                          ' техникой. Идеально подходит для тех, кто ищет простое и доступное жильё на '
                                          'время поездки.',
                     'Номер "Комфорт"': 'Просторный номер «Комфорт» оснащён всем необходимым для приятного отдыха.'
                                        ' Удобная мебель, современная техника и дополнительные удобства создадут '
                                        'атмосферу уюта и спокойствия.',
                     'Семейный номер': 'Семейный номер идеально подходит для путешественников с детьми. В номере есть '
                                       'всё необходимое для комфортного проживания: удобная мебель, '
                                       'современная техника, а также дополнительные спальные места.',
                     'Стандарт люкс': 'Роскошный люкс с изысканным дизайном и элегантной обстановкой.'
                                      ' Просторный номер оснащён всеми современными удобствами для комфортного'
                                      ' отдыха и работы.',
                     'Семейный люкс': 'Элегантный семейный люкс с просторной планировкой и изысканной обстановкой. '
                                      'Номер оснащён всеми необходимыми удобствами для семейного отдыха, включая '
                                      'дополнительные спальные места и современную технику.'}

DATA = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop', 'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk',
        'jkl', 'zxc', 'xcv', 'cvb', 'vbn', 'bnm', 'йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх', 'зхъ',
        'зхъ', 'фыв', 'ыва',
        'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ', 'ячс', 'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю', 'жэё']

MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'декабря']

CURRENT_USER_ID = -1


def check_phone(phone):
    phone = ''.join(phone)
    if len([elem for elem in phone if elem.isdigit()]) != 11:
        return 'Неверная длина номера'

    if phone[0] == '8':
        phone = '+7' + phone[1:]

    if phone.find('(') != -1:
        if phone.find(')') == -1:
            return 'Неверный формат номера'
        if phone.count('(') != 1 or phone.count(')') != 1:
            return 'Неверный формат номера'

        if phone.index('(') < phone.index(')'):
            phone = phone.replace('(', '').replace(')', '')
        else:
            return 'Неверный формат номера'
    else:
        if phone.find(')') != -1:
            return 'Неверный формат номера'
    if phone[-1] != '-' and all(phone.split('-')):
        return 'OK'
    return 'Неверный формат номера'


def need_form_word(number, word):
    morph = pymorphy3.MorphAnalyzer()
    return str(morph.parse(word)[0].make_agree_with_number(number).word)


def check_password(passw):
    while True:
        if len(passw) > 8:
            if any(elem.isupper() for elem in passw) and any(elem.islower() for elem in passw):
                if any(elem.isdigit() for elem in passw):
                    if not any(elem in passw.lower() for elem in DATA):
                        return 'OK'
                    else:
                        return 'Пароль слишком простой'
                else:
                    return 'В пароле должна быть хотя бы 1 цифры'
            else:
                return 'Символы должны быть разных регистров'
        else:
            return 'Длина пароля должна быть больше 8 символов'


class Log_in_wndw(QMainWindow, log_in.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect('users.db')
        self.log_in_btn.clicked.connect(self.run)
        self.register_btn.clicked.connect(self.regist)

    def run(self):
        global CURRENT_USER_ID
        if self.edit_login.text() != '' and self.edit_passw.text() != '':
            cur = self.db.cursor()
            result = cur.execute('SELECT login, password, user_id FROM users').fetchall()
            for elem in result:
                if self.edit_login.text() == elem[0] and self.edit_passw.text() == elem[1]:
                    CURRENT_USER_ID = elem[-1]
                    self.w = main_wndw()
                    self.w.show()
                    self.close()
            self.label_2.setText('Такой пользователь не зарегистрирован')
        else:
            self.label_2.setText('Введите логин и пароль в поля для ввода')

    def regist(self):
        self.w = reg()
        self.w.show()


class reg(QWidget, register.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.confirm_register)
        self.db = sqlite3.connect('users.db')

    def check_name(self):
        if self.name_edit.text() != '' or self.name_edit.text().replace(' ', '') != '':
            if len(self.name_edit.text()) >= 3:
                return 'OK'
            else:
                return 'Имя слишком короткое'
        else:
            return 'Имя должно состоять из букв или цифр'

    def check_passw(self):
        if len(self.psw_edit.text()) > 8:
            if any(elem.isupper() for elem in self.psw_edit.text()) and any(
                    elem.islower() for elem in self.psw_edit.text()):
                if any(elem.isdigit() for elem in self.psw_edit.text()):
                    if not any(elem in self.psw_edit.text().lower() for elem in DATA):
                        return 'OK'
                    else:
                        return 'Пароль слишком простой'
                else:
                    return 'В пароле должна быть хотя бы 1 цифры'
            else:
                return 'Символы должны быть разных регистров'
        else:
            return 'Длина пароля должна быть больше 8 символов'

    def check_mail(self):
        if '@' in self.email_edit.text():
            return 'OK'
        else:
            return 'Пароль должен содержать "@"'

    def check_similar(self):
        cur = self.db.cursor()
        all_data = cur.execute('SELECT login, password, email, phone FROM users').fetchall()
        for elem in all_data:
            if self.name_edit.text() == elem[0]:
                return 'Пользователь с таким именем уже зарегистрирован'
            if self.psw_edit.text() == elem[1]:
                return 'Пользователь с таким паролем уже зарегистрирован'
            if self.email_edit.text() == elem[2]:
                return 'Пользователь с такой почтой уже зарегистрирован'
            if self.phone_edit.text() == elem[3]:
                return 'Пользователь с таким номером телефона уже зарегистрирован'
            else:
                return 'OK'

    def confirm_register(self):
        checks = [self.check_name(), self.check_passw(), self.check_mail(), check_phone(self.phone_edit.text())]
        check_db = self.check_similar()
        if all(map(lambda x: x == 'OK', checks)) and check_db == 'OK':
            cur = self.db.cursor()
            id = len(cur.execute('SELECT * from USERS').fetchall()) + 1
            cur.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)',
                        (self.name_edit.text(), self.psw_edit.text(), self.email_edit.text(), self.phone_edit.text(),
                         self.edit_surname.text(), self.edit_name.text(), id))
            self.db.commit()
            self.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            if check_db != 'OK':
                msg.setText(f'{check_db}')
            else:
                msg.setText("\n".join([elem for elem in checks if elem != "OK"]))
            msg.exec()


class main_wndw(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arrive_date = None
        self.deport_date = None
        self.btn_profile.clicked.connect(self.profile)
        self.btn_find.clicked.connect(self.search)
        self.btn_arrive.clicked.connect(self.choose_date)
        self.btn_deport.clicked.connect(self.choose_date)
        self.btn_num_people.clicked.connect(self.num_people)

    def profile(self):
        self.w = profil()
        self.w.show()

    def search(self):
        flag = 0
        if self.location.text():
            flag += 1
        if self.btn_arrive.text() != 'Дата заезда':
            flag += 1
        if self.btn_deport.text() != 'Дата отъезда':
            flag += 1
        if int(self.btn_num_people.text().split()[0]) >= 1 and int(self.btn_num_people.text().split()[-2]) >= 1:
            flag += 1
        if flag == 4:
            self.w = all_hotels(self.location.text(), self.btn_arrive.text(), self.btn_deport.text(),
                                self.btn_num_people.text())
            self.w.show()
        else:
            self.label_errors.setText('Произошла ошибка! Заполните все поля формы')

    def choose_date(self):
        sender = self.sender()
        dialog = calendar_dial()
        dialog.exec()
        date = dialog.date
        if date is not None:
            date_to_text = str(date).split('-')
            if sender == self.btn_arrive:
                if self.deport_date is None:
                    self.arrive_date = date
                    self.btn_arrive.setText(f'{date_to_text[-1]} {MONTHS[int(date_to_text[1]) - 1]} {date_to_text[0]}')
                else:
                    if date > self.deport_date:
                        self.btn_arrive.setText('Дата заезда')
                        self.label_errors.setText('Некорректная дата приезда')
                        return
                    else:
                        self.arrive_date = date
                        self.btn_arrive.setText(
                            f'{date_to_text[-1]} {MONTHS[int(date_to_text[1]) - 1]} {date_to_text[0]}')
            else:
                if self.arrive_date is None:
                    self.deport_date = date
                    self.btn_deport.setText(f'{date_to_text[-1]} {MONTHS[int(date_to_text[1]) - 1]} {date_to_text[0]}')
                else:
                    if date < self.arrive_date:
                        self.btn_deport.setText('Дата уезда')
                        self.label_errors.setText('Некорректная дата уезда')
                        return
                    else:
                        self.deport_date = date
                        self.btn_deport.setText(
                            f'{date_to_text[-1]} {MONTHS[int(date_to_text[1]) - 1]} {date_to_text[0]}')
        else:
            pass
        self.label_errors.setText('')

    def num_people(self):
        dialog = number_people_dial()
        dialog.exec()
        data = dialog.number
        if data is not None:
            self.btn_num_people.setText(
                f'{data[0]} {need_form_word(int(data[0]), "взрослый")}, {data[1]} '
                f'{need_form_word(int(data[1]), "ребенок")}, '
                f'{data[-1]} {need_form_word(int(data[-1]), "номер")}')
        else:
            pass


class calendar_dial(QDialog, calendar_dialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.date = None
        self.accepted.connect(self.get)

    def get(self):
        self.date = datetime.date(self.calendarWidget.selectedDate().year(), self.calendarWidget.selectedDate().month(),
                                  self.calendarWidget.selectedDate().day())


class number_people_dial(QDialog, choose_number_people.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.number = None
        self.accepted.connect(self.give_data)

    def give_data(self):
        self.number = [self.spinbox_adult.text(), self.spinbox_child.text(), self.spinbox_rooms.text()]


class profil(QWidget, profile.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_change.clicked.connect(self.change)
        # pixmap = QPixmap('photo_avatar.jpg').scaled(80, 80)
        # self.label_photo.setPixmap(pixmap)
        self.db_users = sqlite3.connect('users.db')
        self.fill_labels_info()
        self.fill_edit_books()

    def fill_edit_books(self):
        cur = self.db_users.cursor()
        result = cur.execute(
            f'SELECT name_hotel, date_arrive, date_deport, type_room FROM bookings WHERE '
            f'(SELECT user_id FROM users as us WHERE {CURRENT_USER_ID} = us.user_id)').fetchall()
        self.all_books.setColumnCount(4)
        self.all_books.setHorizontalHeaderLabels(['Отель', 'Дата прибытия', 'Дата отъезда', 'Тип номера'])
        self.all_books.setRowCount(len(result))
        if result:
            for i, elem in enumerate(result):
                for j, item in enumerate(elem):
                    self.all_books.setItem(i, j, QTableWidgetItem(item))
        else:
            self.label_books.setText('Нет существующих броней')

    def fill_labels_info(self):
        user = self.db_users.cursor().execute(
            f'SELECT surname, name, email, phone FROM users WHERE user_id = {CURRENT_USER_ID}').fetchone()
        self.label_FIO.setText(f'{user[0]} {user[1]}')
        self.label_phone.setText(f'{user[-1]}')
        self.label_email.setText(f'{user[2]}')

    def change(self):
        dialog = change_profile_dialog()
        dialog.exec()
        self.fill_labels_info()


class change_profile_dialog(QDialog, dialog_change_profile.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.changes = {'name': '', 'phone': '', 'mail': ''}
        self.buttonBox.accepted.connect(self.change_all)

    def change_all(self):
        db = sqlite3.connect('users.db')
        cur = db.cursor()
        if self.edit_fio.text().replace(' ', '') != '':
            cur.execute(
                f'UPDATE users SET surname = "{self.edit_fio.text().split()[0]}" WHERE user_id = {CURRENT_USER_ID}')
            cur.execute(
                f'UPDATE users SET name = "{self.edit_fio.text().split()[1]}" WHERE user_id = {CURRENT_USER_ID}')
        if '@' in self.edit_mail.text():
            cur.execute(f'UPDATE users SET email = "{self.edit_mail.text()}" WHERE'
                        f' user_id = {CURRENT_USER_ID}')
        if check_phone(self.edit_phone.text()) == 'OK':
            cur.execute(f'UPDATE users SET phone = "{self.edit_phone.text()}" WHERE'
                        f' user_id = {CURRENT_USER_ID}')
        db.commit()


class all_hotels(QWidget, list_hotels.Ui_Form):
    def __init__(self, city, arrive_date, deport_date, people):
        super().__init__()
        self.setupUi(self)
        self.city = city.lower()
        self.arrive = arrive_date
        self.deport = deport_date
        self.nm_people = people.split()
        self.db = sqlite3.connect('hotels.db')
        self.result = self.db.cursor().execute(
            f'SELECT name, street, rating, cost_room, id FROM hotels WHERE city = "{self.city}"').fetchall()
        self.label_amount.setText(
            f'{need_form_word(len(self.result), "найдено").capitalize()}'
            f' {len(self.result)} {need_form_word(len(self.result), "отель")}')
        y = 50
        self.buttons = {}
        for i in range(len(self.result)):
            label = QLabel(self.frame)
            pixmap = QPixmap(f'photo_hotels/{self.result[i][-1]}.jpg').scaled(251, 191)
            label.setPixmap(pixmap)
            label.move(20, y)
            btn = QPushButton('->', self.frame)
            btn.resize(41, 191)
            btn.move(590, y)
            self.buttons[self.result[i][-1]] = btn
            btn.clicked.connect(self.open_descript)
            textedit = QPlainTextEdit(self.frame)
            textedit.resize(301, 191)
            textedit.move(280, y)
            textedit.setReadOnly(True)
            textedit.setPlainText(
                f'"{self.result[i][0]}"\n\nРасположен на улице {self.result[i][1]}\n{self.result[i][-1]}\n'
                f'Цена за номер начинается от {self.result[i][-2]}')
            y += 200

    def open_descript(self):
        for key, elem in self.buttons.items():
            if elem == self.sender():
                self.w = description(key)
                self.w.show()


class description(QWidget, hotel_description.Ui_Form):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect('hotels.db')
        self.id = id
        self.hotel = self.db.cursor().execute(f'SELECT * FROM hotels WHERE id = {self.id}').fetchone()
        self.photo.setPixmap(QPixmap(f'photo_hotels/{self.id}.jpg').scaled(281, 171))
        self.type_rooms = self.db.cursor().execute(f'SELECT * FROM type_rooms WHERE id_hotel = {self.id}').fetchone()
        self.label_name.setText(f'{self.hotel[0]}')
        self.btn_photo_left.clicked.connect(self.change_photo)
        self.btn_photo_right.clicked.connect(self.change_photo)
        self.number_photo = 1
        self.fill_combobox()
        self.fill_edittext()
        self.comboBox.currentTextChanged.connect(self.fill_edittext)
        self.btn_book.clicked.connect(self.final_book)

    def change_photo(self):
        if self.number_photo == 1:
            self.photo.setPixmap(QPixmap(f'photo_hotels/{self.id}_room.jpg').scaled(281, 171))
            self.number_photo = 2
        else:
            self.photo.setPixmap(QPixmap(f'photo_hotels/{self.id}.jpg').scaled(281, 171))
            self.number_photo = 1

    def fill_combobox(self):
        if self.type_rooms[1] == 1:
            self.comboBox.addItem('Стандартный номер')
        if self.type_rooms[2] == 1:
            self.comboBox.addItem('Номер "Комфорт"')
        if self.type_rooms[3] == 1:
            self.comboBox.addItem('Семейный номер')
        if self.type_rooms[4] == 1:
            self.comboBox.addItem('Стандарт люкс')
        if self.type_rooms[-1] == 1:
            self.comboBox.addItem('Семейный люкс')

    def fill_edittext(self):
        self.description.setText(f'"{self.hotel[0]}"\n\nРасположен на улице {self.hotel[2]}\n'
                                 f'Цена за номер {self.comboBox.currentText()} - {self.cost_room()}\n'
                                 f'{DESCRIPTIONS_ROOM[self.comboBox.currentText()]}')

    def cost_room(self):
        if self.comboBox.currentText() == 'Стандартный номер':
            return self.hotel[-3]
        if self.comboBox.currentText() == 'Номер "Комфорт"':
            return self.hotel[-3] * 1.2
        if self.comboBox.currentText() == 'Семейный номер':
            return self.hotel[-3] * 1.4
        if self.comboBox.currentText() == 'Стандарт люкс':
            return self.hotel[-3] * 1.7
        if self.comboBox.currentText() == 'Семейный люкс':
            return self.hotel[-3] * 2

    def final_book(self):
        self.w = confirm()
        self.w.show()
        self.close()


class confirm(QWidget, confirm_booking.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Log_in_wndw()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

# почти все готово. осталось сделать:
# подтверждение бронирования
# подпправить фронтенд
