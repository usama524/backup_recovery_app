from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout

class Ui_BackupWindow(QWidget):
    def setupUi(self, BackupWindow):
        BackupWindow.setWindowTitle("Backup")
        BackupWindow.setGeometry(100, 100, 400, 300)
        
        # Create widgets
        self.source_label = QLabel("Source Directory:")
        self.source_input = QLineEdit()
        
        self.destination_label = QLabel("Destination Directory:")
        self.destination_input = QLineEdit()
        
        self.filename_label = QLabel("Filename:")
        self.filename_input = QLineEdit()
        
        self.compression_label = QLabel("Compression:")
        self.compression_input = QComboBox()
        self.compression_input.addItems(["gzip", "none"])
        
        self.encryption_key_label = QLabel("Encryption Key:")
        self.encryption_key_input = QLineEdit()
        
        self.start_backup_button = QPushButton("Start Backup")
        
        self.status_label = QLabel("")

        # Create layouts
        layout = QVBoxLayout()

        layout.addWidget(self.source_label)
        layout.addWidget(self.source_input)
        layout.addWidget(self.destination_label)
        layout.addWidget(self.destination_input)
        layout.addWidget(self.filename_label)
        layout.addWidget(self.filename_input)
        layout.addWidget(self.compression_label)
        layout.addWidget(self.compression_input)
        layout.addWidget(self.encryption_key_label)
        layout.addWidget(self.encryption_key_input)
        layout.addWidget(self.start_backup_button)
        layout.addWidget(self.status_label)

        BackupWindow.setLayout(layout)
