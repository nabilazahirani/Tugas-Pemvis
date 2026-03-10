# Week2-Tugas2-final.py
# Konversi Suhu dengan tema putih-biru, tombol biru cerah, header macOS

from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFrame
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import sys

class KonversiSuhuApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konversi Suhu")
        self.setFixedSize(500, 400)
        self.setStyleSheet("background-color: white;")  # wallpaper putih

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Header dengan lingkaran warna ala macOS
        header_frame = QFrame()
        header_frame.setFixedHeight(50)
        header_frame.setStyleSheet("background-color: white; border-bottom: 2px solid #d0e6f7;")

        header_label = QLabel("  ⚫ ⚫ ⚫  Konversi Suhu")  # bulatan merah-kuning-hijau
        header_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        header_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        # Kita gunakan emoji atau simbol untuk bulatan, warna merah, kuning, hijau
        header_label.setStyleSheet("color: black; margin-left: 10px;")
        header_layout = QVBoxLayout()
        header_layout.addWidget(header_label)
        header_frame.setLayout(header_layout)
        main_layout.addWidget(header_frame)

        # Label KONVERSI SUHU
        label_konversi = QLabel("KONVERSI SUHU")
        label_konversi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_konversi.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        label_konversi.setStyleSheet("color: #2c3e50; margin-top: 10px;")
        main_layout.addWidget(label_konversi)

        # Input frame
        input_frame = QFrame()
        input_layout = QHBoxLayout()
        input_frame.setLayout(input_layout)
        main_layout.addWidget(input_frame)

        label_input = QLabel("Masukkan Suhu (Celsius):")
        label_input.setFont(QFont("Arial", 10))
        label_input.setStyleSheet("padding: 5px; color: #000;")
        input_layout.addWidget(label_input)

        self.suhu_input = QLineEdit()
        self.suhu_input.setPlaceholderText("Masukkan angka suhu")
        self.suhu_input.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid #87cefa;  /* biru muda cerah */
                border-radius: 5px;
                padding: 6px;
                font-size: 12px;
                color: #000;
            }
            QLineEdit:focus {
                border: 2px solid #3399ff;
            }
            QLineEdit::placeholder {
                color: #9dc6a7;  /* hijau sage */
            }
        """)
        self.suhu_input.setFixedWidth(150)
        input_layout.addWidget(self.suhu_input)

        # Tombol frame
        tombol_frame = QFrame()
        tombol_layout = QHBoxLayout()
        tombol_frame.setLayout(tombol_layout)
        main_layout.addWidget(tombol_frame)

        # Tombol biru cerah muda
        tombol_style = """
            QPushButton {
                background-color: #87cefa;
                color: white;
                padding: 8px 20px;
                border-radius: 5px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00bfff;
            }
        """

        self.fahrenheit_btn = QPushButton("Fahrenheit")
        self.fahrenheit_btn.setStyleSheet(tombol_style)
        tombol_layout.addWidget(self.fahrenheit_btn)

        self.kelvin_btn = QPushButton("Kelvin")
        self.kelvin_btn.setStyleSheet(tombol_style)
        tombol_layout.addWidget(self.kelvin_btn)

        self.reamur_btn = QPushButton("Reamur")
        self.reamur_btn.setStyleSheet(tombol_style)
        tombol_layout.addWidget(self.reamur_btn)

        # Label Hasil Konversi
        label_hasil_title = QLabel("Hasil Konversi:")
        label_hasil_title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        label_hasil_title.setStyleSheet("color: #2c3e50; margin-top: 20px;")
        main_layout.addWidget(label_hasil_title)

        hasil_frame = QFrame()
        hasil_frame.setFrameShape(QFrame.Shape.StyledPanel)
        hasil_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-left: 5px solid #3399ff;
                border-radius: 5px;
                padding: 15px;
                margin-top: 5px;
            }
        """)
        hasil_layout = QVBoxLayout()
        hasil_frame.setLayout(hasil_layout)

        self.hasil_label = QLabel("-")
        self.hasil_label.setFont(QFont("Arial", 12))
        self.hasil_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hasil_label.setStyleSheet("color: #000000;")
        hasil_layout.addWidget(self.hasil_label)
        main_layout.addWidget(hasil_frame)
        main_layout.addStretch()

        # Koneksi tombol
        self.fahrenheit_btn.clicked.connect(lambda: self.konversi_suhu('fahrenheit'))
        self.kelvin_btn.clicked.connect(lambda: self.konversi_suhu('kelvin'))
        self.reamur_btn.clicked.connect(lambda: self.konversi_suhu('reamur'))

    def konversi_suhu(self, tujuan):
        try:
            celsius = float(self.suhu_input.text())
            if tujuan == 'fahrenheit':
                hasil = (celsius * 9/5) + 32
                satuan = "Fahrenheit"
            elif tujuan == 'kelvin':
                hasil = celsius + 273.15
                satuan = "Kelvin"
            elif tujuan == 'reamur':
                hasil = celsius * 4/5
                satuan = "Reamur"
            self.hasil_label.setText(f"{celsius:.2f} Celsius = {hasil:.2f} {satuan}")
        except ValueError:
            QMessageBox.warning(
                self, "Error", "Masukkan harus berupa angka!\nContoh: 100 atau 36.5"
            )
            self.suhu_input.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = KonversiSuhuApp()
    window.show()
    sys.exit(app.exec())