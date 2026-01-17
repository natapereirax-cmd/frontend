#imports classes from libraries
from theme_manager import ThemeManager
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QCheckBox)
from PySide6.QtCore import (Qt, Signal, QRegularExpression)
from PySide6.QtGui import (QIcon, QPixmap, QFontDatabase, QRegularExpressionValidator, QIntValidator)
import sys
#class Signup where all the methods are defined
class SignUp(QWidget):
    go_to_login = Signal()
    def __init__(self, theme_manager: ThemeManager):
        super().__init__()
        self.theme_manager = theme_manager
        self.window()
        self.font()
        self.screen()
        self.apply_light_mode()
        self.theme_manager.theme_changed.connect(self.on_theme_changed)
        self.on_theme_changed(self.theme_manager.dark_mode)
    def window(self):
# screen's size and title defined
        self.setWindowTitle('Sign Up')
        self.setFixedSize(420, 560)
# this defines the background of the screen
        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap("images/login_bg.png"))
        self.bg.setScaledContents(True)
        self.bg.setGeometry(0, 0, self.width(), self.height())
        self.bg.lower()
    def font(self):
# Signup font (title)
        self.title_id = QFontDatabase.addApplicationFont('fonts/SwirlyCanalope.otf')
        self.title_font = QFontDatabase.applicationFontFamilies(self.title_id)[0]
# Subtitle font (under signup)
        self.subtitle_id = QFontDatabase.addApplicationFont('fonts/OrangeAvenueDEMO-Regular.otf')
        self.subtitle_font = QFontDatabase.applicationFontFamilies(self.subtitle_id)[0]
# Additional information font
        self.info_id = QFontDatabase.addApplicationFont('fonts/Lato-Italic.ttf')
        self.info_font = QFontDatabase.applicationFontFamilies(self.info_id)[0]
    def screen(self):
# toggle theme for light and dark mode
        self.toggle_theme=QPushButton('')
        self.toggle_theme.setIcon(QIcon.fromTheme('weather-clear'))
        self.toggle_theme.setFixedSize(35, 35)
        self.toggle_theme.setCursor(Qt.PointingHandCursor)
        self.toggle_theme.setToolTip('Toggle Theme')
        self.toggle_theme.setStyleSheet('''
        QPushButton {
        background-color: #e0e0e0;''')
        self.toggle_theme.clicked.connect(self.theme_manager.toggle)
#icon picture
        icon=QPixmap('images/icon.png').scaled(
            48,48,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
#puts the picture in a label
        icon_lb = QLabel()
        icon_lb.setFixedSize(48, 48)
        icon_lb.setAlignment(Qt.AlignCenter)
        icon_lb.setPixmap(icon)
#title and subtitle's label
        self.title=QLabel('Sign Up')
        self.title.setAlignment(Qt.AlignCenter)
        self.subtitle=QLabel('Fill all the requirements')
        self.subtitle.setAlignment(Qt.AlignCenter)
#checkbox
        self.company=QCheckBox('Company')
        self.company.toggled.connect(self.toggle_email)
        self.employer=QCheckBox('Employer')
        self.employee=QCheckBox('Employee')
#fuction 'for' is important to call the only_one_checked method
        self.checkboxes=[self.company,self.employer,self.employee]
        for cb in self.checkboxes:
            cb.stateChanged.connect(self.only_one_checked)
#information text
        self.information=QLabel('Mark the box\naccording to your role')
#username text box
        self.username=QLineEdit()
        self.username.setPlaceholderText("Company | User name")
#it doesn't allow space button to be pressed in username
        regex_1=QRegularExpression(r"^\S+$")
        validator_1=QRegularExpressionValidator(regex_1)
        self.username.setValidator(validator_1)
#first name box
        self.first_name=QLineEdit()
        self.first_name.setPlaceholderText("First Name")
#last name box
        self.last_name=QLineEdit()
        self.last_name.setPlaceholderText("Last Name")
#restrictions for first and last name input on QLineEdit
        regex_2 = QRegularExpression("^[A-Za-z]+$")
        validator_2 = QRegularExpressionValidator(regex_2)
        self.first_name.setValidator(validator_2)
        self.last_name.setValidator(validator_2)
#ID box
        self.id=QLineEdit()
        self.id.setPlaceholderText("ID")
        validator_3 = QIntValidator(0, 100000)
        self.id.setValidator(validator_3)
#email box
        self.email=QLineEdit()
        self.email.setPlaceholderText("Company's Email")
        self.email.setDisabled(True)
#restrictions for email input on QLineEdit
        regex_3 = QRegularExpression(
            r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        )
        validator_3 = QRegularExpressionValidator(regex_3)
        self.email.setValidator(validator_3)
#password text box
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
#agree check box
        self.agree=QCheckBox('I agree with the terms')
#warning text
        self.warning_text=QLabel('')
#signup button
        self.signup_button=QPushButton('Sign Up')
        self.signup_button.setFixedHeight(35)
        self.signup_button.setStyleSheet('''
        QPushButton {
        background-color: #3a86ff;
        color: white;
        corder-radius: 8px;
        height: 36px;
        font-size: 14px;}
        QPushButton:hover {
        background-color: #5a9bff;}''')
        self.signup_button.clicked.connect(self.pressed_signup)
#back button
        self.back_button=QPushButton('Back')
        self.back_button.setFixedHeight(35)
        self.back_button.setStyleSheet('''
        QPushButton {
        background-color: #3a86ff;
        color: white;
        corder-radius: 8px;
        height: 36px;
        font-size: 14px;}
        QPushButton:hover {
        background-color: #5a9bff;}''')
        self.back_button.clicked.connect(self.go_to_login.emit)
#defines top bar layout
        top_bar=QHBoxLayout()
        top_bar.addWidget(self.toggle_theme)
        top_bar.addStretch()
        top_bar.addWidget(icon_lb)
#defines the welcome message with title and subtitle
        welcome_layout=QVBoxLayout()
        welcome_layout.addWidget(self.title)
        welcome_layout.addWidget(self.subtitle)
#defines the option layout with three boxes
        option_layout=QVBoxLayout()
        option_layout.addWidget(self.company)
        option_layout.addWidget(self.employer)
        option_layout.addWidget(self.employee)
#defines the three boxes and info text layout
        info_layout=QHBoxLayout()
        info_layout.addLayout(option_layout)
        info_layout.addWidget(self.information)
        info_layout.setAlignment(Qt.AlignLeft)
#full name text layout
        name=QHBoxLayout()
        name.addWidget(self.first_name)
        name.addWidget(self.last_name)
#full name + all other information text layout
        form=QVBoxLayout()
        form.addLayout(name)
        form.addWidget(self.username)
        form.addWidget(self.id)
        form.addWidget(self.email)
        form.addWidget(self.password)
#buttons layout
        btn_layout=QHBoxLayout()
        btn_layout.addWidget(self.signup_button)
        btn_layout.addWidget(self.back_button)
#everything that's going to be printed in the card
        card_layout=QVBoxLayout()
        card_layout.setContentsMargins(30,30,30,30)
        card_layout.addLayout(top_bar)
        card_layout.addLayout(welcome_layout)
        card_layout.addLayout(info_layout)
        card_layout.addLayout(name)
        card_layout.addLayout(form)
        card_layout.addWidget(self.agree)
        card_layout.addWidget(self.warning_text)
        card_layout.addLayout(btn_layout)
        self.card=QFrame()
        self.card.setLayout(card_layout)
#finally, the main layout
        main_layout=QVBoxLayout()
        main_layout.addStretch()
        main_layout.addWidget(self.card)
        main_layout.addStretch()
        main_layout.setContentsMargins(40,4,40,4)
        self.setLayout(main_layout)
#this method doesn't allow the user to mark more than one checkbox
    def only_one_checked(self, state):
        if state:
            sender=self.sender()
            for cb in self.checkboxes:
                if cb is not sender:
                    cb.setChecked(False)
#email only enables if Manager's checkbox is clicked
    def toggle_email(self, checked):
        self.email.setEnabled(checked)
#confirms if the account has been created or not
    def pressed_signup(self):
        if not all([
            self.company.text(),
            self.employee.text(),
            self.first_name.text(),
            self.last_name.text(),
            self.username.text(),
            self.email.text(),
            self.id.text(),
            self.password.text(),
            self.agree.isChecked()
        ]):
            self.warning_text.setText("Fill all fields above")
            self.warning_text.setStyleSheet('color:red')
            return
        else:
            self.warning_text.setText("Account created")
            self.warning_text.setStyleSheet('color:green')
    def apply_light_mode(self):
#card's light mode layout
        self.card.setStyleSheet('''
        QFrame {
        background-color: #f0f1f4;
        border-radius: 12px;}''')
#title and subtitle's light mode layout
        self.title.setStyleSheet(f'''
        QLabel {{
        font-size: 40px;
        font-family: "{self.title_font}";
        color: black;}}''')
        self.subtitle.setStyleSheet(f'''
        QLabel {{
        font-size: 12px;
        font-family: "{self.subtitle_font}";
        color: #5a5a5a;}}''')
#company, employer and employee's light mode layout
        self.company.setStyleSheet('color: black')
        self.employer.setStyleSheet('color: black')
        self.employee.setStyleSheet('color: black')
#text input's light mode layout
        self.first_name.setStyleSheet(self.input_style('light'))
        self.last_name.setStyleSheet(self.input_style('light'))
        self.username.setStyleSheet(self.input_style('light'))
        self.password.setStyleSheet(self.input_style('light'))
        self.id.setStyleSheet(self.input_style('light'))
        self.email.setStyleSheet(self.input_style('light'))
#agree box on dark mode layout
        self.agree.setStyleSheet('color: black')
#this is the StyleSheet of the text next to the three check boxes
        self.information.setStyleSheet(f'''
        QLabel {{
        font-size: 12px;
        font-family: "{self.info_font}";
        color: #5a5a5a}}''')
# layout texts on dark mode
    def apply_dark_mode(self):
# card's dark mode layout
        self.card.setStyleSheet('''
        QFrame {
        background-color: #1e1e1e;
        border-radius: 12px;}''')
# title and subtitle's dark mode layout
        self.title.setStyleSheet(f'''
        QLabel {{
        font-size: 40px;
        font-family: "{self.title_font}";
        color: white;}}''')
        self.subtitle.setStyleSheet(f'''
        QLabel {{
        font-size: 12px;
        font-family: "{self.subtitle_font}";
        color: #aaaaaa}}''')
#company, employer and employee's dark mode layout
        self.company.setStyleSheet('color: #aaaaaa')
        self.employer.setStyleSheet('color: #aaaaaa')
        self.employee.setStyleSheet('color: #aaaaaa')
#text input's dark mode layout
        self.first_name.setStyleSheet(self.input_style('dark'))
        self.last_name.setStyleSheet(self.input_style('dark'))
        self.username.setStyleSheet(self.input_style('dark'))
        self.password.setStyleSheet(self.input_style('dark'))
        self.id.setStyleSheet(self.input_style('dark'))
        self.email.setStyleSheet(self.input_style('dark'))
#agree box on dark mode layout
        self.agree.setStyleSheet('color: #aaaaaa')
#this is the StyleSheet of the text next to the three check boxes
        self.information.setStyleSheet(f'''
        QLabel {{
        font-size: 12px;
        font-family: "{self.info_font}";
        color: #aaaaaa}}''')
#input_style is called by text inputs as the toggle theme button is clicked
    def input_style(self, mode='dark'):
        if mode=='dark':
            return '''
                QLabel {
                color: #aaaaaa;}
                QLineEdit {
                background-color: #2a2a2a;
                color:white;
                border:1px solid #444;
                border-radius: 6px;
                padding: 8px;}
                QLineEdit:focus {
                border: 1px solid #3a86ff;}'''
        else:
            return '''
                QLabel {
                color: #5a5a5a;}
                QLineEdit {
                background-color: #e6e9ee;
                color: 1e1e1e;
                border: 1px solid #b0b6bf;
                border-radius: 6px;
                padding: 8px;}
                QLineEdit:focus {
                border: 1px solid #3a86ff;
                background-color: #edf0f5;}'''
    def on_theme_changed(self, dark):
        if dark:
            self.apply_dark_mode()
        else:
            self.apply_light_mode()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    theme_manager = ThemeManager()
    window = SignUp(theme_manager)
    window.show()
    sys.exit(app.exec())