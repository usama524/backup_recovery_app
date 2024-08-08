import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox
from login import LoginWindow  # Import the LoginWindow class
from ui_backup import Ui_BackupWindow
from ui_restore import Ui_RestoreWindow
from ui_log import Ui_LogWindow
from ui_about import Ui_AboutWindow
from backup_manager import BackupThread
from restore_manager import RestoreThread
from user_auth import authenticate_user, register_user

class MainApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.login_window = LoginWindow()  # Initialize the LoginWindow
        self.backup_window = Ui_BackupWindow()  # Initialize the backup window
        self.restore_window = Ui_RestoreWindow()
        self.log_window = Ui_LogWindow()
        self.about_window = Ui_AboutWindow()
        self.init_ui()

    def init_ui(self):
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Initialize and setup login, backup, restore, log, and about windows
        self.login_window.init_ui()  # Use init_ui instead of setupUi
        self.backup_window.setupUi(self)  # Setup backup window UI
        self.restore_window.setupUi(self)
        self.log_window.setupUi(self)
        self.about_window.setupUi(self)

        # Add windows to stacked widget
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.backup_window)
        self.stacked_widget.addWidget(self.restore_window)
        self.stacked_widget.addWidget(self.log_window)
        self.stacked_widget.addWidget(self.about_window)

        # Connect signals and slots
        self.login_window.login_button.clicked.connect(self.login)
        self.login_window.register_button.clicked.connect(self.register)
        self.backup_window.start_backup_button.clicked.connect(self.start_backup)
        self.restore_window.start_restore_button.clicked.connect(self.start_restore)
        self.log_window.clear_log_button.clicked.connect(self.clear_logs)
        
        # Show login window initially
        self.stacked_widget.setCurrentWidget(self.login_window)    

    def login(self):
        username = self.login_window.username_input.text()
        password = self.login_window.password_input.text()
        if authenticate_user(username, password):
            self.stacked_widget.setCurrentWidget(self.backup_window)
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def register(self):
        username = self.login_window.username_input.text()
        password = self.login_window.password_input.text()
        try:
            register_user(username, password)
            QMessageBox.information(self, "Registration Successful", "You can now log in.")
        except ValueError:
            QMessageBox.warning(self, "Registration Failed", "Username already exists.")

    def start_backup(self):
        # Start the backup process (this should include gathering backup options)
        backup_thread = BackupThread(filename="backup", source="/path/to/source",
                                     destination="/path/to/destination", compression="gzip",
                                     encryption_key=b"your-encryption-key")
        backup_thread.progress.connect(self.update_log)
        backup_thread.start()

    def start_restore(self):
        # Start the restore process (this should include gathering restore options)
        restore_thread = RestoreThread(filename="backup.enc", destination="/path/to/destination",
                                       encryption_key=b"your-encryption-key")
        restore_thread.progress.connect(self.update_log)
        restore_thread.start()

    def update_log(self, message):
        self.log_window.log_text.append(message)

    def clear_logs(self):
        self.log_window.log_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
