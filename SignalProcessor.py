from typing import Tuple, Union
from matplotlib import pyplot
from pylab import *
from enum import Enum
from scipy import signal
from SignalFilter import *

class SignalProcessor:
    
    def __init__(self) -> None:
        pass
        
    def apply_lowpass_filter(self, signal_array: Union[list[complex64], list[float]], 
                             cutoff_frequency: float, 
                             sampling_rate: float, 
                             poles: int=5, 
                             custom_filter: SignalFilter = None)->Union[list[complex64], list[float]]:
        """
        Apply a lowpass filter to a signal array.

        Parameters
        ----------
        signal_array : list[complex64] | list[float]
            The signal, in array form, to be filtered
        cutoff_frequency : float
            The desired cutoff frequency of the filter
        sampling_rate : float
            The sampling rate at which the signal was recorded
        poles : int, optional
            The order of the filter by default 5
        custom_filter : SignalFilter, optional
           A custom lowpass filter which can be applied to the signal array, by default None

        Returns
        -------
        list[complex64] | list[float]
            A filtered version of the original signal array 
        """
        filter = custom_filter

        # Create butterworth lowpass filter if no custom filter or non-lowpass filter is provided
        if filter == None:
            sos = signal.butter(N=poles, Wn=cutoff_frequency, btype='low',fs=sampling_rate, output='sos')
            filter = sos
        
        filtered_signal_array = signal.sosfiltfilt(filter, signal_array)
        return filtered_signal_array

    def apply_highpass_filter(self, signal_array:list[complex64], cutoff_frequency: float, sampling_rate: float, poles: int, custom_filter: list[float]= None)->list[complex64]:
        pass

    def apply_bandpass_filter(self, signal_array:list[complex64], cutoff_frequency: float, sampling_rate: float, poles: int, custom_filter: list[float]= None)->list[complex64]:
        pass

    #TODO: Move this to an example class 
    @staticmethod
    def generate_sample_tone_with_noise(sampling_rate: float, time_shift_vector_size: float, tone_frequency: float)->Tuple[list[float], list[float]]:
        """_summary_

        Parameters
        ----------
        sampling_rate : float
            _description_
        time_shift_vector_size : float
            _description_
        tone_frequency : float
            _description_

        Returns
        -------
        Tuple[list[float], list[float]]
            _description_
        """
        time_shift_vector = np.arange(time_shift_vector_size)/sampling_rate
        noise = 0.2*np.random.randn(len(time_shift_vector))
        signal = np.sin(2 * np.pi * tone_frequency * time_shift_vector)
        signal_with_noise = signal + noise
        return signal_with_noise, time_shift_vector
    
    #TODO: Move this to an example class 
    def plot_time_domain_signal(self, time_shift_vector: list[float], signal: list[float], sampling_rate: float, file_name: str)-> None:
        """_summary_

        Parameters
        ----------
        time_shift_vector : list[float]
            _description_
        signal : list[float]
            _description_
        sampling_rate : float
            _description_
        file_name : str
            _description_
        """
        plot(time_shift_vector*sampling_rate, signal)
        # plt.locator_params(axis='x', nbins=10)
        xlabel("Time Domain")
        ylabel("Amplitude")
        savefig(file_name)
