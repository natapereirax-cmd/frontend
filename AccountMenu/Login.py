#imports classes from libraries
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QCheckBox)
from PySide6.QtCore import (Qt, Signal)
from PySide6.QtGui import (QIcon, QPixmap, QFontDatabase, QIntValidator)
import sys
from theme_manager import ThemeManager
#class Login where all the methods are defined
class Login(QWidget):
    go_to_signup = Signal()
    def __init__(self, theme_manager: ThemeManager):
        self.theme_manager=theme_manager
        super().__init__()
        self.window()
        self.font()
        self.screen()
        self.apply_light_mode()
        self.theme_manager.theme_changed.connect(self.on_theme_changed)
        self.on_theme_changed(self.theme_manager.dark_mode)
    def window(self):
#screen's size and title defined
        self.setFixedSize(420, 540)
        self.setWindowTitle("Login")
#this defines the background of the screen
        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap("images/login_bg.png"))
        self.bg.setScaledContents(True)
        self.bg.setGeometry(0, 0, self.width(), self.height())
        self.bg.lower()
    def font(self):
#Welcome font (title)
        self.title_id=QFontDatabase.addApplicationFont('fonts/SwirlyCanalope.otf')
        self.title_font=QFontDatabase.applicationFontFamilies(self.title_id)[0]
#Subtitle font (under welcome)
        self.subtitle_id=QFontDatabase.addApplicationFont('fonts/OrangeAvenueDEMO-Regular.otf')
        self.subtitle_font=QFontDatabase.applicationFontFamilies(self.subtitle_id)[0]
#Additional information font
        self.info_id=QFontDatabase.addApplicationFont('fonts/Lato-Italic.ttf')
        self.info_font=QFontDatabase.applicationFontFamilies(self.info_id)[0]
    def screen(self):
#toggle theme for light and dark mode
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
#Welcome message
        self.title=QLabel('Welcome Back!')
        self.title.setAlignment(Qt.AlignCenter)
#subtitle bellow
        self.subtitle=QLabel('Sign in to continue')
        self.subtitle.setAlignment(Qt.AlignCenter)
#check box
        self.company=QCheckBox('Company')
        self.employer=QCheckBox('Employer')
        self.employee=QCheckBox('Employee')
#fuction 'for' is important to call the only_one_checked method
        self.checkboxes=[self.company,self.employer,self.employee]
        for cb in self.checkboxes:
            cb.stateChanged.connect(self.only_one_checked)
#information text
        self.information=QLabel('Mark the box\naccording to your role')
#id text box
        self.id=QLineEdit()
        self.id.setPlaceholderText("Company | User ID")
        self.id.setStyleSheet(self.input_style())
        validator_3 = QIntValidator(0, 100000)
        self.id.setValidator(validator_3)
#password text box
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setStyleSheet(self.input_style())
        self.password.setEchoMode(QLineEdit.Password)
#warning text
        self.warning_text=QLabel('')
#check box to save username and password
        self.save_infodata=QCheckBox('Save Account')
#login button
        self.login_button=QPushButton('Login')
        self.login_button.setFixedHeight(35)
        self.login_button.setStyleSheet('''
        QPushButton {
        background-color: #3a86ff;
        color: white;
        border-radius: 8px;
        height: 36px;
        font-size: 14px;}
        QPushButton:hover {
        background-color: #5a9bff;}''')
        self.login_button.clicked.connect(self.pressed_login)
#signup button
        self.signup_button=QPushButton('Sign Up')
        self.signup_button.setFixedHeight(35)
        self.signup_button.setStyleSheet('''
        QPushButton {
        background-color: #3a86ff;
        color: white;
        border-radius: 8px;
        height: 36px;
        font-size: 14px;}
        QPushButton:hover {
        background-color: #5a9bff;}''')
        self.signup_button.clicked.connect(self.go_to_signup.emit)
#now let's define where everything is placed
#let's start from the icon on the left top
        icon_lb=QLabel()
        icon_lb.setFixedSize(48, 48)
        icon_lb.setAlignment(Qt.AlignCenter)
        icon_lb.setPixmap(icon)
#defines the top layout
        top_bar = QHBoxLayout()
        top_bar.addWidget(self.toggle_theme)
        top_bar.addStretch()
        top_bar.addWidget(icon_lb)
#defines the welcome message
        welcome_layout=QVBoxLayout()
        welcome_layout.addWidget(self.title)
        welcome_layout.addWidget(self.subtitle)
#defines the check bot and info message
        option_layout=QVBoxLayout()
        option_layout.addWidget(self.company)
        option_layout.addWidget(self.employer)
        option_layout.addWidget(self.employee)
        info_layout=QHBoxLayout()
        info_layout.addLayout(option_layout)
        info_layout.addWidget(self.information)
        info_layout.setAlignment(Qt.AlignLeft)
#defines the text input boxes
        box_layout=QVBoxLayout()
        box_layout.addWidget(self.id)
        box_layout.addWidget(self.password)
#defines the buttons layout
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.signup_button)
#defines the final layout
        self.card=QFrame()
        card_layout=QVBoxLayout()
        card_layout.setContentsMargins(30, 30, 30, 30)
        card_layout.addLayout(top_bar)
        card_layout.addLayout(welcome_layout)
        card_layout.addLayout(info_layout)
        card_layout.addLayout(box_layout)
        card_layout.addWidget(self.warning_text)
        card_layout.addWidget(self.save_infodata)
        card_layout.addLayout(button_layout)
        self.card.setLayout(card_layout)
#finally the layout is printed and its size is fully defined
        mainLayout = QVBoxLayout()
        mainLayout.addStretch()
        mainLayout.addWidget(self.card)
        mainLayout.addStretch()
        mainLayout.setContentsMargins(40, 20, 40, 20)
        self.setLayout(mainLayout)
#this method doesn't allow the user to mark more than one checkbox
    def only_one_checked(self, state):
        if state:
            sender=self.sender()
            for cb in self.checkboxes:
                if cb is not sender:
                    cb.setChecked(False)
#layout texts on light mode
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
        self.id.setStyleSheet(self.input_style('light'))
        self.password.setStyleSheet(self.input_style('light'))
#this is the StyleSheet of the text next to the three check boxes
        self.information.setStyleSheet(f'''
        QLabel {{
        font-size: 12px;
        font-family: "{self.info_font}";
        color: #5a5a5a}}''')
# Save Account's light mode layout
        self.save_infodata.setStyleSheet('color: black')
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
        self.id.setStyleSheet(self.input_style('dark'))
        self.password.setStyleSheet(self.input_style('dark'))
#this is the StyleSheet of the text next to the three check boxes
        self.information.setStyleSheet(f'''
        QLabel {{
        font-size: 12px;
        font-family: "{self.info_font}";
        color: #aaaaaa}}''')
#Save Account's dark mode layout
        self.save_infodata.setStyleSheet('color: #aaaaaa')
    def pressed_login(self):
        if not all([
            self.company.text(),
            self.employer.text(),
            self.employee.text(),
            self.id.text(),
            self.password.text(),
        ]):
            self.warning_text.setText("Fill all fields above")
            self.warning_text.setStyleSheet('color:red')
            return
        else:
            self.warning_text.setText("Account created")
            self.warning_text.setStyleSheet('color:green')
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
                color: #1e1e1e;
                border: 1px solid #b0b6bf;
                border-radius: 6px;
                padding: 8px;}
                QLineEdit:focus {
                border: 1px solid #3a86ff;
                background-color: #edf0f5;}'''
#this makes the toggle theme button always work
    def on_theme_changed(self, dark):
        if dark:
            self.apply_dark_mode()
        else:
            self.apply_light_mode()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    theme_manager = ThemeManager()
    window = Login(theme_manager)
    window.show()
    sys.exit(app.exec())

