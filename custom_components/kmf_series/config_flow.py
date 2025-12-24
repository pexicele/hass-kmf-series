"""Config flow for KM-F Series integration."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from . import DOMAIN


class KMFSeriesConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for KM-F Series."""
    
    VERSION = 1
    
    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(
                title=user_input.get("name", "KM-F Series"),
                data=user_input,
            )
        
        data_schema = vol.Schema({
            vol.Required("name", default="KM-F Series"): str,
            vol.Required("host", default=""): str,
            vol.Optional("port", default=8899): int,
        })
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
        )
    
    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return KMFSeriesOptionsFlow(config_entry)


class KMFSeriesOptionsFlow(config_entries.OptionsFlow):
    """Handle options for KM-F Series."""
    
    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry
    
    async def async_step_init(self, user_input=None):
        """Handle the initial options step."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional(
                    "scan_interval",
                    default=self.config_entry.options.get("scan_interval", 30),
                ): int,
            }),
        )
