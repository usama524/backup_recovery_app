from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication
import sys

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        # Initialize layout
        self.layout = QVBoxLayout(self)
        
        # Username label and input
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)

        # Password label and input
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        # Login and Register buttons
        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("Register")
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.register_button)

        # Connect buttons to methods
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        print(f"Login: {username}, {password}")

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        print(f"Register: {username}, {password}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
