"""Sensor platform for KM-F Series integration."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up sensor platform from a config entry."""
    config = hass.data[DOMAIN][entry.entry_id]
    
    sensors = [
        KMFSeriesSensor(entry, "Temperature", "°C"),
        KMFSeriesSensor(entry, "Humidity", "%"),
        KMFSeriesSensor(entry, "Power", "W"),
    ]
    
    async_add_entities(sensors)


class KMFSeriesSensor(SensorEntity):
    """KM-F Series sensor entity."""
    
    def __init__(self, entry: ConfigEntry, sensor_type: str, unit: str) -> None:
        """Initialize the sensor."""
        self._entry = entry
        self._sensor_type = sensor_type
        self._attr_native_unit_of_measurement = unit
        self._attr_name = f"KM-F Series {sensor_type}"
        self._attr_unique_id = f"{entry.entry_id}_{sensor_type.lower()}"
        self._state = None
    
    @property
    def state(self):
        """Return the state."""
        return self._state
