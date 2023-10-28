import sys
import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QWidget
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from signals import signal
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main window and UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the "Open" action to the open_csv_file function
        self.ui.actionOpen.triggered.connect(self.open_csv_file)

        # Create a widget to display the matplotlib plot
        self.plot_widget = QWidget(self.ui.viewerTab)
        self.ui.signalLayout.addWidget(self.plot_widget)
        self.plot_widget.setLayout(QtWidgets.QVBoxLayout())

        self.canvas = FigureCanvas(plt.figure())
        self.plot_widget.layout().addWidget(self.canvas)
        self.my_siganl=signal()
        self.my_siganl.upload_signal_data([1,2],[2,3])
        
    def open_csv_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        # Get the path to the selected CSV file
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)",
                                                   options=options)

        if file_path:
            # Read the CSV file and extract the data
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                data = [row for row in csv_reader]

            if data:
                # Assuming your CSV file has two columns: time and magnitude
                time = [float(row[0]) for row in data]
                magnitude = [float(row[1]) for row in data]
                #self.MySignal(time,magnitude)
                self.my_siganl.upload_signal_data(time,magnitude)
                # Clear the previous plot
                self.canvas.figure.clear()
                # Create a new plot and display it
                self.my_siganl.sample_signal()
                ax = self.canvas.figure.add_subplot(3,1,1)
                ax.plot(self.my_siganl.x_data, self.my_siganl.y_data,linewidth=3)
                ax.set_xlabel("Time")
                ax.set_ylabel("Magnitude")
                ax.set_title("CSV Data Plot")
                ax.grid(True)
                ax.plot(self.my_siganl.samples_time, self.my_siganl.samples_amplitude, 'ro',  markersize=3,label='Sampled Signal')
                self.my_siganl.reconstruct_from_samples()
                ax = self.canvas.figure.add_subplot(3,1,2)
                ax.plot(self.my_siganl.x_data, self.my_siganl.reconstructed,linewidth=3)

                # Redraw the canvas
                self.canvas.draw()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.viewerTab = QtWidgets.QWidget()
        self.viewerTab.setObjectName("viewerTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.viewerTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.signalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.signalLayout.setContentsMargins(0, 0, 0, 0)
        self.signalLayout.setObjectName("signalLayout")
        self.FsampleDisp = QtWidgets.QLCDNumber(self.viewerTab)
        self.FsampleDisp.setGeometry(QtCore.QRect(620, 450, 51, 41))
        self.FsampleDisp.setObjectName("FsampleDisp")
        self.label = QtWidgets.QLabel(self.viewerTab)
        self.label.setGeometry(QtCore.QRect(20, 460, 131, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.viewerTab)
        self.label_2.setGeometry(QtCore.QRect(690, 460, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.viewerTab)
        self.label_4.setGeometry(QtCore.QRect(80, 510, 81, 21))
        self.label_4.setObjectName("label_4")
        self.FsampleSlider = QtWidgets.QSlider(self.viewerTab)
        self.FsampleSlider.setGeometry(QtCore.QRect(170, 460, 431, 22))
        self.FsampleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FsampleSlider.setObjectName("FsampleSlider")
        self.SNR_Slider = QtWidgets.QSlider(self.viewerTab)
        self.SNR_Slider.setGeometry(QtCore.QRect(170, 510, 431, 22))
        self.SNR_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.SNR_Slider.setObjectName("SNR_Slider")
        self.SNR_Disp = QtWidgets.QLCDNumber(self.viewerTab)
        self.SNR_Disp.setGeometry(QtCore.QRect(620, 500, 51, 41))
        self.SNR_Disp.setObjectName("SNR_Disp")
        self.tabWidget.addTab(self.viewerTab, "")
        self.composeTab = QtWidgets.QWidget()
        self.composeTab.setObjectName("composeTab")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.composeTab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 150, 791, 391))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.composeLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.composeLayout.setContentsMargins(0, 0, 0, 0)
        self.composeLayout.setObjectName("composeLayout")
        self.addSinButton = QtWidgets.QPushButton(self.composeTab)
        self.addSinButton.setGeometry(QtCore.QRect(40, 10, 101, 28))
        self.addSinButton.setObjectName("addSinButton")
        self.sinComboBox = QtWidgets.QComboBox(self.composeTab)
        self.sinComboBox.setGeometry(QtCore.QRect(360, 10, 91, 31))
        self.sinComboBox.setObjectName("sinComboBox")
        self.label_5 = QtWidgets.QLabel(self.composeTab)
        self.label_5.setGeometry(QtCore.QRect(50, 60, 81, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.composeTab)
        self.label_6.setGeometry(QtCore.QRect(650, 60, 55, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.composeTab)
        self.label_7.setGeometry(QtCore.QRect(50, 90, 71, 21))
        self.label_7.setObjectName("label_7")
        self.composeButton = QtWidgets.QPushButton(self.composeTab)
        self.composeButton.setGeometry(QtCore.QRect(270, 110, 93, 28))
        self.composeButton.setObjectName("composeButton")
        self.saveButton = QtWidgets.QPushButton(self.composeTab)
        self.saveButton.setGeometry(QtCore.QRect(440, 110, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.removeSinbutton = QtWidgets.QPushButton(self.composeTab)
        self.removeSinbutton.setGeometry(QtCore.QRect(650, 10, 101, 28))
        self.removeSinbutton.setObjectName("removeSinbutton")
        self.FcomposeSlider = QtWidgets.QSlider(self.composeTab)
        self.FcomposeSlider.setGeometry(QtCore.QRect(140, 60, 491, 22))
        self.FcomposeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FcomposeSlider.setObjectName("FcomposeSlider")
        self.amplitudeSlider = QtWidgets.QSlider(self.composeTab)
        self.amplitudeSlider.setGeometry(QtCore.QRect(140, 90, 491, 22))
        self.amplitudeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.amplitudeSlider.setObjectName("amplitudeSlider")
        self.tabWidget.addTab(self.composeTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sampling Frequency ="))
        self.label_2.setText(_translate("MainWindow", "Max Frequency"))
        self.label_4.setText(_translate("MainWindow", "SNR Level ="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewerTab), _translate("MainWindow", "Viewer"))
        self.addSinButton.setText(_translate("MainWindow", "Add Sinusoidal"))
        self.label_5.setText(_translate("MainWindow", "Frequency ="))
        self.label_6.setText(_translate("MainWindow", "Hz"))
        self.label_7.setText(_translate("MainWindow", "Amplitude ="))
        self.composeButton.setText(_translate("MainWindow", "Compose"))
        self.saveButton.setText(_translate("MainWindow", "Save As CSV"))
        self.removeSinbutton.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.composeTab), _translate("MainWindow", "Composer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
