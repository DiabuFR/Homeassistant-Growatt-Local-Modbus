"""Constants for growattRS232 library."""

# Defaults
from enum import Enum


DEFAULT_PORT = "/dev/ttyUSB0"
DEFAULT_ADDRESS = 0x1


# Supported devices
class DeviceTypes(str, Enum):
    INVERTER = "inverter"
    INVERTER_120 = "inverter_120"
    STORAGE_120 = "storage_120"
    HYBRIDE_120 = "hybride_120"
    TL_XH_120 = "tl-xh_120"
    INVERTER_315 = "inverter_315"
    OFFGRID_SPF = "offgrid_SPF"



# Unit of measurement
ELECTRICAL_POTENTIAL_VOLT = "V"
ELECTRICAL_CURRENT_AMPERE = "A"
POWER_WATT = "W"
REACTIVE_POWER_VAR = "var"
TIME_HOURS = "h"
ENERGY_KILO_WATT_HOUR = "kWh"
REACTIVE_ENERGY_KILO_VAR_HOUR = "kvarh"
FREQUENCY_HERTZ = "Hz"
TEMP_CELSIUS = "°C"
