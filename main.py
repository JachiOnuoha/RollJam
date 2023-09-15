from SignalRecorder import *
from SDR import *

my_sdr = SDR()
rx_file_name = "Test-Recording-File"
signal_recorder = SignalRecorder(my_sdr)
my_signal_array = signal_recorder.record_samples(signal_array_size=256*1024, center_frequency=372e6, sdr_gain='auto')
signal_recorder.write_signal_to_file(my_signal_array, rx_file_name)
new_signal_array = signal_recorder.read_signal_from_file(rx_file_name)
signal_recorder.generate_psd_plot(new_signal_array, "plots/{}-Plot-1".format(rx_file_name))