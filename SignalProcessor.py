from enum import Enum
from pylab import *
from scipy import signal

class FilterType(Enum):
    """
    An enumeration of different filter types namely: lowpass, highpass and bandpass
    """
    LOWPASS = "lowpass"
    HIGHPASS = "highpass"
    BANDPASS = "bandpass"

class SignalProcessor:
    
    def __init__(self) -> None:
        pass

    def design_custom_filter(signal_array: list[complex64], filter_type: FilterType, cutoff_frequencies: list[float], num_taps: int, sampling_rate: float)-> list[float]:
        """
        Design a custom FIR filter using the window method

        Parameters
        ----------
        signal_array : list[complex64]
            _description_
        filter_type : FilterType
            _description_
        cutoff_frequency : list[float]
            _description_
        num_taps : int
            _description_
        sampling_rate : float
            _description_

        Returns
        -------
        list[float]
            _description_
        """
        custom_filter = signal.firwin(num_taps, cutoff_frequencies, sampling_rate)
        return custom_filter
        
    def apply_lowpass_filter(signal_array:list[complex64], cutoff_frequency: float, sampling_rate: float, poles: int=5, custom_filter: list[float]= None)->list[complex64]:
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
        custom_filter : list[float], optional
           A custom lowpass filter which can be applied to the signal array, by default None

        Returns
        -------
        list[complex64]
            A filtered version of the original signal array 
        """
        filter = custom_filter
        # Create lowpass filter if butterworth lowpass filter
        if filter == None:
            sos = signal.butter(N=poles, Wn=cutoff_frequency, btype='low',fs=sampling_rate, output='sos')
        filtered_signal_array = signal.sosfiltfilt(sos, signal_array)
        return filtered_signal_array

    def apply_highpass_filter(signal_array:list[complex64], cutoff_frequency: float, sampling_rate: float, poles: int, custom_filter: list[float]= None)->list[complex64]:
        pass

    def apply_bandpass_filter(signal_array:list[complex64], cutoff_frequency: float, sampling_rate: float, poles: int, custom_filter: list[float]= None)->list[complex64]:
        pass