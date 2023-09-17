from enum import Enum
from scipy import signal

class FilterType(Enum):
    """
    An enumeration of different filter types namely: lowpass, highpass and bandpass
    """
    LOWPASS = "lowpass"
    HIGHPASS = "highpass"
    BANDPASS = "bandpass"

class SignalFilter:
    """
    A custom signal filter
    """
    def __init__(self, filter_type: FilterType, cutoff_frequencies: list[float], num_taps: int, sampling_rate: float) -> None:
         #TODO: Update docstring to contain class docstring
        """_summary_

        Parameters
        ----------
        filter_type : FilterType
            _description_
        cutoff_frequencies : list[float]
            _description_
        num_taps : int
            _description_
        sampling_rate : float
            _description_
        """

        self.filter_type = filter_type
        self.cutoff_frequencies = cutoff_frequencies
        self.num_taps = num_taps
        self.sampling_rate = sampling_rate
        self.filter = self.__create_firwin_filter(cutoff_frequencies, num_taps, sampling_rate)
    
    
    def __create_firwin_filter(self, cutoff_frequencies: list[float], num_taps: int, sampling_rate: float)-> list[float]:
        """
        Design a custom FIR filter using the window method

        Parameters
        ----------
        cutoff_frequencies : list[float]
           The cutoff frequencies to be used in the filter. Provide two for bandpass and bandstop filters but, only one for highpass and lowpass filters
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
    
    @staticmethod
    def create_firwin_filter(self, cutoff_frequencies: list[float], num_taps: int, sampling_rate: float)-> list[float]:
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