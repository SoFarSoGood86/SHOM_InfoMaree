from homeassistant.core import HomeAssistant
from homeassistant.helpers.discovery import async_load_platform
from .const import DOMAIN, PLATFORM

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up SHOM InfoMarée."""
    if DOMAIN not in config:
        return True

    hass.async_create_task(
        async_load_platform(hass, PLATFORM, DOMAIN, config[DOMAIN], config)
    )

    return True
