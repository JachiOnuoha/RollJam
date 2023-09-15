from SignalRecorder import *
from SDR import *

my_sdr = SDR()
signal_recorder = SignalRecorder(my_sdr)
my_signal_array = signal_recorder.record_samples(signal_array_size=256*1024, center_frequency=372e6, sdr_gain='auto')
signal_recorder.generate_psd_plot(my_signal_array, "plots/Test-Plot-1")