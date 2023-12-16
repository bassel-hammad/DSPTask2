import sys
import os
import csv
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
        self.sinwaves_lst = []
        self.currentSinIndex = 0
        self.x = np.linspace(0, 2 * np.pi, 1000)
        self.count = 1
        # Initialize default values for frequency and amplitude
        self.frequency = 1.0
        self.amplitude = 1.0
        self.count=1

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
        self.Max_freq_Display = QtWidgets.QLCDNumber(self.frame_4)
        self.Max_freq_Display.setObjectName("Max_freq_Display")
        self.gridLayout_5.addWidget(self.Max_freq_Display, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.SNR_Slider = QtWidgets.QSlider(self.frame_4)
        self.SNR_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.SNR_Slider.setObjectName("SNR_Slider")
        self.SNR_Slider.setRange(0,30)
        self.SNR_Slider.setSingleStep(10)
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

        self.my_siganl = signal()
        self.my_siganl.upload_signal_data([1, 2], [2, 3])

        # create canvas_1,2,3
        self.canvas_1 = FigureCanvas(plt.figure())
        self.canvas_2 = FigureCanvas(plt.figure())
        self.canvas_3 = FigureCanvas(plt.figure())
        # create canvas_sin for sinwaves
        self.canvas_sin = FigureCanvas(plt.figure())
        self.canvas_added = FigureCanvas(plt.figure())

        # add canvas_1,2,3 in the signalLayout
        self.signalLayout.layout().addWidget(self.canvas_1)
        self.signalLayout.layout().addWidget(self.canvas_2)
        self.signalLayout.layout().addWidget(self.canvas_3)
        # add canvas_sin in the composeLayout
        self.composeLayout.layout().addWidget(self.canvas_sin)
        self.composeLayout.layout().addWidget(self.canvas_added)

        # Connect the "Open" action to the open_csv_file function
        self.actionOpen.triggered.connect(self.open_csv_file)

        # connect Addsinbutton to plot_selected_sinwaves function
        self.addSinButton.clicked.connect(self.create_new_sinwave)
        # self.addSinButton.clicked.connect(self.plot_selected_sinwave)

        # Connect the slider to the change_frequency function
        self.FcomposeSlider.valueChanged.connect(self.change_frequency)
        # Connect the amplitudeSlider to the change_amplitude function
        self.amplitudeSlider.valueChanged.connect(self.change_amplitude)

        # Initialize default values for frequency and amplitude
        self.frequency = 1.0
        self.amplitude = 1.0

        # initialize empty canvases
        self.init_empty_canvases()

        # siganl of sliders
        self.FsampleSlider.valueChanged.connect(self.my_siganl.sample_signal)
        self.FsampleSlider.valueChanged.connect(self.draw_plots)
        self.SNR_Slider.valueChanged.connect(self.my_siganl.add_noise)
        self.SNR_Slider.valueChanged.connect(self.draw_plots)


        self.saveButton.clicked.connect(self.save_plot_data_as_csv)
        # Connect the currentIndexChanged signal of the combo box to the slot function
        # self.sinComboBox.currentIndexChanged.connect(self.plot_selected_sinwave)
        self.sinComboBox.currentIndexChanged.connect(self.change_currentSinIndex)
        self.sinComboBox.currentIndexChanged.connect(self.plot_selected_sinwave)
        self.removeSinbutton.clicked.connect(self.RemoveSinwave)


        #connect composeButton => to move created signal to studio
        self.composeButton.clicked.connect(self.load_Composed)

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
            time = df.iloc[:, 0]
            magnitude = df.iloc[:, 1]
            # self.MySignal(time,magnitude)
            self.update_signal_data(time,magnitude)

    def update_signal_data(self,signal_time,signal_magnitude,max_freq=0):
        self.my_siganl.upload_signal_data(signal_time, signal_magnitude,max_freq)

        self.FsampleSlider.setRange(0, int(10 * self.my_siganl.Max_frequency))
        self.FsampleSlider.setValue(2*int(self.my_siganl.Max_frequency))
        self.FsampleDisp.display(int(self.FsampleSlider.value()))
        self.FsampleSlider.setSingleStep(int(self.my_siganl.Max_frequency))
        self.Max_freq_Display.display(int(self.my_siganl.Max_frequency))
        # Clear the previous plot
        self.my_siganl.sample_signal()
        self.draw_plots()


    def draw_plots(self):
        self.canvas_1.figure.clear()
        self.canvas_2.figure.clear()
        self.canvas_3.figure.clear()
        # Create a new plot and display it
        self.FsampleDisp.display(self.FsampleSlider.value())
        
        ax = self.canvas_1.figure.add_subplot(1, 1, 1)
        ax.plot(self.my_siganl.x_data, self.my_siganl.signal_with_noise, linewidth=3)
        ax.set_xlabel("Time")
        ax.set_ylabel("Magnitude")
        ax.set_title("Original Signal")
        ax.grid(True)
        ax.plot(self.my_siganl.samples_time, self.my_siganl.samples_amplitude, 'ro', markersize=3,
                label='Sampled Signal')
        ax_reconstructed = self.canvas_2.figure.add_subplot(1, 1, 1)
        ax_reconstructed.set_xlabel("Time")
        ax_reconstructed.set_ylabel("Magnitude")
        ax_reconstructed.set_title("Reconstructed Signal")
        ax_reconstructed.grid(True)
        ax_reconstructed.plot(self.my_siganl.x_data, self.my_siganl.reconstructed, linewidth=3)
        self.my_siganl.calc_difference()
        ax_difference = self.canvas_3.figure.add_subplot(1, 1, 1)
        ax_difference.set_xlabel("Time")
        ax_difference.set_ylabel("Magnitude")
        ax_difference.set_title("ax_difference Signal")
        ax_difference.grid(True)
        ax_difference.plot(self.my_siganl.x_data, self.my_siganl.difference_original_reconstructed, linewidth=3)

        # Redraw the canvas
        self.canvas_1.draw()
        self.canvas_2.draw()
        self.canvas_3.draw()

    def change_currentSinIndex(self):
        self.currentSinIndex = self.sinComboBox.currentIndex()
        print("currentSinIndex " + str(self.currentSinIndex))
        for sinwave in self.sinwaves_lst:
            print(f"Name: {sinwave.name}, Frequency: {sinwave._frequency}, Amplitude: {sinwave._amplitude}")

    def create_new_sinwave(self):

        self.frequency = 1.0
        self.amplitude = 1.0

        new_sinwaves = sinwaves(frequency=self.frequency, amplitude=self.amplitude)
        new_sinwaves.name = f"SineWave{self.count}"
        self.count+=1

        self.sinwaves_lst.append(new_sinwaves)

        # call Function updateComboBox To add names of waves in comboBox
        self.updateComboBox()

        self.sinComboBox.setCurrentIndex(len(self.sinwaves_lst) - 1)

        self.plot_selected_sinwave()

    def plot_selected_sinwave(self):

        if (len(self.sinwaves_lst) == 0):
            self.canvas_sin.figure.clear()
            self.canvas_added.figure.clear()
            return

        # Get the index of the selected sinwave
        selected_sinwave = self.sinwaves_lst[self.currentSinIndex]

        # Clear the canvas for the selected sinwave
        self.canvas_sin.figure.clear()
        ax = self.canvas_sin.figure.add_subplot(111)

        # Plot the selected sinwave
        ax.plot(selected_sinwave.Xaxis, selected_sinwave.Yaxis)
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
        ax.set_title(f"Sine Wave (Frequency: {selected_sinwave._frequency} Hz,"
                     f" Amplitude: {selected_sinwave._amplitude})")
        ax.grid(True)

        # Redraw the canvas
        self.canvas_sin.draw()

        self.plot_composer()

    def change_frequency(self, value):
        # Get the slider value and use it to update the frequency
        self.frequency = value / 10.0  # You may need to adjust this scaling factor
        if self.sinwaves_lst:  # Check if there are sine waves in the list
            if 0 <= self.currentSinIndex < len(self.sinwaves_lst):
                selected_sinwave = self.sinwaves_lst[self.currentSinIndex]
                selected_sinwave.set_frequency(self.frequency)
                selected_sinwave.update_data()
                self.plot_selected_sinwave()  # Update the plot

    def change_amplitude(self, value):
        # Get the slider value and use it to update the frequency
        self.amplitude = value / 10.0  # You may need to adjust this scaling factor
        if self.sinwaves_lst:  # Check if there are sine waves in the list
            if 0 <= self.currentSinIndex < len(self.sinwaves_lst):
                selected_sinwave = self.sinwaves_lst[self.currentSinIndex]
                selected_sinwave.set_amplitude(self.amplitude)
                selected_sinwave.update_data()
                self.plot_selected_sinwave()  # Update the plot

    def save_plot_data_as_csv(self):
        filename = f"composer_data{self.count}.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            y = self.sum_sinwaves()
            writer.writerow(['x', 'y'])
            for i in range(len(self.x)):
                writer.writerow([self.x[i], y[i]])

        self.count += 1

    def plot_composer(self):
        self.canvas_added.figure.clear()
        ax = self.canvas_added.figure.add_subplot(111)
        y = self.sum_sinwaves()
        # Plot the selected sinwave with the updated frequency
        ax.plot(self.x, y)
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
        ax.grid(True)


        # Redraw the canvas
        self.canvas_added.draw()

    def sum_sinwaves(self):
        sum_amplitude = 0
        self.max_frequency = 0
        y_summed = 0
        # Calculate the sum of amplitudes and find the maximum frequency
        for sinwaves in self.sinwaves_lst:
            sum_amplitude += sinwaves.get_amplitude()
            if sinwaves.get_frequency() > self.max_frequency:
                self.max_frequency = sinwaves.get_frequency()

        # Calculate y-axis values for the summed sine wave
        for sinwaves in self.sinwaves_lst:
            y_summed += sinwaves.Yaxis
        # RETURN Y_SUMMED TO PLOT IT

        return y_summed
    
    def RemoveSinwave(self):

        if(len(self.sinwaves_lst)!=0):
         index = self.sinComboBox.currentIndex()
         self.sinwaves_lst.pop(index)
        self.updateComboBox()
        self.sum_sinwaves()





    # add sinwaves names to comboBox
    def updateComboBox(self):
        self.sinComboBox.clear()  # Clear the existing items
        for sinwave in self.sinwaves_lst:
            self.sinComboBox.addItem(sinwave.name)

    #fuction to move created signal  to viewer to try Sample & Recover:
    def load_Composed(self):
        y = self.sum_sinwaves()
        self.update_signal_data(self.x,y,self.max_frequency)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Sampling Frequency"))
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
