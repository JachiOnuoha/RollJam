from pylab import *
from SDR import *
from SignalRecorder import *
from SignalProcessor import *



# my_sdr = SDR()
# rx_file_name = "Test-Recording-File"
# signal_recorder = SignalRecorder(my_sdr)
# my_signal_array = signal_recorder.record_samples(signal_array_size=256*1024, center_frequency=372e6, sdr_gain='auto')
# signal_recorder.write_signal_to_file(my_signal_array, rx_file_name)
# new_signal_array = signal_recorder.read_signal_from_file(rx_file_name)
# signal_recorder.generate_psd_plot(new_signal_array, "plots/{}-Plot-1".format(rx_file_name))

# mock_signal, mock_time_shift_vector = SignalProcessor.generate_sample_tone_with_noise(2.4e6, 1024*1000, 372e6)
# SignalProcessor.plot_time_domain_signal(mock_time_shift_vector[:200], mock_signal[:200], 2.4e6)
my_sig_processor = SignalProcessor()
sampling_rate = 1e6
time_shift_vector = np.arange(1000)/sampling_rate # time vector

signal_one = np.sin(2 * np.pi * 10e3 * time_shift_vector)
signal_two = np.sin(2 * np.pi * 20e3 * time_shift_vector)
signal_sum = np.sin(2 * np.pi * 10e3 * time_shift_vector) + np.sin(2 * np.pi * 20e3 * time_shift_vector)
filtered_signal = my_sig_processor.apply_lowpass_filter(signal_sum, 20e3, sampling_rate)

my_sig_processor.plot_time_domain_signal(time_shift_vector, signal_two, sampling_rate, "20MHz-Signal")
# my_sig_processor.plot_time_domain_signal(time_shift_vector, signal_sum, sampling_rate, "Summed-10MHz-and-20MHz")
my_sig_processor.plot_time_domain_signal(time_shift_vector, filtered_signal, sampling_rate, "Filtered-Summed-10MHz-and-20MHz")