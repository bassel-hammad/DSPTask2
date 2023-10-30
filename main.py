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
from sinwaves import sinwaves


class Ui_MainWindow(object):
    def __init__(self):
        self.MainWindow = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.viewerTab = QtWidgets.QWidget()
        self.viewerTab.setObjectName("viewerTab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.viewerTab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_2 = QtWidgets.QFrame(self.viewerTab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.signalLayout = QtWidgets.QVBoxLayout()
        self.signalLayout.setObjectName("signalLayout")
        self.gridLayout_9.addLayout(self.signalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 125))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 3, 1, 1)
        self.SNR_Disp = QtWidgets.QLCDNumber(self.frame_4)
        self.SNR_Disp.setObjectName("SNR_Disp")
        self.gridLayout_5.addWidget(self.SNR_Disp, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.SNR_Slider = QtWidgets.QSlider(self.frame_4)
        self.SNR_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.SNR_Slider.setObjectName("SNR_Slider")
        self.gridLayout_5.addWidget(self.SNR_Slider, 1, 1, 1, 1)
        self.FsampleDisp = QtWidgets.QLCDNumber(self.frame_4)
        self.FsampleDisp.setObjectName("FsampleDisp")
        self.gridLayout_5.addWidget(self.FsampleDisp, 0, 2, 1, 1)
        self.FsampleSlider = QtWidgets.QSlider(self.frame_4)
        self.FsampleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FsampleSlider.setObjectName("FsampleSlider")
        self.gridLayout_5.addWidget(self.FsampleSlider, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 1, 0, 1, 1)
        self.gridLayout_11.addWidget(self.frame_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.viewerTab, "")
        self.composeTab = QtWidgets.QWidget()
        self.composeTab.setObjectName("composeTab")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.composeTab)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frame_5 = QtWidgets.QFrame(self.composeTab)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.removeSinbutton = QtWidgets.QPushButton(self.frame_7)
        self.removeSinbutton.setObjectName("removeSinbutton")
        self.gridLayout_6.addWidget(self.removeSinbutton, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 2, 0, 1, 1)
        self.addSinButton = QtWidgets.QPushButton(self.frame_7)
        self.addSinButton.setObjectName("addSinButton")
        self.gridLayout_6.addWidget(self.addSinButton, 0, 0, 1, 1)
        self.amplitudeSlider = QtWidgets.QSlider(self.frame_7)
        self.amplitudeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.amplitudeSlider.setObjectName("amplitudeSlider")
        self.gridLayout_6.addWidget(self.amplitudeSlider, 2, 1, 2, 3)
        self.FcomposeSlider = QtWidgets.QSlider(self.frame_7)
        self.FcomposeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FcomposeSlider.setObjectName("FcomposeSlider")
        self.gridLayout_6.addWidget(self.FcomposeSlider, 1, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)
        self.sinComboBox = QtWidgets.QComboBox(self.frame_7)
        self.sinComboBox.setObjectName("sinComboBox")
        self.gridLayout_6.addWidget(self.sinComboBox, 0, 1, 1, 3)
        self.composeButton = QtWidgets.QPushButton(self.frame_7)
        self.composeButton.setObjectName("composeButton")
        self.gridLayout_6.addWidget(self.composeButton, 4, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.frame_7)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_6.addWidget(self.saveButton, 4, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_7, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.composeLayout = QtWidgets.QVBoxLayout()
        self.composeLayout.setObjectName("composeLayout")
        self.gridLayout_7.addLayout(self.composeLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_6, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.composeTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 26))
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

        # create canvas_1,2,3
        self.canvas_1 = FigureCanvas(plt.figure())
        self.canvas_2 = FigureCanvas(plt.figure())
        self.canvas_3 = FigureCanvas(plt.figure())
        #create canvas_sin for sinwaves
        self.canvas_sin = FigureCanvas(plt.figure())
        self.canvas_added = FigureCanvas(plt.figure())

        # add canvas_1,2,3 in the signalLayout
        self.signalLayout.layout().addWidget(self.canvas_1)
        self.signalLayout.layout().addWidget(self.canvas_2)
        self.signalLayout.layout().addWidget(self.canvas_3)
        #add canvas_sin in the composeLayout
        self.composeLayout.layout().addWidget(self.canvas_sin)
        self.composeLayout.layout().addWidget(self.canvas_added)

        # Connect the "Open" action to the open_csv_file function
        self.actionOpen.triggered.connect(self.open_csv_file)

        # connect Addsinbutton to plot_sinwaves function
        self.addSinButton.clicked.connect(self.update_sine_wave_plot)
        self.addSinButton.mouseDoubleClickEvent(self.update_sine_wave_plot)
        # Connect the slider to the change_frequency function
        self.FcomposeSlider.valueChanged.connect(self.change_frequency)
        # Connect the amplitudeSlider to the change_amplitude function
        self.amplitudeSlider.valueChanged.connect(self.change_amplitude)

        # Initialize default values for frequency and amplitude
        self.frequency = 1.0
        self.amplitude = 1.0

        # initialize empty canvases
        self.init_empty_canvases()

    def init_empty_canvases(self):
        # Create empty subplots for the canvases
        for canvas in [self.canvas_1, self.canvas_2, self.canvas_3, self.canvas_sin, self.canvas_added]:
            canvas.figure.add_subplot(111)

        # Add the empty canvases to the layouts
        self.signalLayout.layout().addWidget(self.canvas_1)
        self.signalLayout.layout().addWidget(self.canvas_2)
        self.signalLayout.layout().addWidget(self.canvas_3)
        self.composeLayout.layout().addWidget(self.canvas_sin)
        self.composeLayout.layout().addWidget(self.canvas_added)


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
            self.canvas_3.figure.clear()
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
       
      
    sinwaves_lst=[]   
    #def create_sinwaves(self): lesa feha sh08l
     

    def sum_sinwaves(sinwaves_lst):
      sum_amplitude = 0
      max_frequency = 0

     # Calculate the sum of amplitudes and find the maximum frequency
      for sinwaves in sinwaves_lst:
        sum_amplitude += sinwaves.amplitude
        if sinwaves.frequency > max_frequency:
            max_frequency = sinwaves.frequency

    # Generate x-axis values
      x = np.linspace(0, 2 * np.pi, 1000)

    # Calculate y-axis values for the summed sine wave
      y_summed = np.zeros_like(x)
      for sinwaves in sinwaves_lst:
        y_summed += sinwaves.amplitude * np.sin(x * sinwaves.frequency * 2 * np.pi)

     # Create a new SinWave object with the maximum frequency and summed amplitude
      summed_wave = sinwaves(max_frequency, sum_amplitude)

    # Plot the summed sine wave
   

      return summed_wave


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
        self.label_2.setText(_translate("MainWindow", "Max Frequency"))
        self.label.setText(_translate("MainWindow", "Sampling Frequency ="))
        self.label_4.setText(_translate("MainWindow", "   SNR   Level     ="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewerTab), _translate("MainWindow", "Viewer"))
        self.removeSinbutton.setText(_translate("MainWindow", "Remove"))
        self.label_7.setText(_translate("MainWindow", "Amplitude ="))
        self.addSinButton.setText(_translate("MainWindow", "Add Sinusoidal"))
        self.label_6.setText(_translate("MainWindow", "Hz"))
        self.label_5.setText(_translate("MainWindow", "Frequency ="))
        self.composeButton.setText(_translate("MainWindow", "Compose"))
        self.saveButton.setText(_translate("MainWindow", "Save As CSV"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.composeTab), _translate("MainWindow", "Composer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))




def main():
    app = QtWidgets.QApplication(sys.argv)  # Create the application instance
    MainWindow = QtWidgets.QMainWindow()  # Create the main window
    ui = Ui_MainWindow()  # Create an instance of the UI class
    ui.setupUi(MainWindow)  # Set up the UI for the main window
    MainWindow.show()  # Display the main window
    sys.exit(app.exec_())  # Run the application event loop

main()