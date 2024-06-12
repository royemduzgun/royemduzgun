import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit

class GünlükUygulaması(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Günlük Uygulaması')

        self.text_area = QTextEdit()
        self.add_button = QPushButton('Giriş Ekle')
        self.view_button = QPushButton('Girişleri Görüntüle')

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.add_button)
        v_box.addWidget(self.view_button)

        self.setLayout(v_box)

        self.add_button.clicked.connect(self.add_entry)
        self.view_button.clicked.connect(self.view_entries)

    def add_entry(self):
        entry = self.text_area.toPlainText()
        with open('günlük.txt', 'a') as file:
            file.write(entry + '\n')
        self.text_area.clear()

    def view_entries(self):
        try:
            with open('günlük.txt', 'r') as file:
                entries = file.read()
                self.text_area.setText(entries)
        except FileNotFoundError:
            self.text_area.setText("Günlük bulunamadı.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    günlük_uygulaması = GünlükUygulaması()
    günlük_uygulaması.show()
    sys.exit(app.exec_())
