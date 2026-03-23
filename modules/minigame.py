from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QApplication, QWidget
from PySide6.QtCore import Qt, QTimer

class MinigameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.count = 0
        self.target = 5

        screen = QApplication.primaryScreen().geometry()
        self.setFixedSize(screen.width(), screen.height())
        self.move(0, 0)

        # TAKES AWAY THE X / CLOSE AND THE MINIMIZE BUTTON
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | 
            Qt.FramelessWindowHint
        )

        self.setStyleSheet("background-color: rgb(140, 58, 199);") #layout styling

        # outer layout, covers the whole screen
        outer_layout = QVBoxLayout()
        outer_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(outer_layout)

        # inner container
        container = QWidget()
        container.setFixedSize(400,300)
        container.setStyleSheet("background-color: rgb(196, 140, 237); border-radius: 10px;") #container styling
        outer_layout.addWidget(container, alignment=Qt.AlignCenter)

        # layout inside the container
        layout = QVBoxLayout()
        container.setLayout(layout)

        # label
        self.label = QLabel(f"Press the button {self.target} times to unlock your app!")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # counter label
        self.counter_label = QLabel(f"0 / {self.target}")
        self.counter_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.counter_label)

        # button
        self.button = QPushButton("PRESS ME")
        self.button.setStyleSheet("background-color: rgb(255,255,255);")
        self.button.clicked.connect(self.buttonPressed)
        layout.addWidget(self.button)

    def buttonPressed(self):
        self.count += 1
        self.counter_label.setText(f"{self.count} / {self.target}")

        if self.count >= self.target:
            self.label.setText("You won!")
            self.button.setEnabled(False)
            #wait 1.2 seconds and then close
            QTimer.singleShot(1200, self.accept)