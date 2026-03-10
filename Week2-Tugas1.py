from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QComboBox, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtGui import QFont, QColor, QPainter
from PySide6.QtCore import Qt
import sys

class Header(QWidget):
    """Header dengan 3 lingkaran warna ala macOS + judul"""
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.setFixedHeight(50)

    def paintEvent(self, event):
        painter = QPainter(self)
        # Lingkaran merah, kuning, hijau
        colors = [QColor("#e74c3c"), QColor("#f1c40f"), QColor("#2ecc71")]
        for i, color in enumerate(colors):
            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(10 + i*25, 12, 15, 15)
        # Judul
        painter.setPen(QColor("#2c3e50"))
        painter.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        painter.drawText(100, 30, self.title)

class BiodataApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setFixedSize(400, 450)

        # Layout utama
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Header
        header = Header("Form Biodata Mahasiswa")
        main_layout.addWidget(header)

        # Form Layout (runtut ke bawah)
        form_layout = QFormLayout()
        main_layout.addLayout(form_layout)

        # Warna hijau mint untuk semua input
        input_style = "background-color: #d5f5e3; padding:5px;"

        # Input Nama
        self.nama_input = QLineEdit()
        self.nama_input.setPlaceholderText("Masukkan Nama Lengkap")
        self.nama_input.setStyleSheet(input_style)
        form_layout.addRow("Nama Lengkap:", self.nama_input)

        # Input NIM
        self.nim_input = QLineEdit()
        self.nim_input.setPlaceholderText("Masukkan NIM")
        self.nim_input.setStyleSheet(input_style)
        form_layout.addRow("NIM:", self.nim_input)

        # Input Kelas
        self.kelas_input = QLineEdit()
        self.kelas_input.setPlaceholderText("Contoh: TI-2A")
        self.kelas_input.setStyleSheet(input_style)
        form_layout.addRow("Kelas:", self.kelas_input)

        # ComboBox Jenis Kelamin
        self.jk_combo = QComboBox()
        self.jk_combo.addItems(["Laki-laki", "Perempuan"])
        self.jk_combo.setStyleSheet(input_style)
        form_layout.addRow("Jenis Kelamin:", self.jk_combo)

        # Tombol Tampilkan & Reset horizontal
        btn_layout = QHBoxLayout()
        self.tampilkan_btn = QPushButton("Tampilkan")
        self.reset_btn = QPushButton("Reset")
        self.tampilkan_btn.setStyleSheet(
            "background-color: #85c1e9; color: white; padding:5px 15px;"
        )
        self.reset_btn.setStyleSheet(
            "background-color: #7f8c8d; color: white; padding:5px 15px;"
        )
        btn_layout.addWidget(self.tampilkan_btn)
        btn_layout.addWidget(self.reset_btn)
        main_layout.addLayout(btn_layout)

        # Label hasil
        self.hasil_label = QLabel("")
        self.hasil_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.hasil_label.setStyleSheet(
            "background-color: #d5f5e3; border-left: 5px solid #27ae60; padding: 10px;"
        )
        self.hasil_label.setWordWrap(True)
        main_layout.addWidget(self.hasil_label)

        # Koneksi tombol
        self.tampilkan_btn.clicked.connect(self.tampilkan_data)
        self.reset_btn.clicked.connect(self.reset_data)

    def tampilkan_data(self):
        nama = self.nama_input.text().strip()
        nim = self.nim_input.text().strip()
        kelas = self.kelas_input.text().strip()
        jk = self.jk_combo.currentText()

        # Validasi input
        if not nama or not nim or not kelas:
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        # Tampilkan hasil dengan jarak antar baris rapi
        self.hasil_label.setText(
            f"<b>DATA BIODATA</b><br><br>"
            f"<b>Nama:</b> {nama}<br>"
            f"<b>NIM:</b> {nim}<br>"
            f"<b>Kelas:</b> {kelas}<br>"
            f"<b>Jenis Kelamin:</b> {jk}"
        )

    def reset_data(self):
        self.nama_input.clear()
        self.nim_input.clear()
        self.kelas_input.clear()
        self.jk_combo.setCurrentIndex(0)
        self.hasil_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BiodataApp()
    window.show()
    sys.exit(app.exec())