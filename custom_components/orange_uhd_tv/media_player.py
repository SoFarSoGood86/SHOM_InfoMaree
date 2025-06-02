from homeassistant.components.media_player import MediaPlayerEntity
from homeassistant.components.media_player.const import (
    SUPPORT_TURN_ON, SUPPORT_TURN_OFF, SUPPORT_VOLUME_STEP
)
from .const import DOMAIN, DEFAULT_NAME

class OrangeUHDTV(MediaPlayerEntity):
    _attr_supported_features = SUPPORT_TURN_ON | SUPPORT_TURN_OFF | SUPPORT_VOLUME_STEP
    _attr_name = DEFAULT_NAME

    def turn_on(self):
        # TODO: Implémenter l’allumage
        pass

    def turn_off(self):
        # TODO: Implémenter l’extinction
        pass

    def volume_up(self):
        # TODO: Implémenter volume +
        pass

    def volume_down(self):
        # TODO: Implémenter volume -
        pass
