import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QProgressBar, QHBoxLayout,
    QVBoxLayout
)
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QTimer
from PySide6.QtGui import QPainter, QColor, QFont


class AdvancedDynamicIsland(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Sizes
        self.normal_width = 180
        self.normal_height = 40
        self.expanded_width = 380
        self.expanded_height = 150

        self.resize(self.normal_width, self.normal_height)

        # Animation
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(220)

        # Position (top center)
        screen = QApplication.primaryScreen().geometry()
        x = screen.width() // 2 - self.normal_width // 2
        self.move(x, 30)

        # ---------- MAIN UI ----------
        self.init_ui()

        # Fake music progress simulation
        self.progress_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

    def init_ui(self):
        # Container layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 10, 20, 10)

        # Title
        self.title = QLabel("Now Playing")
        self.title.setStyleSheet("color: white; font-size: 13px; font-weight: bold;")

        # Song name
        self.song = QLabel("► Memories – Maroon 5")
        self.song.setStyleSheet("color: white; font-size: 12px;")

        # Progress bar
        self.progress = QProgressBar()
        self.progress.setStyleSheet("""
            QProgressBar {
                background-color: rgba(255,255,255,80);
                border-radius: 5px;
                height: 6px;
            }
            QProgressBar::chunk {
                background-color: white;
                border-radius: 5px;
            }
        """)
        self.progress.setValue(0)

        # Controls
        btn_layout = QHBoxLayout()
        self.play = QPushButton("⏯")
        self.play.setStyleSheet(self.button_style())

        self.play.clicked.connect(self.toggle_play)

        btn_layout.addWidget(self.play)
        btn_layout.addStretch()

        # Add widgets
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.song)
        self.layout.addWidget(self.progress)
        self.layout.addLayout(btn_layout)

        # A hidden container (only visible when expanded)
        container = QWidget()
        container.setLayout(self.layout)
        self.container = container

        # Start collapsed (hide details)
        container.hide()

        # Add to main
        main = QVBoxLayout(self)
        main.addWidget(self.container)

    def button_style(self):
        return """
            QPushButton {
                background-color: rgba(255,255,255,40);
                color: white;
                border-radius: 15px;
                padding: 4px 10px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: rgba(255,255,255,80);
            }
        """

    # Rounded transparent background
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        color = QColor(0, 0, 0, 210)
        painter.setBrush(color)
        painter.setPen(Qt.NoPen)

        painter.drawRoundedRect(self.rect(), 20, 20)

    # Expand
    def enterEvent(self, event):
        self.animate_to(self.expanded_width, self.expanded_height)
        self.container.show()

    # Collapse
    def leaveEvent(self, event):
        self.animate_to(self.normal_width, self.normal_height)
        self.container.hide()

    # Animation logic
    def animate_to(self, w, h):
        current = self.geometry()
        new_rect = QRect(
            current.x() - (w - current.width()) // 2,
            current.y(),
            w,
            h
        )
        self.animation.stop()
        self.animation.setStartValue(current)
        self.animation.setEndValue(new_rect)
        self.animation.start()

    # Play/pause simulation
    def toggle_play(self):
        if self.timer.isActive():
            self.timer.stop()
            self.play.setText("▶")
        else:
            self.timer.start(100)
            self.play.setText("⏸")

    def update_progress(self):
        self.progress_value += 1
        if self.progress_value >= 100:
            self.progress_value = 0
        self.progress.setValue(self.progress_value)


app = QApplication(sys.argv)
island = AdvancedDynamicIsland()
island.show()
sys.exit(app.exec())
