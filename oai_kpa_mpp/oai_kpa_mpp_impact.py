try:
    import OAI_Modbus
except ImportError:
    from oai_modbus import OAI_Modbus


class MPP_Registers_DAC:
    def __init__(self, **kwargs):
        self.channel = kwargs.get('channel', 1)
        if self.channel == 1:
            self.scaler_addr = 1393
        elif self.channel == 2:
            self.scaler_addr = 1400
        else:
            raise Exception('Incorrect MPP_Register_DAC channel')
        self.U0_addr = self.scaler_addr + 1  # low voltage level (from 0: -15V to 4095: +15V)
        self.U1_addr = self.scaler_addr + 2  # high voltage level (from 0: -15V to 4095: +15V)
        self.N_addr = self.scaler_addr + 3  # the amount of pulse in a batch (from 0 to 125)
        self.M_addr = self.scaler_addr + 4  # the amount of batches in impact (from 0 to 255)
        self.T_addr = self.scaler_addr + 5  # impact period (from 0 to 65535 ms)
        self.t_addr = self.scaler_addr + 6  # pulse period (from 0 to 25.5 ms)


class ImpactModuleMPP:
    def __init__(self, **kwargs):
        self.client = None
        self.connection_status = False
        self.channel: int = kwargs.get('channel', 1)
        self.dac_struct: MPP_Registers_DAC = MPP_Registers_DAC(channel=self.channel)
        self.low_voltage_level_adc: int = 0  # low voltage level (from 0: -15V to 4095: +15V)
        self.high_voltage_level_adc: int = 0  # high voltage level (from 0: -15V to 4095: +15V)
        self.amount_of_pulse: int = 0  # the amount of pulse in a batch (from 0 to 125)
        self.amount_of_batches: int = 0  # the amount of batches in impact (from 0 to 255)
        self.impact_period: int = 0  # impact period (from 0 to 65535 ms)
        self.pulse_period: int = 0  # pulse period (from 0 to 25.5 ms)

        self.dac_struct_array = [0, 0, 0, 0, 0, 0]

    def set_client(self, client: OAI_Modbus):
        self.client = client

    # def connect(self):
    #     self.connection_status = self.client.connect()
    #     return self.connection_status
    #
    # def disconnect(self):
    #     self.client.disconnect()
    #     self.connection_status = False

    @staticmethod
    def _voltage_to_adc_converter(voltage: float) -> int:
        if -15.0 > voltage or voltage > 15.0:
            raise Exception('Incorrect voltage level for ImpactModuleMPP')
        volt_per_bit: float = 30 / 4095
        return int(voltage / volt_per_bit) + 2048

    def set_low_voltage_level(self, voltage: float) -> None:
        u0_adc = self._voltage_to_adc_converter(voltage)
        self.low_voltage_level_adc = u0_adc
        self.dac_struct_array[0] = u0_adc

    def set_high_voltage_level(self, voltage: float) -> None:
        u1_adc = self._voltage_to_adc_converter(voltage)
        self.high_voltage_level_adc = self._voltage_to_adc_converter(voltage)
        self.dac_struct_array[1] = u1_adc

    def set_amount_of_pulse(self, num: int) -> None:
        if num < 0 or num > 125:
            raise Exception('Incorrect amount of pulse in a batch for ImpactModuleMPP')
        self.amount_of_pulse = num
        self.dac_struct_array[2] = num

    def set_amount_of_batches(self, num: int) -> None:
        if num < 0 or num > 255:
            raise Exception('Incorrect amount of batches for ImpactModuleMPP')
        self.amount_of_batches = num
        self.dac_struct_array[3] = num

    def set_impact_period(self, time_ms: int) -> None:
        if time_ms < 0 or time_ms > 65535:
            raise Exception('Incorrect impact period for ImpactModuleMPP')
        self.impact_period = time_ms
        self.dac_struct_array[4] = time_ms

    def set_pulse_period(self, time_ms: float) -> None:
        if time_ms < 0 or time_ms > 25.5:
            raise Exception('Incorrect amount of batches for ImpactModuleMPP')
        self.pulse_period = int(time_ms * 10)
        self.dac_struct_array[5] = int(time_ms * 10)

    def init_impact_parameters(self, U0: float, U1: float, N: int, M: int, T: int, t: int):
        if U0 >= U1:
            raise Exception("Incorrect voltage level for ImpactModuleMPP. U0 is bigger then U1 or equals")
        self.set_low_voltage_level(U0)
        self.set_high_voltage_level(U1)
        self.set_amount_of_pulse(N)
        self.set_amount_of_batches(M)
        self.set_impact_period(T)
        self.set_pulse_period(t)

        self.dac_struct_array = [self.low_voltage_level_adc,
                                 self.high_voltage_level_adc,
                                 self.amount_of_pulse,
                                 self.amount_of_batches,
                                 self.impact_period,
                                 self.pulse_period]

    def write_impact_parameters(self):
        self.client.write_regs(offset=self.dac_struct.U0_addr, data_list=self.dac_struct_array)

    def start_impact(self):
        self.client.write_regs(offset=self.dac_struct.scaler_addr, data_list=[1])

    def get_impact_parameters(self) -> dict:
        return {'U0adc': self.low_voltage_level_adc, 'U1adc': self.high_voltage_level_adc,
                'N': self.amount_of_pulse, 'M': self.amount_of_batches,
                'T': self.impact_period, 't': self.pulse_period, 'channel': self.channel}


if __name__ == '__main__':
    impModule = ImpactModuleMPP()
    impModule.init_impact_parameters(U0=-15.0, U1=6.0, N=11, M=17, T=256, t=10)
    print(impModule.get_impact_parameters())
    print(impModule.dac_struct_array)
    impModule.set_amount_of_pulse(1)
    print(impModule.dac_struct_array)
