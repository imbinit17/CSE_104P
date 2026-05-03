from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QGridLayout, QComboBox, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interactive Temperature Conversion Application")
        self.setGeometry(500, 200, 500, 450)
        self.Celsius_Input = True
        self.UI()

    def UI(self):
        self.central_widget = QWidget()
        self.central_widget.setObjectName("BG")
        self.central_widget.setStyleSheet("""
            #BG {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                stop:0 #0f2027, stop:0.5 #203a43, stop:1 #2c5364);
            }
        """)
        self.setCentralWidget(self.central_widget)
        self.window_layout = QGridLayout(self.central_widget)

        self.container = QWidget()
        self.container.setObjectName("MainContainer")
        self.container.setStyleSheet("""
            #MainContainer {
                background-color: white;
                border-radius: 35px;
            }
            QLabel { background: transparent; color: #2c3e50; }
        """)
        self.container.setFixedSize(360, 320)

        input_style = """
            border: 2px solid #ecf0f1;
            border-radius: 12px;
            padding: 10px;
            font-size: 15px;
            color: #2c3e50;
            background: #fdfdfd;
        """
        btn_style = """
            QPushButton {
                background: #2c5364;
                color: white;
                border-radius: 12px;
                padding: 12px;
                font-size: 15px;
                font-weight: bold;
            }
            QPushButton:hover { background: #203a43; }
        """

        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(35, 35, 35, 35)
        self.container_layout.setSpacing(15)

        self.cOrF_combo = QComboBox()
        self.cOrF_combo.setStyleSheet(input_style)
        self.cOrF_combo.addItems(['Celsius to Fahrenheit', 'Fahrenheit to Celsius'])
        self.cOrF_combo.currentTextChanged.connect(self.CelsiusFahreheitSelection)

        self.input_temp = QLineEdit()
        self.input_temp.setStyleSheet(input_style)
        self.input_temp.returnPressed.connect(self.submit)
        self.input_temp.setPlaceholderText("Enter Celsius...")
        
        self.submit_btn = QPushButton("Convert Now")
        self.submit_btn.setStyleSheet(btn_style)
        self.submit_btn.clicked.connect(self.submit)

        self.output_label = QLabel("")
        self.output_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #bdc3c7;")
        self.output_label.setAlignment(Qt.AlignCenter)

        self.container_layout.addWidget(self.cOrF_combo)
        self.container_layout.addWidget(self.input_temp)
        self.container_layout.addWidget(self.submit_btn)
        self.container_layout.addWidget(self.output_label)

        self.window_layout.addWidget(self.container, 0, 0, Qt.AlignCenter)

    def CelsiusFahreheitSelection(self, text):
        self.Celsius_Input = not self.Celsius_Input
        unit = "Celsius" if self.Celsius_Input else "Fahrenheit"
        self.input_temp.setPlaceholderText(f"Enter {unit}...")
        self.output_label.setText("")
        self.output_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #bdc3c7;")

    def submit(self):
        try:
            num = float(self.input_temp.text())
            if self.Celsius_Input:
                res = (num * 9/5) + 32
                self.output_label.setText(f"{res:.2f} °F")
            else:
                res = (num - 32) * 5/9
                self.output_label.setText(f"{res:.2f} °C")
            self.output_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c5364;")
        except ValueError:
            self.output_label.setText("Numbers only!")
            self.output_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #e74c3c;")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
