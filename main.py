from SignalRecorder import *
from SDR import *

mySDR = SDR()
mySignalRecorder = SignalRecorder(mySDR)
samples = mySignalRecorder.record_samples(sample_size=256*1024, center_frequency=372e6, sdr_gain='auto')
mySignalRecorder.generate_psd_plot(samples, "Test-Plot-1")