from pylab import *
from rtlsdr import RtlSdrAio
from typing import Union

class SignalRecorder:
    def __init__(self, sdr: RtlSdrAio) -> None:
        self.__sdr = sdr

    def record_samples(self, sample_size: float, center_frequency: float, sdr_gain: Union[int, str])-> list[complex]:
        """ Record a signal at a specified center frequency with a specified gain and sample size in bytes

        Parameters
        ----------
        sample_size : `float`
            The size of the recorded signal sample in bytes
        center_frequency : `float`
            A center frequency for the range of the target signal
        sdr_gain : `int` | `str`
        The gain setting for the sdr. It can range from -30 to 30 or can be set to 'auto'
        
        Returns
        -------
        `list[complex]`
            a list of complex numbers which represent the magnitude and phase values of frequnencies recorded by the tuner.
            This will be a :class:`numpy.ndarray` if numpy is available
        """
        
        self.__sdr.center_freq = center_frequency
        self.__sdr.gain = sdr_gain

        samples = self.__sdr.read_samples(sample_size)
        self.__sdr.close()
        return samples
    
    def generate_psd_plot(self, samples:list[complex], plot_name: str) -> None:
        """ Generate a Power Spectral Density(PSD) plot of an array of samples of a given signal recording

        Parameters
        ----------
        samples: `list[complex] | nd.array`
            a list of complex numbers which represent the magnitude and phase values of frequnencies recorded by the tuner.
        plot_name: `str`
            The name that the generated plot image
        Returns
        ----------
        None
        """
        try:
            psd(samples, NFFT=1024, Fs=self.__sdr.sample_rate/1e6, Fc= self.__sdr.center_freq/1e6)
            xlabel("Frequency in MHz")
            ylabel("Magnitude in dB")
            savefig(fname="plots/{}.png".format(plot_name) )
        except:
            print("Failed to plot samples")
