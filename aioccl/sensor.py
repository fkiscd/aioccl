from __future__ import annotations

from dataclasses import dataclass
import enum
from typing import TypedDict

class CCLSensor:
    """Class that represents a CCLSensor object in the aioCCL API."""
    
    def __init__(self, key: str):
        """Initialize a CCL sensor."""
        self._value: None | str | int | float
    
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
    def binary(self) -> bool:
        return CCL_SENSORS[self._key].binary

    @property
    def value(self):
        if self.sensor_type == CCLSensorTypes.CH_SENSOR_TYPE:
            return CCL_CH_SENSOR_TYPES.get(self._value)
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

@dataclass
class CCLSensorPreset:
    name: str
    sensor_type: str
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
    
CCL_CH_SENSOR_TYPES: dict[int, str] = {
    2: 'Thermo-Hygro',
    3: 'Pool',
    4: 'Soil',
}
    
CCL_SENSORS: dict[str, CCLSensorPreset] = {
    'rbar': CCLSensorPreset('Relative Pressure', CCLSensorTypes.PRESSURE),
    'abar': CCLSensorPreset('Absolute Pressure', CCLSensorTypes.PRESSURE),
    'intem': CCLSensorPreset('Indoor Temperature', CCLSensorTypes.TEMPERATURE),
    'inhum': CCLSensorPreset('Indoor Humidity', CCLSensorTypes.HUMIDITY),
    'inbat': CCLSensorPreset('Console Battery', CCLSensorTypes.BATTERY_BINARY, True),
    't1tem': CCLSensorPreset('Outdoor Temperature', CCLSensorTypes.TEMPERATURE),
    't1hum': CCLSensorPreset('Outdoor Humidity', CCLSensorTypes.HUMIDITY),
    't1wdir': CCLSensorPreset('Wind Direction', CCLSensorTypes.WIND_DIRECITON),
    't1ws': CCLSensorPreset('Wind Speed', CCLSensorTypes.WIND_SPEED),
    't1ws10mav': CCLSensorPreset('Wind Speed (10 mins avg.)', CCLSensorTypes.WIND_SPEED),
    't1wgust': CCLSensorPreset('Wind Gust', CCLSensorTypes.WIND_SPEED),
    't1rainra': CCLSensorPreset('Rain Rate', CCLSensorTypes.RAIN_RATE),
    't1rainhr': CCLSensorPreset('Hourly Rainfall', CCLSensorTypes.RAINFALL),
    't1raindy': CCLSensorPreset('Daily Rainfall', CCLSensorTypes.RAINFALL),
    't1rainwy': CCLSensorPreset('Weekly Rainfall', CCLSensorTypes.RAINFALL),
    't1rainmth': CCLSensorPreset('Monthly Rainfall', CCLSensorTypes.RAINFALL),
    't1uvi': CCLSensorPreset('UV Index', CCLSensorTypes.UVI),
    't1solrad': CCLSensorPreset('Light Intensity', CCLSensorTypes.RADIATION),
    't1bat': CCLSensorPreset('CH0 Battery', CCLSensorTypes.BATTERY_BINARY, True),
    't1cn': CCLSensorPreset('CH0 Connection', CCLSensorTypes.CONNECTION),
    't1feels': CCLSensorPreset('Feels Like', CCLSensorTypes.TEMPERATURE),
    't1chill': CCLSensorPreset('Wind Chill', CCLSensorTypes.TEMPERATURE),
    't1heat': CCLSensorPreset('Heat Index', CCLSensorTypes.TEMPERATURE),
    't1dew': CCLSensorPreset('Dew Point', CCLSensorTypes.TEMPERATURE),
    't1wbgt': CCLSensorPreset('WBGT Index', CCLSensorTypes.TEMPERATURE),
    't234c1tem': CCLSensorPreset('CH1 Temperature', CCLSensorTypes.TEMPERATURE),
    't234c1hum': CCLSensorPreset('CH1 Humidity', CCLSensorTypes.HUMIDITY),
    't234c1bat': CCLSensorPreset('CH1 Battery', CCLSensorTypes.BATTERY_BINARY, True),
    't234c1cn': CCLSensorPreset('CH1 Connection', CCLSensorTypes.CONNECTION, True),
    't234c1tp': CCLSensorPreset('CH1 Sensor Type', CCLSensorTypes.CH_SENSOR_TYPE),
    't234c2tem': CCLSensorPreset('CH2 Temperature', CCLSensorTypes.TEMPERATURE),
    't234c2hum': CCLSensorPreset('CH2 Humidity', CCLSensorTypes.HUMIDITY),
    't234c2bat': CCLSensorPreset('CH2 Battery', CCLSensorTypes.BATTERY_BINARY, True),
    't234c2cn': CCLSensorPreset('CH2 Connection', CCLSensorTypes.CONNECTION, True),
    't234c2tp': CCLSensorPreset('CH2 Sensor Type', CCLSensorTypes.CH_SENSOR_TYPE),
}
