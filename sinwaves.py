
from scipy import fft
import numpy as np
from main import *

MAX_SAMPLES = 3000

class sinwaves():
   def __init__(self,amplitude=1,frequency=1):
      
      self.amplitude = amplitude
      self.frequency = frequency
      self.Xaxis=np.linspace(0,2*np.pi,MAX_SAMPLES)
      self.Yaxis=(self.amplitude)/(np.sin(self.Xaxis*self.frequency*2*np.pi))

      def sum_sinwaves(sinwaves_list):
        sum_frequency = 0
        sum_amplitude = 0

    # Calculate the sum of frequencies and amplitudes
        for sinwaves in sinwaves_list:
           sum_frequency += sinwaves.frequency
           sum_amplitude += sinwaves.amplitude

    # Generate x-axis values
        x = np.linspace(0, 2 * np.pi, 1000)

    # Calculate y-axis values for the summed sine wave
        y_summed = sum_amplitude * np.sin(x * sum_frequency * 2 * np.pi)

    # Create a new SinWave object with the summed frequency and amplitude
        summed_wave = sinwaves(sum_frequency, sum_amplitude)

    # return the summed sine wave
        return summed_wave