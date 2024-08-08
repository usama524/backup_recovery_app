from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class Ui_AboutWindow(QWidget):
    def setupUi(self, AboutWindow):
        AboutWindow.setWindowTitle("About")
        AboutWindow.setGeometry(100, 100, 300, 200)
        
        # Create widgets
        self.info_label = QLabel("This is a Backup and Restore Application.\nVersion 1.0")
        self.close_button = QPushButton("Close")
        
        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.close_button)
        
        AboutWindow.setLayout(layout)
