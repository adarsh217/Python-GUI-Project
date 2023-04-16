from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PySide2.QtWidgets import QApplication
from forma import MainWindow2
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the UI Page
        self.chartView = None
        uic.loadUi('mainWindow.ui', self)
        self.w = None
        self.comboBox.textActivated.connect(self.create_bar)

        self.image.clicked.connect(self.new_window)

    def new_window(self):
        self.w = MainWindow2()
        self.w.show()

    def create_bar(self):

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
        self.chartView.show()


def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
