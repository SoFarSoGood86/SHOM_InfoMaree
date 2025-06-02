import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, DEFAULT_NAME

@config_entries.HANDLERS.register(DOMAIN)
class OrangeUHDTVConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Valider et créer la config
            return self.async_create_entry(title=DEFAULT_NAME, data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("host"): str,
                vol.Required("token", default=""): str,
            }),
            errors=errors,
        )
