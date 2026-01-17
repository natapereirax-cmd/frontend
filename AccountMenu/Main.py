import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from AccountMenu.Login import Login
from AccountMenu.Signup import SignUp
from theme_manager import ThemeManager
theme_manager = ThemeManager()
#class MainWindow where all the methods are defined
class MainWindow(QMainWindow):
    def __init__(self):
        super(). __init__()
#makes variables that call the classes related to other windows
        self.login = Login(theme_manager)
        self.signup = SignUp(theme_manager)
#makes a stacked widget where all windows are going to be printed
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
#stacks the windows in order
        self.stack.addWidget(self.login)
        self.stack.addWidget(self.signup)
#the buttons of each screen are given a function
        self.login.go_to_signup.connect(self.show_signup)
        self.signup.go_to_login.connect(self.show_login)
#the first screen method is called
        self.show_login()
#each screen's method
    def show_login(self):
        self.stack.setCurrentWidget(self.login)
        self.setFixedSize(self.login.size())
    def show_signup(self):
        self.stack.setCurrentWidget(self.signup)
        self.setFixedSize(self.signup.size())
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
