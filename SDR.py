from rtlsdr import RtlSdrAio
from typing import Union

class SDR(RtlSdrAio):
    """ A class used to create and initialize an RtlSdrAio instance with a specific sample rate """

    def __init__(self, sample_rate: float=2.4e6) -> None:
        super().__init__()
        self.sample_rate = sample_rate