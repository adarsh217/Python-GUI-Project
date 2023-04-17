import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget, \
    QHBoxLayout, QLabel, QComboBox
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from forma import MainWindow2

uri = "mongodb+srv://zarathos07:Abcd123@cluster0.ixhyrfv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

mydb = client.bottles
mycol = mydb.images


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = None
        self.chartView = None
        self.graph_layout = None
        self.graph = None
        self.stacked_widget = None
        self.main_layout = None
        self.combo_box = None
        self.w = None
        self.initUI()
        
    def initUI(self):
        # Set up the main layout
        main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        main_widget.setLayout(self.main_layout)

        # Create a button to switch to the graph
        graph_button = QPushButton("Image Gallery")
        graph_button.clicked.connect(self.switch_to_image)
        graph_button2 = QPushButton("Analytics")
        graph_button2.clicked.connect(self.switch_to_graph)
        self.main_layout.addWidget(graph_button2)
        self.main_layout.addWidget(graph_button)

        # Set up the stacked widget to switch between the image gallery and graph
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Set up the graph
        self.graph = QWidget()
        self.graph_layout = QVBoxLayout()
        self.graph.setLayout(self.graph_layout)
        self.stacked_widget.addWidget(self.graph)

        set0 = QBarSet("Good")
        set1 = QBarSet("Bad")

        result = [0] * 5
        for x in mycol.find({"Status": "Bad"}):
            if x["Unit id"] < 21:
                result[0] += 1
            elif 20 < x["Unit id"] < 41:
                result[1] += 1
            elif 40 < x["Unit id"] < 61:
                result[2] += 1
            elif 60 < x["Unit id"] < 81:
                result[3] += 1
            elif 80 < x["Unit id"] < 101:
                result[4] += 1

        result2 = [0] * 5
        for x in mycol.find({"Status": "Good"}):
            if x["Unit id"] < 20:
                result2[0] += 1
            elif 20 < x["Unit id"] < 40:
                result2[1] += 1
            elif 40 < x["Unit id"] < 60:
                result2[2] += 1
            elif 60 < x["Unit id"] < 80:
                result2[3] += 1
            elif 80 < x["Unit id"] < 100:
                result2[4] += 1

        set1 << result[0] << result[1] << result[2] << result[3] << result[4]
        set0 << result2[0] << result2[1] << result2[2] << result2[3] << result2[4]

        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = ["9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "12:00 PM"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        axis.setTitleText("Time")

        chart.addAxis(axis, Qt.AlignBottom)
        axisY = QValueAxis()
        axisY.setRange(0, 100)
        axisY.setTitleText("Percentage")
        chart.addAxis(axisY, Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignRight)

        self.chartView = QChartView(chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.resize(800, 600)
        self.graph_layout.addWidget(self.chartView)
        self.label = QLabel("Select KU id:")
        self.main_layout.addWidget(self.label)

        # Create a combo box to select the filter option
        self.combo_box = QComboBox()
        self.combo_box.addItem("SKU1")
        self.combo_box.addItem("SKU2")
        self.main_layout.addWidget(self.combo_box)
        self.combo_box.currentIndexChanged.connect(self.initUI)
        # Set the main widget for the window
        self.setCentralWidget(main_widget)

    def switch_to_graph(self):
        self.label.show()
        self.combo_box.show()
        self.chartView.show()

    def switch_to_image(self):
        self.w = MainWindow2()
        self.chartView.hide()
        self.label.hide()
        self.combo_box.hide()
        self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1000, 800)
    window.show()
    sys.exit(app.exec_())
