from pylab import *
from rtlsdr import RtlSdrAio
from typing import Union

class SignalRecorder:

    """ A class that manages signal recording and saving
    
    Methods
    -------
    record_samples(signal_array_size: float, center_frequency: float, sdr_gain: Union[int, str])
        Record a signal at a specified center frequency with a specified gain and sample size in bytes
    generate_psd_plot(signal_array:list[complex], plot_name: str, frequency_bin_size: int)
        Generate a Power Spectral Density(PSD) plot of an array of samples of a given signal recording
    write_signal_to_file(signal_array: list[complex], file_name: str)
        Write a recorded signal array to an iq file for further processing
    read_signal_from_file(file_name: str)
        Reads an iq file into a np.complex128 array
    """

    def __init__(self, sdr: RtlSdrAio) -> None:
        self.__sdr = sdr

    def record_samples(self, signal_array_size: float, center_frequency: float, sdr_gain: Union[int, str])-> list[complex64]:
        """ Record a specifc number of data points of signal at a specified center frequency with a specified gain
        Note: The recorded signal is stored in an array of np.complex64 numbers - these are complex numbers whereby each value is a 32-bit float i.e. [32-bit float] + j[32-bit float].
        See https://pysdr.org/content/iq_files.html for futher details

        Parameters
        ----------
        signal_array_size : `float`
            The total number of data points collected for the recorded signal.
        center_frequency : `float`
            A center frequency for the range of the target signal
        sdr_gain : `int` | `str`
        The gain setting for the sdr. It can range from -30 to 30 or can be set to 'auto'
        
        Returns
        -------
        `list[complex64]`
            A list of complex numbers which represent the magnitude and phase values of frequnencies recorded by the tuner.
            This will be a :class:`numpy.ndarray` if numpy is available and will return an array of np.complex64 numbers
        """
        
        self.__sdr.center_freq = center_frequency
        self.__sdr.gain = sdr_gain

        signal_array = self.__sdr.read_samples(signal_array_size)
        signal_array = self.__convert_to_npcomplex64_array(signal_array)
        self.__sdr.close()
        return signal_array
    
    def generate_psd_plot(self, signal_array:list[complex], plot_name: str, frequency_bin_size: int = 1024) -> None:
        """ Generate a Power Spectral Density(PSD) plot of an array of samples of a given signal recording.

        Parameters
        ----------
        signal_array: `list[complex] | nd.array`
            A list of complex numbers which represent the magnitude and phase values of frequnencies recorded by the tuner.
        plot_name: `str`
            The name or filepath of the generated plot image
        frequency_bin_size: `int`, default is 1024
            The number data points in each frequency bins
        
        Returns
        ----------
        None
        """
        try:
            psd(signal_array, NFFT=frequency_bin_size, Fs=self.__sdr.sample_rate/1e6, Fc= self.__sdr.center_freq/1e6)
            xlabel("Frequency in MHz")
            ylabel("Magnitude in dB")
            savefig(fname=plot_name)
        except:
            print("Failed to plot samples")

    def write_signal_to_file(self, signal_array: list[complex], file_name: str)-> None:
        """ Write a recorded signal array to an iq file for further processing

        Parameters
        ----------
        signal_array: `list[complex] | nd.array`
            A list of complex numbers which represent the magnitude and phase values of frequnencies recorded by the tuner.
        file_name: `str`
            The name or file path of the file to be written to.
        
        Returns
        ----------
        None
        """
        signal_array_npcomplex64 = self.__convert_to_npcomplex64_array(signal_array)
        signal_array_npcomplex64.tofile("{}.iq".format(file_name))

    def read_signal_from_file(self, file_name)->list[complex64]:
        """ Reads an iq file into a np.complex64 array

        Parameters
        ----------
        file_name : `str`
           The name or file path of the iq file of the recorded signal

        Returns
        -------
        `list[complex64]`
            A signal array of np.complex64 values
        """

        try:
            result_signal_array = np.fromfile(file="{}.iq".format(file_name), dtype=np.complex64)
            return result_signal_array
        except FileNotFoundError:
            print(FileNotFoundError)
        except:
            print("Failed to read from {}".format(file_name))


    def __convert_to_npcomplex64_array(self, signal_array: list[complex])->list[complex64]:
        """ Converts any signal array into an array of np.complex64 values

        Parameters
        ----------
        signal_array : list[complex]
            A list of complex numbers which represent the magnitude and phase values of frequnencies recorded by the tuner.

        Returns
        -------
        list[complex64]
            A list of np.complex64 numbers
        """
        if type(signal_array[0]) != complex64:
            signal_array = signal_array.astype(np.complex64)
        return signal_array
