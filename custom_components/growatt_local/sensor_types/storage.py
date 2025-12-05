"""Growatt Sensor definitions for the Inverter type."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    UnitOfEnergy,
    UnitOfPower,
    PERCENTAGE, UnitOfTemperature, UnitOfElectricCurrent, UnitOfElectricPotential,
)
from .sensor_entity_description import GrowattSensorEntityDescription
from .switch_entity_description import GrowattSwitchEntityDescription

from ..API.device_type.base import (
    ATTR_AC_CHARGE_ENABLED,
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
    ATTR_PAC_TO_GRID_TOTAL,
    ATTR_PAC_TO_USER_TOTAL, ATTR_FLAGS, ATTR_NTC_TEMPERATURE, ATTR_BB_TEMPERATURE, ATTR_BATTERY_CURRENT,
    ATTR_BATTERY_VOLTAGE, ATTR_WARNING_CODE, ATTR_FAULT_CODE, ATTR_WORKING_MODE,
)

STORAGE_SWITCH_TYPES: tuple[GrowattSwitchEntityDescription, ...] = (
    GrowattSwitchEntityDescription(
        key=ATTR_AC_CHARGE_ENABLED,
        name="AC Charge",
        state_on=0x1,
        state_off=0x0
    ),
)


STORAGE_SENSOR_TYPES: tuple[GrowattSensorEntityDescription, ...] = (
    GrowattSensorEntityDescription(
        key=ATTR_SOC_PERCENTAGE,
        name="SOC",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_DISCHARGE_POWER,
        name="Discharge Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_CHARGE_POWER,
        name="Charge Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_GRID_TOTAL,
        name="Energy To Grid (Total)",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_GRID_TODAY,
        name="Energy To Grid (Today)",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_USER_TOTAL,
        name="Energy To User (Total)",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),

    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_USER_TODAY,
        name="Energy To User (Today)",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_AC_CHARGE_ENABLED,
        name="AC Charge Enabled",
    ),
    GrowattSensorEntityDescription(
        key=ATTR_DISCHARGE_ENERGY_TODAY,
        name="Battery Discharged (Today)",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_DISCHARGE_ENERGY_TOTAL,
        name="Battery Discharged (Total)",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_CHARGE_ENERGY_TODAY,
        name="Battery Charged (Today)",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_CHARGE_ENERGY_TOTAL,
        name="Battery Charged (Total)",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_PAC_TO_USER_TOTAL,
        name="AC to user total",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_PAC_TO_GRID_TOTAL,
        name="AC to grid total",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
)

def bms_sensors(bdc_id:int) -> tuple[GrowattSensorEntityDescription, ...]:
    from custom_components.growatt_local.API.device_type.tl_xh_120 import BMS_PREFIX_FMT
    key_prefix = BMS_PREFIX_FMT.format(bdc_id)
    name_prefix = "BMS {:d} ".format(bdc_id)
    return (
        GrowattSensorEntityDescription(
            key=key_prefix + ATTR_WORKING_MODE,
            name=name_prefix + "Working Mode",
        ),
        GrowattSensorEntityDescription(
            # TODO: Render as string
            key=key_prefix + ATTR_FAULT_CODE,
            name=name_prefix + "Fault Code",
        ),
        GrowattSensorEntityDescription(
            # TODO: Render as string
            key=key_prefix + ATTR_WARNING_CODE,
            name=name_prefix+"Warning Code",
        ),
        GrowattSensorEntityDescription(
            key=key_prefix+ATTR_BATTERY_VOLTAGE,
            name=name_prefix+"Voltage",
            native_unit_of_measurement=UnitOfElectricPotential.VOLT,
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        GrowattSensorEntityDescription(
            key=key_prefix+ATTR_BATTERY_CURRENT,
            name=name_prefix+"Amperage",
            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE ,
            device_class=SensorDeviceClass.CURRENT,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        GrowattSensorEntityDescription(
            key=key_prefix+ATTR_SOC_PERCENTAGE,
            name=name_prefix+"SOC",
            native_unit_of_measurement=PERCENTAGE,
            device_class=SensorDeviceClass.BATTERY
        ),
        GrowattSensorEntityDescription(
            key=key_prefix+ATTR_NTC_TEMPERATURE,
            name=name_prefix+"NTC Temperature",
            native_unit_of_measurement=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
        ),
        GrowattSensorEntityDescription(
            key=key_prefix+ATTR_BB_TEMPERATURE,
            name=name_prefix+"BB Temperature",
            native_unit_of_measurement=UnitOfTemperature.CELSIUS,
            device_class=SensorDeviceClass.TEMPERATURE,
        ),
        GrowattSensorEntityDescription(
            key=key_prefix+ATTR_DISCHARGE_POWER,
            name=name_prefix+"Discharge Power".format(bdc_id),
            native_unit_of_measurement=UnitOfPower.WATT,
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        GrowattSensorEntityDescription(
            key=key_prefix+ATTR_CHARGE_POWER,
            name=name_prefix+"Charge Power".format(bdc_id),
            native_unit_of_measurement=UnitOfPower.WATT,
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        GrowattSensorEntityDescription(
            key=key_prefix+ATTR_DISCHARGE_ENERGY_TOTAL,
            name=name_prefix+"Discharged (Total)".format(bdc_id),
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
        ),
        GrowattSensorEntityDescription(
            key=key_prefix+ATTR_CHARGE_ENERGY_TOTAL,
            name=name_prefix+"Charged (Total)".format(bdc_id),
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
        ),
        GrowattSensorEntityDescription(
            # TODO: Render better
            key=key_prefix+ATTR_FLAGS,
            name=name_prefix+"Flags",
        ),
    )