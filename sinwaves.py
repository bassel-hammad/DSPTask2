
from scipy import fft
import numpy as np
from main import *

MAX_SAMPLES = 3000

class sinwaves():
   def __init__(self,amplitude=1,frequency=1):
      
      self.amplitude = amplitude
      self.frequency = frequency
      self.Xaxis=np.linspace(0, 2 * np.pi, 1000)
      self.Yaxis=self.amplitude * np.sin(2 * np.pi * self.frequency * self.Xaxis)

      def add(self,sinwaves1):
         return sinwaves1.Yaxis + self.Yaxis
      def Getfrequncy(self):
         return self.frequency

   def update_frequency(self,newFrequency):
      self.frequency = newFrequency
      return self.frequency

   def update_data(self, num_points=1000):
      # Generate the X-axis values (time)
      Xaxis = np.linspace(0, 2 * np.pi, 1000)

      # Generate the Y-axis values based on the current frequency and amplitude

      self.Yaxis = self.amplitude * np.sin(2 * np.pi * self.frequency * Xaxis)