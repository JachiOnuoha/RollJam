from pylab import *
from enum import Enum
from scipy import signal
from SignalFilter import *

class SignalProcessor:
    
    def __init__(self) -> None:
        pass
        
    def apply_lowpass_filter(signal_array:list[complex64], cutoff_frequency: float, sampling_rate: float, poles: int=5, custom_filter: SignalFilter = None)->list[complex64]:
        """
        Apply a lowpass filter to a signal array.

        Parameters
        ----------
        signal_array : list[complex64]
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
        list[complex64]
            A filtered version of the original signal array 
        """
        filter = custom_filter

        # Create butterworth lowpass filter if no custom filter or non-lowpass filter is provided
        if filter == None | filter.filter_type != FilterType.LOWPASS:
            sos = signal.butter(N=poles, Wn=cutoff_frequency, btype='low',fs=sampling_rate, output='sos')
            filter = sos
        
        filtered_signal_array = signal.sosfiltfilt(filter, signal_array)
        return filtered_signal_array

    def apply_highpass_filter(signal_array:list[complex64], cutoff_frequency: float, sampling_rate: float, poles: int, custom_filter: list[float]= None)->list[complex64]:
        pass

    def apply_bandpass_filter(signal_array:list[complex64], cutoff_frequency: float, sampling_rate: float, poles: int, custom_filter: list[float]= None)->list[complex64]:
        pass