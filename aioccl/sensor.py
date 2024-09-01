from __future__ import annotations

from dataclasses import dataclass
import enum
from typing import TypedDict

class CCLSensor:
    """Class that represents a CCLSensor object in the aioCCL API."""
    
    def __init__(self, key: str):
        """Initialize a CCL sensor."""
        self._value: None | str | int | float = None
    
        if key in CCL_SENSORS.keys():
            self._key = key
    
    @property
    def key(self) -> str:
        return self._key
    
    @property
    def name(self) -> str:
        return CCL_SENSORS[self._key].name
    
    @property
    def sensor_type(self) -> CCLSensorTypes:
        return CCL_SENSORS[self._key].sensor_type
    
    @property
    def compartment(self) -> None | str:
        if CCL_SENSORS[self._key].compartment is not None:
            return CCL_SENSORS[self._key].compartment.value
    
    @property
    def binary(self) -> bool:
        return CCL_SENSORS[self._key].binary

    @property
    def value(self) -> None | str | int | float:
        if self.sensor_type.name in CCL_SENSOR_VALUES:
            return CCL_SENSOR_VALUES[self.sensor_type.name].get(self._value)
        elif self.sensor_type in CCL_LEVEL_SENSORS:
            return 'Lv ' + self._value
        elif self.sensor_type == CCLSensorTypes.BATTERY_BINARY:
            try:
                return int(self._value) - 1
            except ValueError:
                pass
        
        try:
            return int(self._value)
        except ValueError:
            try:
                return float(self._value)
            except ValueError:
                return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

@dataclass
class CCLSensorPreset:
    name: str
    sensor_type: str
    compartment: None | CCLDeviceCompartment = None
    binary: bool = False
    
class CCLSensorTypes(enum.Enum):
    PRESSURE = 1
    TEMPERATURE = 2
    HUMIDITY = 3
    WIND_DIRECITON = 4
    WIND_SPEED = 5
    RAIN_RATE = 6
    RAINFALL = 7
    UVI = 8
    RADIATION = 9
    BATTERY_BINARY = 10
    CONNECTION = 11
    CH_SENSOR_TYPE = 12
    CO = 13
    CO2 = 14
    VOLATILE = 15
    VOC = 16
    PM10 = 17
    PM25 = 18
    AQI = 19
    LEAKAGE = 20
    BATTERY = 21
    DISTANCE = 22
    DURATION = 23
    FREQUENCY_NU = 24
    
class CCLDeviceCompartment(enum.Enum):
    MAIN = 'Console and Sensor Array'
    OTHER = 'Other Sensors'
    STATUS = 'Status'

CCL_SENSOR_VALUES: dict[str, dict[str, str]] = {
    'CH_SENSOR_TYPE': {
        '2': 'Thermo-Hygro',
        '3': 'Pool',
        '4': 'Soil',
    },
    'LEAKAGE': {
        '0': 'No Leak',
        '1': 'Leaking',
    }
}

CCL_LEVEL_SENSORS = (CCLSensorTypes.VOC, CCLSensorTypes.BATTERY)

CCL_SENSORS: dict[str, CCLSensorPreset] = {
    # Main Sensors 12-34
    'abar': CCLSensorPreset('Air Pressure (Absolute)', CCLSensorTypes.PRESSURE, CCLDeviceCompartment.MAIN),
    'rbar': CCLSensorPreset('Air Pressure (Relative)', CCLSensorTypes.PRESSURE, CCLDeviceCompartment.MAIN),
    't1dew': CCLSensorPreset('Index: Dew Point', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.MAIN),
    't1feels': CCLSensorPreset('Index: Feels Like', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.MAIN),
    't1heat': CCLSensorPreset('Index: Heat Index', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.MAIN),
    't1wbgt': CCLSensorPreset('Index: WBGT', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.MAIN),
    't1chill': CCLSensorPreset('Index: Wind Chill', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.MAIN),
    'inhum': CCLSensorPreset('Indoor Humidity', CCLSensorTypes.HUMIDITY, CCLDeviceCompartment.MAIN),
    'intem': CCLSensorPreset('Indoor Temperature', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.MAIN),
    't1solrad': CCLSensorPreset('Light Intensity', CCLSensorTypes.RADIATION, CCLDeviceCompartment.MAIN),
    't1hum': CCLSensorPreset('Outdoor Humidity', CCLSensorTypes.HUMIDITY, CCLDeviceCompartment.MAIN),
    't1tem': CCLSensorPreset('Outdoor Temperature', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.MAIN),
    't1rainra': CCLSensorPreset('Rain Rate', CCLSensorTypes.RAIN_RATE, CCLDeviceCompartment.MAIN),
    't1rainhr': CCLSensorPreset('Rainfall: Hourly ', CCLSensorTypes.RAINFALL, CCLDeviceCompartment.MAIN),
    't1raindy': CCLSensorPreset('Rainfall: Daily', CCLSensorTypes.RAINFALL, CCLDeviceCompartment.MAIN),
    't1rainwy': CCLSensorPreset('Rainfall: Weekly', CCLSensorTypes.RAINFALL, CCLDeviceCompartment.MAIN),
    't1rainmth': CCLSensorPreset('Rainfall: Monthly', CCLSensorTypes.RAINFALL, CCLDeviceCompartment.MAIN),
    't1rainyr': CCLSensorPreset('Rainfall: Yearly', CCLSensorTypes.RAINFALL, CCLDeviceCompartment.MAIN),
    't1uvi': CCLSensorPreset('UV Index', CCLSensorTypes.UVI, CCLDeviceCompartment.MAIN),
    't1wdir': CCLSensorPreset('Wind Direction', CCLSensorTypes.WIND_DIRECITON, CCLDeviceCompartment.MAIN),
    't1wgust': CCLSensorPreset('Wind Gust', CCLSensorTypes.WIND_SPEED, CCLDeviceCompartment.MAIN),
    't1ws': CCLSensorPreset('Wind Speed', CCLSensorTypes.WIND_SPEED, CCLDeviceCompartment.MAIN),
    't1ws10mav': CCLSensorPreset('Wind Speed (10 mins AVG.)', CCLSensorTypes.WIND_SPEED, CCLDeviceCompartment.MAIN),
    # Additional Sensors 35-77
    't11co': CCLSensorPreset('Air Quality: CO', CCLSensorTypes.CO, CCLDeviceCompartment.OTHER),
    't10co2': CCLSensorPreset('Air Quality: CO\u2082', CCLSensorTypes.CO2, CCLDeviceCompartment.OTHER),
    't9hcho': CCLSensorPreset('Air Quality: HCHO', CCLSensorTypes.VOLATILE, CCLDeviceCompartment.OTHER),
    't8pm10': CCLSensorPreset('Air Quality: PM10', CCLSensorTypes.PM10, CCLDeviceCompartment.OTHER),
    't8pm10ai': CCLSensorPreset('Air Quality: PM10 AQI', CCLSensorTypes.AQI, CCLDeviceCompartment.OTHER),
    't8pm25': CCLSensorPreset('Air Quality: PM2.5', CCLSensorTypes.PM25, CCLDeviceCompartment.OTHER),
    't8pm25ai': CCLSensorPreset('Air Quality: PM2.5 AQI', CCLSensorTypes.AQI, CCLDeviceCompartment.OTHER),
    't9voclv': CCLSensorPreset('Air Quality: VOC Level', CCLSensorTypes.VOC, CCLDeviceCompartment.OTHER),
    't234c1tem': CCLSensorPreset('CH1 Temperature', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.OTHER),
    't234c1hum': CCLSensorPreset('CH1 Humidity', CCLSensorTypes.HUMIDITY, CCLDeviceCompartment.OTHER),
    't234c1tp': CCLSensorPreset('CH1 Type', CCLSensorTypes.CH_SENSOR_TYPE, CCLDeviceCompartment.OTHER),
    't234c2tem': CCLSensorPreset('CH2 Temperature', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.OTHER),
    't234c2hum': CCLSensorPreset('CH2 Humidity', CCLSensorTypes.HUMIDITY, CCLDeviceCompartment.OTHER),
    't234c2tp': CCLSensorPreset('CH2 Type', CCLSensorTypes.CH_SENSOR_TYPE, CCLDeviceCompartment.OTHER),
    't234c3tem': CCLSensorPreset('CH3 Temperature', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.OTHER),
    't234c3hum': CCLSensorPreset('CH3 Humidity', CCLSensorTypes.HUMIDITY, CCLDeviceCompartment.OTHER),
    't234c3tp': CCLSensorPreset('CH3 Type', CCLSensorTypes.CH_SENSOR_TYPE, CCLDeviceCompartment.OTHER),
    't234c4tem': CCLSensorPreset('CH4 Temperature', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.OTHER),
    't234c4hum': CCLSensorPreset('CH4 Humidity', CCLSensorTypes.HUMIDITY, CCLDeviceCompartment.OTHER),
    't234c4tp': CCLSensorPreset('CH4 Type', CCLSensorTypes.CH_SENSOR_TYPE, CCLDeviceCompartment.OTHER),
    't234c5tem': CCLSensorPreset('CH5 Temperature', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.OTHER),
    't234c5hum': CCLSensorPreset('CH5 Humidity', CCLSensorTypes.HUMIDITY, CCLDeviceCompartment.OTHER),
    't234c5tp': CCLSensorPreset('CH5 Type', CCLSensorTypes.CH_SENSOR_TYPE, CCLDeviceCompartment.OTHER),
    't234c6tem': CCLSensorPreset('CH6 Temperature', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.OTHER),
    't234c6hum': CCLSensorPreset('CH6 Humidity', CCLSensorTypes.HUMIDITY, CCLDeviceCompartment.OTHER),
    't234c6tp': CCLSensorPreset('CH6 Type', CCLSensorTypes.CH_SENSOR_TYPE, CCLDeviceCompartment.OTHER),
    't234c7tem': CCLSensorPreset('CH7 Temperature', CCLSensorTypes.TEMPERATURE, CCLDeviceCompartment.OTHER),
    't234c7hum': CCLSensorPreset('CH7 Humidity', CCLSensorTypes.HUMIDITY, CCLDeviceCompartment.OTHER),
    't234c7tp': CCLSensorPreset('CH7 Type', CCLSensorTypes.CH_SENSOR_TYPE, CCLDeviceCompartment.OTHER),
    't6c1wls': CCLSensorPreset('Leakage CH1', CCLSensorTypes.LEAKAGE, CCLDeviceCompartment.OTHER),
    't6c2wls': CCLSensorPreset('Leakage CH2', CCLSensorTypes.LEAKAGE, CCLDeviceCompartment.OTHER),
    't6c3wls': CCLSensorPreset('Leakage CH3', CCLSensorTypes.LEAKAGE, CCLDeviceCompartment.OTHER),
    't6c4wls': CCLSensorPreset('Leakage CH4', CCLSensorTypes.LEAKAGE, CCLDeviceCompartment.OTHER),
    't6c5wls': CCLSensorPreset('Leakage CH5', CCLSensorTypes.LEAKAGE, CCLDeviceCompartment.OTHER),
    't6c6wls': CCLSensorPreset('Leakage CH6', CCLSensorTypes.LEAKAGE, CCLDeviceCompartment.OTHER),
    't6c7wls': CCLSensorPreset('Leakage CH7', CCLSensorTypes.LEAKAGE, CCLDeviceCompartment.OTHER),
    't5lskm': CCLSensorPreset('Lightning Distance', CCLSensorTypes.DISTANCE, CCLDeviceCompartment.OTHER),
    't5lst': CCLSensorPreset('Lightning: Last Strike', CCLSensorTypes.DURATION, CCLDeviceCompartment.OTHER),
    't5lsf': CCLSensorPreset('Lightning: Hourly Strikes', CCLSensorTypes.FREQUENCY_NU, CCLDeviceCompartment.OTHER),
    't5ls1dtc': CCLSensorPreset('Lightning: Daily Strikes', CCLSensorTypes.FREQUENCY_NU, CCLDeviceCompartment.OTHER),
    # Status 78-119
    't234c1bat': CCLSensorPreset('Battery: CH1', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't234c2bat': CCLSensorPreset('Battery: CH2', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't234c3bat': CCLSensorPreset('Battery: CH3', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't234c4bat': CCLSensorPreset('Battery: CH4', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't234c5bat': CCLSensorPreset('Battery: CH5', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't234c6bat': CCLSensorPreset('Battery: CH6', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't234c7bat': CCLSensorPreset('Battery: CH7', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't11bat': CCLSensorPreset('Battery: CO', CCLSensorTypes.BATTERY, CCLDeviceCompartment.STATUS),
    't10bat': CCLSensorPreset('Battery: CO\u2082', CCLSensorTypes.BATTERY, CCLDeviceCompartment.STATUS),
    'inbat': CCLSensorPreset('Battery: Console', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't9bat': CCLSensorPreset('Battery: HCHO/VOC', CCLSensorTypes.BATTERY, CCLDeviceCompartment.STATUS),
    't6c1bat': CCLSensorPreset('Battery: Leakage CH1', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't6c2bat': CCLSensorPreset('Battery: Leakage CH2', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't6c3bat': CCLSensorPreset('Battery: Leakage CH3', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't6c4bat': CCLSensorPreset('Battery: Leakage CH4', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't6c5bat': CCLSensorPreset('Battery: Leakage CH5', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't6c6bat': CCLSensorPreset('Battery: Leakage CH6', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't6c7bat': CCLSensorPreset('Battery: Leakage CH7', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't5lsbat': CCLSensorPreset('Battery: Lightning Sensor', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't1bat': CCLSensorPreset('Battery: Main Sensor Array', CCLSensorTypes.BATTERY_BINARY, CCLDeviceCompartment.STATUS, True),
    't8bat': CCLSensorPreset('Battery: PM2.5/10', CCLSensorTypes.BATTERY, CCLDeviceCompartment.STATUS),
    't234c1cn': CCLSensorPreset('Connection: CH1', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't234c2cn': CCLSensorPreset('Connection: CH2', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't234c3cn': CCLSensorPreset('Connection: CH3', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't234c4cn': CCLSensorPreset('Connection: CH4', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't234c5cn': CCLSensorPreset('Connection: CH5', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't234c6cn': CCLSensorPreset('Connection: CH6', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't234c7cn': CCLSensorPreset('Connection: CH7', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't6c1cn': CCLSensorPreset('Connection: Leakage CH1', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't6c2cn': CCLSensorPreset('Connection: Leakage CH2', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't6c3cn': CCLSensorPreset('Connection: Leakage CH3', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't6c4cn': CCLSensorPreset('Connection: Leakage CH4', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't6c5cn': CCLSensorPreset('Connection: Leakage CH5', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't6c6cn': CCLSensorPreset('Connection: Leakage CH6', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't6c7cn': CCLSensorPreset('Connection: Leakage CH7', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't5lscn': CCLSensorPreset('Connection: Lightning Sensor', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't11cn': CCLSensorPreset('Connection: CO', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't10cn': CCLSensorPreset('Connection: CO\u2082', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't9cn': CCLSensorPreset('Connection: HCHO/VOC', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't6c1cn': CCLSensorPreset('Connection: Leakage CH1', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't1cn': CCLSensorPreset('Connection: Main Sensor Array', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
    't8cn': CCLSensorPreset('Connection: PM2.5/10', CCLSensorTypes.CONNECTION, CCLDeviceCompartment.STATUS, True),
}
