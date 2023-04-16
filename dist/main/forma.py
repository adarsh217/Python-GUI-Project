from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, \
    QPushButton, QFrame


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_grid = None
        # Set up the main layout
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)
        # Set up the filter options
        filter_frame = QFrame()
        filter_layout = QHBoxLayout(filter_frame)
        filter_layout.setAlignment(Qt.AlignRight)
        main_layout.addWidget(filter_frame)

        all_button = QPushButton("All")
        all_button.clicked.connect(self.update_image_grid_all)
        good_button = QPushButton("Good")
        good_button.clicked.connect(self.update_image_grid_good)
        bad_button = QPushButton("Bad")
        bad_button.clicked.connect(self.update_image_grid_bad)
        filter_layout.addWidget(all_button)
        filter_layout.addWidget(good_button)
        filter_layout.addWidget(bad_button)

        # Set up the image grid
        self.image_grid = QGridLayout()
        self.image_grid.setAlignment(Qt.AlignTop)
        main_layout.addLayout(self.image_grid)

    def update_image_grid_all(self):
        # Clear the current images in the grid layout
        for i in reversed(range(self.image_grid.count())):
            self.image_grid.itemAt(i).widget().setParent(None)
        image_paths = [f"images2/{i}.jpg" for i in range(1, 100)]
        image_labels = []
        # Update the image labels
        for i in range(36):
            image_label = QLabel()
            image_label.setFixedSize(100, 100)
            image_label.setAlignment(Qt.AlignCenter)
            image_label.setFrameShape(QFrame.Box)
            row = i // 6
            col = i % 6
            image_labels.append(image_label)
            pixmap = QPixmap(image_paths[i])
            image_labels[i].setPixmap(pixmap)
            if i % 10 != 0:
                image_label.setStyleSheet("border: 3px solid green;")
                self.image_grid.addWidget(image_label, row, col)
            else:
                image_label.setStyleSheet("border: 3px solid red;")
                self.image_grid.addWidget(image_label, row, col)

    def update_image_grid_good(self):
        # Clear the current images in the grid layout
        for i in reversed(range(self.image_grid.count())):
            self.image_grid.itemAt(i).widget().setParent(None)
        image_paths = [f"images2/{i}.jpg" for i in range(1, 100)]
        image_labels = []
        j = 0
        # Update the image labels
        for i in range(36):
            image_label = QLabel()
            image_label.setFixedSize(100, 100)
            image_label.setAlignment(Qt.AlignCenter)
            image_label.setFrameShape(QFrame.Box)
            row = j // 6
            col = j % 6
            image_labels.append(image_label)
            pixmap = QPixmap(image_paths[i])
            image_labels[i].setPixmap(pixmap)
            if i % 10 != 0:
                image_label.setStyleSheet("border: 3px solid green;")
                self.image_grid.addWidget(image_label, row, col)
                j += 1

    def update_image_grid_bad(self):
        # Clear the current images in the grid layout
        for i in reversed(range(self.image_grid.count())):
            self.image_grid.itemAt(i).widget().setParent(None)

        image_paths = [f"images2/{i}.jpg" for i in range(1, 100)]
        image_labels = []
        j = 0

        # Update the image labels
        for i in range(36):
            image_label = QLabel()
            image_label.setFixedSize(100, 100)
            image_label.setAlignment(Qt.AlignCenter)
            image_label.setFrameShape(QFrame.Box)
            row = j // 6
            col = j % 6
            image_labels.append(image_label)
            pixmap = QPixmap(image_paths[i])
            image_labels[i].setPixmap(pixmap)
            if i % 10 == 0:
                image_label.setStyleSheet("border: 3px solid red;")
                self.image_grid.addWidget(image_label, row, col)
                j += 1


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow2()
    window.show()
    app.exec_()
