import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN, CONF_API_KEY, CONF_STATION_ID, DEFAULT_NAME

class ShomInfoMareeConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for SHOM InfoMarée."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(
                title=user_input.get("name", DEFAULT_NAME),
                data=user_input,
            )

        data_schema = vol.Schema({
            vol.Required(CONF_API_KEY): str,
            vol.Required(CONF_STATION_ID): str,
            vol.Optional("name", default=DEFAULT_NAME): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return ShomInfoMareeOptionsFlowHandler(config_entry)


class ShomInfoMareeOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options for SHOM InfoMarée."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the SHOM InfoMarée options."""
        return self.async_show_form(step_id="init", data_schema=vol.Schema({}))
