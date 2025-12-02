from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt, QPropertyAnimation, QRect
from PySide6.QtGui import QPainter, QColor, QFont
import sys


class DynamicIsland(QWidget):
    def __init__(self):
        super().__init__()

        # --- Window properties ---
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Bubble size
        self.normal_width = 180
        self.normal_height = 40
        self.expanded_width = 350
        self.expanded_height = 120

        self.resize(self.normal_width, self.normal_height)

        # --- Simple text inside ---
        self.label = QLabel("Dynamic Island", self)
        self.label.setStyleSheet("color: white;")
        self.label.setFont(QFont("Arial", 12))
        self.label.move(20, 10)

        # Animation setup
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(200)

        # Position (top center of the screen)
        screen = QApplication.primaryScreen().geometry()
        x = screen.width() // 2 - self.normal_width // 2
        y = 30
        self.move(x, y)

    # Draw the rounded bubble
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        color = QColor(0, 0, 0, 200)  # semi-transparent black
        painter.setBrush(color)
        painter.setPen(Qt.NoPen)

        painter.drawRoundedRect(self.rect(), 20, 20)

    # Expand when mouse enters
    def enterEvent(self, event):
        self.animate_to(self.expanded_width, self.expanded_height)

    # Collapse when mouse leaves
    def leaveEvent(self, event):
        self.animate_to(self.normal_width, self.normal_height)

    # Animation function
    def animate_to(self, w, h):
        current_geometry = self.geometry()
        new_geometry = QRect(
            current_geometry.x() - (w - current_geometry.width()) // 2,
            current_geometry.y(),
            w,
            h
        )
        self.animation.stop()
        self.animation.setStartValue(current_geometry)
        self.animation.setEndValue(new_geometry)
        self.animation.start()


app = QApplication(sys.argv)
window = DynamicIsland()
window.show()

sys.exit(app.exec())
