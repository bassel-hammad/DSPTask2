from scipy import fft
import numpy as np
import pandas as pd
class signal():
    def __init__(self):
        self.signal_with_noise=[]
        self.MAX_SAMPLES = 10000
        self.x_data = []
        self.y_data = []
        self.samples_time = []
        self.samples_amplitude = []
        self.fsampling = 1.0
        self.Max_frequency= 0.0
        self.reconstructed=[]
        self.difference_original_reconstructed=[]

    def upload_signal_data(self,x_data,y_data,max_freq=0):
        self.MAX_SAMPLES =10000
        self.fsampling = 1.0
        self.Max_frequency= 0.0
        if(len(x_data)<self.MAX_SAMPLES ):
            self.MAX_SAMPLES = len(x_data)
        self.x_data=np.array(x_data[0:self.MAX_SAMPLES])
        self.y_data=np.array(y_data[0:self.MAX_SAMPLES])
        self.signal_with_noise=self.y_data
        self.Max_frequency= max_freq
        self.fsampling = 2*max_freq
        
       
    def sample_signal(self, sample_freq=-1):
        if sample_freq == -1:
            self.fsampling = 2 * self.Max_frequency
        else:
            self.fsampling = sample_freq
        if self.fsampling == 0:
            # Handle the case when fsampling is zero
            self.reconstructed = np.zeros(self.MAX_SAMPLES)  # Or set it to an appropriate default
            self.samples_time = np.linspace(0, self.x_data[self.MAX_SAMPLES - 1], self.MAX_SAMPLES)
            self.samples_amplitude = np.zeros(self.MAX_SAMPLES)  # Or set it to an appropriate default
            return

        # sample_freq=sample_freq # Nyquist rate (Hz)
        time_step = 1 / self.fsampling  # Time interval between samples (seconds)
        print(self.fsampling)

        # Generate the time array based on the sample frequency
        max_time = self.x_data[self.MAX_SAMPLES - 1]
        sampled_time = np.arange(0, max_time, time_step)

        # Interpolate the amplitude data at the sampled time points
        # https://www.geeksforgeeks.org/numpy-interp-function-python/
        sampled_amplitude = np.interp(sampled_time, self.x_data, self.signal_with_noise)

        self.samples_time = sampled_time
        self.samples_amplitude = sampled_amplitude
        self.fsampling = sample_freq
        self.reconstruct_from_samples()

    def reconstruct_from_samples(self):
        self.reconstructed = np.array([])
        sinc_ = np.sinc(((np.tile(self.x_data, (len(self.samples_time), 1))) - self.samples_time[:, None]) / (self.samples_time[1] - self.samples_time[0]))
        self.reconstructed = np.dot(self.samples_amplitude, sinc_)

    def calc_difference(self):
        self.difference_original_reconstructed = self.y_data - self.reconstructed

    def add_noise(self,snr):
        signal=self.y_data
        signal_power = np.var(self.y_data) # Calculate signal power
        SNR_dB = snr # Set desired SNR in dB
        noise_std = np.sqrt(signal_power / (10 ** (SNR_dB / 10))) # Calculate noise standard deviation
        noise = np.random.normal(0, noise_std, len(signal)) # Generate noise array
        self.signal_with_noise = signal + noise # Add noise to signal
        self.sample_signal(self.fsampling)
        
         