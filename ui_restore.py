from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class Ui_RestoreWindow(QWidget):
    def setupUi(self, RestoreWindow):
        RestoreWindow.setWindowTitle("Restore")
        RestoreWindow.setGeometry(100, 100, 400, 200)
        
        # Create widgets
        self.filename_label = QLabel("Backup File:")
        self.filename_input = QLineEdit()
        
        self.destination_label = QLabel("Destination Directory:")
        self.destination_input = QLineEdit()
        
        self.encryption_key_label = QLabel("Encryption Key:")
        self.encryption_key_input = QLineEdit()
        
        self.start_restore_button = QPushButton("Start Restore")
        
        self.status_label = QLabel("")

        # Create layouts
        layout = QVBoxLayout()

        layout.addWidget(self.filename_label)
        layout.addWidget(self.filename_input)
        layout.addWidget(self.destination_label)
        layout.addWidget(self.destination_input)
        layout.addWidget(self.encryption_key_label)
        layout.addWidget(self.encryption_key_input)
        layout.addWidget(self.start_restore_button)
        layout.addWidget(self.status_label)

        RestoreWindow.setLayout(layout)
