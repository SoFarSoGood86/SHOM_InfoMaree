from datetime import timedelta
import logging
import requests

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import HomeAssistantType, ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator

from .const import DOMAIN, CONF_API_KEY, CONF_STATION_ID, DEFAULT_NAME

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(hours=1)

def setup_platform(hass: HomeAssistantType, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info=None):
    api_key = config.get(CONF_API_KEY)
    station_id = config.get(CONF_STATION_ID)
    name = config.get(CONF_NAME, DEFAULT_NAME)

    if not api_key or not station_id:
        _LOGGER.error("Clé API ou ID de station manquante.")
        return

    add_entities([ShomMareeSensor(api_key, station_id, name)], True)

class ShomMareeSensor(SensorEntity):
    def __init__(self, api_key, station_id, name):
        self._api_key = api_key
        self._station_id = station_id
        self._name = name
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    def update(self):
        try:
            response = requests.get(
                f"https://data.shom.fr/api/maree/horaires",
                params={
                    "apikey": self._api_key,
                    "station": self._station_id,
                },
                timeout=10,
            )
            data = response.json()

            prochaine = data["marees"][0]  # Exemple
            self._state = prochaine["type"]  # "PM" ou "BM"
            self._attributes = {
                "heure": prochaine["heure"],
                "hauteur": prochaine["hauteur"],
                "station": self._station_id,
            }

        except Exception as e:
            _LOGGER.error(f"Erreur lors de la récupération des données SHOM : {e}")
