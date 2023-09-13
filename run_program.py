import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QInputDialog, QDesktopWidget
import encrypt
import decrypt

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Encryption and Decryption App'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        # Set the geometry of the window
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Center the window on the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        layout = QVBoxLayout()

        # Create and place the "Encrypt" button
        self.encrypt_button = QPushButton('Encrypt a Message', self)
        self.encrypt_button.clicked.connect(self.encrypt_message)
        layout.addWidget(self.encrypt_button)

        # Create and place the "Decrypt" button
        self.decrypt_button = QPushButton('Decrypt a Message', self)
        self.decrypt_button.clicked.connect(self.decrypt_message)
        layout.addWidget(self.decrypt_button)

        self.setLayout(layout)
        self.show()

    def encrypt_message(self):
        text, ok = QInputDialog.getMultiLineText(self, 'Message', 'Enter the message to encrypt:')
        if ok:
            _ = encrypt.main_encryption(text)
            QMessageBox.information(self, "Success", "Message encrypted successfully.")

    def decrypt_message(self):
        decrypted_content = decrypt.main_decryption()
        QMessageBox.information(self, "Decrypted Message", decrypted_content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())