from PySide6.QtCore import QObject, Signal
class ThemeManager(QObject):
    theme_changed=Signal(bool)
    def __init__(self):
        super().__init__()
        self.dark_mode=False
    def toggle(self):
        self.dark_mode=not self.dark_mode
        self.theme_changed.emit(self.dark_mode)