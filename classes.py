from scipy import fft
import numpy as np

MAX_SAMPLES = 3000
class sinwaves():
   def __init__(self,index=0,amplitude=1,frequency=1,added=False):   
      self.index = index
      self.amplitude = amplitude
      self.frequency = frequency
      self.added = added
      self.Xaxis=np.linspace(0,2*np.pi,MAX_SAMPLES)
      self.Yaxis=(self.amplitude)/(np.sin(self.Xaxis*self.frequency*2*np.pi))

      def add(self,sinwaves1):
         return sinwaves1.Yaxis + self.Yaxis
      def Getfrequncy(self):
         return self.frequency