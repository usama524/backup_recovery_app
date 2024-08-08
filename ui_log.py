from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit

class Ui_LogWindow(QWidget):
    def setupUi(self, LogWindow):
        LogWindow.setWindowTitle("Log")
        LogWindow.setGeometry(100, 100, 400, 300)
        
        # Create widgets
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        
        self.clear_log_button = QPushButton("Clear Log")
        
        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Log Messages:"))
        layout.addWidget(self.log_text)
        layout.addWidget(self.clear_log_button)
        
        LogWindow.setLayout(layout)
