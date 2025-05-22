from .base import (
    GrowattDeviceRegisters,
    custom_function,
    FIRMWARE_REGISTER,
    DEVICE_TYPE_CODE_REGISTER,
    NUMBER_OF_TRACKERS_AND_PHASES_REGISTER,
    ATTR_INPUT_POWER,
    ATTR_INVERTER_MODEL,
    ATTR_MODBUS_VERSION,
    ATTR_SOC_PERCENTAGE,
    ATTR_DISCHARGE_POWER,
    ATTR_CHARGE_POWER,
    ATTR_ENERGY_TO_USER_TODAY,
    ATTR_ENERGY_TO_USER_TOTAL,
    ATTR_ENERGY_TO_GRID_TODAY,
    ATTR_ENERGY_TO_GRID_TOTAL,
    ATTR_DISCHARGE_ENERGY_TODAY,
    ATTR_DISCHARGE_ENERGY_TOTAL,
    ATTR_CHARGE_ENERGY_TODAY,
    ATTR_CHARGE_ENERGY_TOTAL,
    ATTR_AC_CHARGE_ENABLED,
    ATTR_SERIAL_NUMBER,
    ATTR_PAC_TO_GRID_TOTAL,
    ATTR_PAC_TO_USER_TOTAL, ATTR_WARNING_CODE,
    ATTR_FAULT_CODE, ATTR_DERATING_MODE, ATTR_OUTPUT_PERCENTAGE, ATTR_N_BUS_VOLTAGE, ATTR_P_BUS_VOLTAGE,
    ATTR_BOOST_TEMPERATURE, ATTR_IPM_TEMPERATURE, ATTR_TEMPERATURE, ATTR_INPUT_ENERGY_TOTAL, ATTR_COMM_TEMPERATURE,
    ATTR_INPUT_2_ENERGY_TOTAL, ATTR_INPUT_3_ENERGY_TODAY, ATTR_INPUT_3_ENERGY_TOTAL, ATTR_INPUT_2_ENERGY_TODAY,
    ATTR_INPUT_1_ENERGY_TOTAL, ATTR_INPUT_1_ENERGY_TODAY, ATTR_OPERATION_HOURS, ATTR_OUTPUT_ENERGY_TOTAL,
    ATTR_OUTPUT_ENERGY_TODAY, ATTR_OUTPUT_3_POWER, ATTR_OUTPUT_3_AMPERAGE, ATTR_OUTPUT_3_VOLTAGE,
    ATTR_OUTPUT_2_AMPERAGE, ATTR_OUTPUT_2_POWER, ATTR_OUTPUT_2_VOLTAGE, ATTR_OUTPUT_1_POWER, ATTR_OUTPUT_1_AMPERAGE,
    ATTR_OUTPUT_1_VOLTAGE, ATTR_OUTPUT_POWER, ATTR_GRID_FREQUENCY, ATTR_INPUT_4_POWER, ATTR_INPUT_4_AMPERAGE,
    ATTR_INPUT_4_VOLTAGE, ATTR_INPUT_3_POWER, ATTR_INPUT_3_AMPERAGE, ATTR_INPUT_3_VOLTAGE, ATTR_INPUT_2_POWER,
    ATTR_INPUT_2_AMPERAGE, ATTR_INPUT_2_VOLTAGE, ATTR_INPUT_1_POWER, ATTR_INPUT_1_AMPERAGE, ATTR_INPUT_1_VOLTAGE,
    ATTR_STATUS_CODE,
)

MAXIMUM_DATA_LENGTH_120 = 100

def model(registers) -> str:
    mo = (registers[0] << 16) + registers[1]
    return "{:X}".format(mo)


TL_XH_HOLDING_REGISTERS_120: tuple[GrowattDeviceRegisters, ...] = (
    FIRMWARE_REGISTER,
    GrowattDeviceRegisters(
        name=ATTR_SERIAL_NUMBER, register=3001, value_type=str, length=15
    ),
    GrowattDeviceRegisters(
        name=ATTR_INVERTER_MODEL,
        register=3092,
        value_type=custom_function,
        length=2,
        function=model
    ),
    DEVICE_TYPE_CODE_REGISTER,
    NUMBER_OF_TRACKERS_AND_PHASES_REGISTER,
    GrowattDeviceRegisters(
        name=ATTR_MODBUS_VERSION,
        register=88,
        value_type=float,
        scale=100
    ),
    GrowattDeviceRegisters(
        name=ATTR_AC_CHARGE_ENABLED,
        register=3049,
        value_type=int,
        length=1
    ),
)

TL_XH_INPUT_REGISTERS_120: tuple[GrowattDeviceRegisters, ...] = (
GrowattDeviceRegisters(
        name=ATTR_STATUS_CODE, register=3000, value_type=int
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_POWER, register=3001, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_VOLTAGE, register=3003, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_AMPERAGE, register=3004, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_POWER, register=3005, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_VOLTAGE, register=3007, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_AMPERAGE, register=3008, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_POWER, register=3009, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_VOLTAGE, register=3011, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_AMPERAGE, register=3012, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_POWER, register=3013, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_4_VOLTAGE, register=3015, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_4_AMPERAGE, register=3016, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_4_POWER, register=3017, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_POWER, register=3023, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_GRID_FREQUENCY, register=3025, value_type=float, scale=100
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_1_VOLTAGE, register=3026, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_1_AMPERAGE, register=3027, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_1_POWER, register=3028, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_2_VOLTAGE, register=3030, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_2_AMPERAGE, register=3031, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_2_POWER, register=3032, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_3_VOLTAGE, register=3034, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_3_AMPERAGE, register=3035, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_3_POWER, register=3036, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_ENERGY_TODAY, register=3043, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_ENERGY_TOTAL, register=3045, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OPERATION_HOURS, register=3047, value_type=float, length=2, scale=7200,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_ENERGY_TODAY, register=3055, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_ENERGY_TOTAL, register=3057, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_ENERGY_TODAY, register=3059, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_ENERGY_TOTAL, register=3061, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_ENERGY_TODAY, register=3063, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_ENERGY_TOTAL, register=3065, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_ENERGY_TOTAL, register=3053, value_type=float, length=2
    ),
    GrowattDeviceRegisters(name=ATTR_TEMPERATURE, register=3093, value_type=float),
    GrowattDeviceRegisters(name=ATTR_IPM_TEMPERATURE, register=3094, value_type=float),
    GrowattDeviceRegisters(name=ATTR_BOOST_TEMPERATURE, register=3095, value_type=float),
    GrowattDeviceRegisters(name=ATTR_COMM_TEMPERATURE, register=3097, value_type=float),
    GrowattDeviceRegisters(name=ATTR_P_BUS_VOLTAGE, register=3098, value_type=float),
    GrowattDeviceRegisters(name=ATTR_N_BUS_VOLTAGE, register=3099, value_type=float),
    GrowattDeviceRegisters(name=ATTR_OUTPUT_PERCENTAGE, register=3101, value_type=int),
    GrowattDeviceRegisters(name=ATTR_DERATING_MODE, register=3104, value_type=int),
    GrowattDeviceRegisters(name=ATTR_FAULT_CODE, register=3105, value_type=int),
    GrowattDeviceRegisters(
        name=ATTR_WARNING_CODE, register=3106, value_type=int, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_SOC_PERCENTAGE, register=3171, value_type=int
    ),
    GrowattDeviceRegisters(
        name=ATTR_DISCHARGE_POWER, register=3178, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_CHARGE_POWER, register=3180, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_USER_TODAY, register=3067, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_USER_TOTAL, register=3069, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_GRID_TODAY, register=3071, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_GRID_TOTAL, register=3073, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_DISCHARGE_ENERGY_TODAY, register=3125, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_DISCHARGE_ENERGY_TOTAL, register=3127, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_CHARGE_ENERGY_TODAY, register=3129, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_CHARGE_ENERGY_TOTAL, register=3131, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_PAC_TO_USER_TOTAL, register=3041, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_PAC_TO_GRID_TOTAL, register=3043, value_type=float, length=2,
    ),
)