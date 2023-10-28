import sys
import os
import csv
from classes import*
import pandas as pd
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
        #self.ui.actionOpen.triggered.connect(self.open_csv_file)

        # Create a widget to display the matplotlib plot
        self.plot_widget = QWidget(self.ui.viewerTab)
        self.ui.signalLayout.addWidget(self.plot_widget)
        self.plot_widget.setLayout(QtWidgets.QVBoxLayout())

        self.sinwaves_list = []  # List to store sinwaves objects


        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
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
        self.my_siganl=signal()
        self.my_siganl.upload_signal_data([1,2],[2,3])
        self.canvas_1 = FigureCanvas(plt.figure())
        self.canvas_2 = FigureCanvas(plt.figure())
        self.canvas_3 = FigureCanvas(plt.figure())
        #create canvas_sin for sinwaves
        self.canvas_sin = FigureCanvas(plt.figure())

        self.signalLayout.layout().addWidget(self.canvas_1)
        self.signalLayout.layout().addWidget(self.canvas_2)
        self.signalLayout.layout().addWidget(self.canvas_3)
        #add canvas_sin in the composeLayout
        self.composeLayout.layout().addWidget(self.canvas_sin)

        # Connect the "Open" action to the open_csv_file function
        self.actionOpen.triggered.connect(self.open_csv_file)

        # connect Addsinbutton to plot_sinwaves function
        self.addSinButton.clicked.connect(self.update_sine_wave_plot)

        # Connect the slider to the change_frequency function
        self.FcomposeSlider.valueChanged.connect(self.change_frequency)
        # Connect the amplitudeSlider to the change_amplitude function
        self.amplitudeSlider.valueChanged.connect(self.change_amplitude)

        # Initialize default values for frequency and amplitude
        self.frequency = 1.0
        self.amplitude = 1.0



    def open_csv_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.MainWindow, 'Open CSV File', '', 'CSV Files (*.csv)')
        if file_path:
            df = pd.read_csv(file_path)

            # Assuming your CSV file has two columns: time and magnitude
            time = df.iloc[:,0]
            magnitude = df.iloc[:,1]
            #self.MySignal(time,magnitude)
            self.my_siganl.upload_signal_data(time,magnitude)
            # Clear the previous plot
            self.canvas_1.figure.clear()
            self.canvas_2.figure.clear()
            # Create a new plot and display it
            self.my_siganl.sample_signal()
            ax = self.canvas_1.figure.add_subplot(1,1,1)
            ax.plot(self.my_siganl.x_data, self.my_siganl.y_data,linewidth=3)
            ax.set_xlabel("Time")
            ax.set_ylabel("Magnitude")
            ax.set_title("Original Signal")
            ax.grid(True)
            ax.plot(self.my_siganl.samples_time, self.my_siganl.samples_amplitude, 'ro',  markersize=3,label='Sampled Signal')
            self.my_siganl.reconstruct_from_samples()
            ax_reconstructed = self.canvas_2.figure.add_subplot(1,1,1)
            ax_reconstructed.set_xlabel("Time")
            ax_reconstructed.set_ylabel("Magnitude")
            ax_reconstructed.set_title("Reconstructed Signal")
            ax_reconstructed.grid(True)
            ax_reconstructed.plot(self.my_siganl.x_data, self.my_siganl.reconstructed,linewidth=3)
            self.my_siganl.calc_difference()
            ax_difference = self.canvas_3.figure.add_subplot(1,1,1)
            ax_difference.set_xlabel("Time")
            ax_difference.set_ylabel("Magnitude")
            ax_difference.set_title("ax_difference Signal")
            ax_difference.grid(True)
            ax_difference.plot(self.my_siganl.x_data, self.my_siganl.difference_original_reconstructed,linewidth=3)


            # Redraw the canvas
            self.canvas_1.draw()
            self.canvas_2.draw()
            self.canvas_3.draw()



    def change_frequency(self, value):
        # Get the slider value and use it to update the frequency
        self.frequency = value / 10.0  # You may need to adjust this scaling factor
        # Update the sine wave plot
        self.update_sine_wave_plot()

    def change_amplitude(self, value):
        # Get the slider value and use it to update the amplitude
        self.amplitude = value / 10.0  # You may need to adjust this scaling factor
        # Update the sine wave plot
        self.update_sine_wave_plot()

    def update_sine_wave_plot(self):



        # Recreate and update the sine wave plot with the current frequency and amplitude
        self.canvas_sin.figure.clear()
        ax = self.canvas_sin.figure.add_subplot(111)

        # Generate a sine wave with the current frequency and amplitude
        time = np.linspace(0, 2 * np.pi, 1000)
        sine_wave = self.amplitude * np.sin(2 * np.pi * self.frequency * time)

        ax.plot(time, sine_wave)
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
        ax.set_title(f"Sine Wave (Frequency: {self.frequency} Hz, Amplitude: {self.amplitude})")
        ax.grid(True)

        # Redraw the canvas
        self.canvas_sin.draw()



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
