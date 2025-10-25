import os
import sys


# Настройка путей для PyQt5
def find_pyqt5_plugins():
    possible_paths = [
        os.path.join(os.path.dirname(sys.executable), 'Lib', 'site-packages', 'PyQt5', 'Qt5', 'plugins'),
        os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Programs', 'Python', 'Python39', 'Lib',
                     'site-packages', 'PyQt5', 'Qt5', 'plugins'),
        os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Python', 'Python39', 'site-packages', 'PyQt5',
                     'Qt5', 'plugins'),
    ]

    for path in possible_paths:
        if os.path.exists(path):
            print(f"Found Qt plugins at: {path}")
            return path

    print("Qt plugins not found in standard paths")
    return ''


plugin_path = find_pyqt5_plugins()
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройки графического интерфейса приложения."""
        # Устанавливаем размер как в Kivy
        self.setGeometry(100, 100, 400, 600)
        self.setWindowTitle("Софья Трегубова - Биография")
        self.setStyleSheet("background-color: #f5f5f5;")
        self.setUpMainWindow()
        self.show()

    def create_avatar_image(self):
        """Создаём простую аватарку"""
        import os
        os.makedirs("images", exist_ok=True)

        from PIL import Image, ImageDraw

        # Создаём простую аватарку
        avatar_img = Image.new('RGB', (150, 150), color='#e0e0e0')
        draw = ImageDraw.Draw(avatar_img)

        # Рисуем простой круг с инициалами
        draw.ellipse([0, 0, 149, 149], outline='#666666', width=3)
        draw.text((50, 55), "СТ", fill='#666666', font_size=40)

        avatar_img.save("images/avatar.png")

    def setUpMainWindow(self):
        """Создаём основной интерфейс в строгом стиле"""
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Создаём аватарку
        self.create_avatar_image()

        # Аватарка
        avatar_label = QLabel()
        pixmap = QPixmap("images/avatar.png")
        avatar_label.setPixmap(pixmap)
        avatar_label.setAlignment(Qt.AlignCenter)

        # Имя
        name_label = QLabel("Софья Трегубова")
        name_label.setFont(QFont("Arial", 18, QFont.Bold))
        name_label.setStyleSheet("color: #333333; margin: 10px 0;")
        name_label.setAlignment(Qt.AlignCenter)

        # Возраст
        age_label = QLabel("18 лет")
        age_label.setFont(QFont("Arial", 12))
        age_label.setStyleSheet("color: #666666; margin: 5px 0;")
        age_label.setAlignment(Qt.AlignCenter)

        # Раздел "Биография"
        bio_title = QLabel("Биография")
        bio_title.setFont(QFont("Arial", 14, QFont.Bold))
        bio_title.setStyleSheet("color: #444444; margin-top: 15px;")

        bio_text = QLabel(
            "Я люблю своих котов и играть на гитаре.")
        bio_text.setFont(QFont("Arial", 11))
        bio_text.setWordWrap(True)
        bio_text.setStyleSheet("color: #555555; background: white; padding: 10px; border-radius: 5px;")
        bio_text.setTextFormat(Qt.PlainText)

        # Раздел "Образование"
        education_title = QLabel("Образование")
        education_title.setFont(QFont("Arial", 14, QFont.Bold))
        education_title.setStyleSheet("color: #444444; margin-top: 15px;")

        education_text = QLabel("МАИ")
        education_text.setFont(QFont("Arial", 11))
        education_text.setStyleSheet("color: #555555; background: white; padding: 10px; border-radius: 5px;")

        # Собираем всё вместе
        main_layout.addWidget(avatar_label)
        main_layout.addWidget(name_label)
        main_layout.addWidget(age_label)
        main_layout.addWidget(bio_title)
        main_layout.addWidget(bio_text)
        main_layout.addWidget(education_title)
        main_layout.addWidget(education_text)

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())