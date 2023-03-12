# Released under GPL 2

from typing import Optional

from autoSettingsUtils.autoSettings import SupportedSettingType
from cursorManager import CursorManager
from logHandler import log
from NVDAObjects import NVDAObject
from vision import providerBase
from vision.constants import Context
from vision.visionHandlerExtensionPoints import EventExtensionPoints

_ = lambda x: x  # FIXME


class Settings(providerBase.VisionEnhancementProviderSettings):
    @classmethod
    def getId(cls) -> str:
        return "focusHighlight"

    @classmethod
    def getDisplayName(cls) -> str:
        # Translators:
        return _("focusHighlight")

    def _get_supportedSettings(self) -> SupportedSettingType:
        return []


class Provider(providerBase.VisionEnhancementProvider):
    _settings = Settings()

    @classmethod  # override
    def getSettings(cls) -> Settings:
        return cls._settings

    @classmethod  # override
    def canStart(cls) -> bool:
        return True

    def registerEventExtensionPoints(  # override
        self, extensionPoints: EventExtensionPoints
    ) -> None:
        extensionPoints.post_objectUpdate.register(self.handleObjectUpdate)
        extensionPoints.post_focusChange.register(self.handleFocusChange)
        extensionPoints.post_foregroundChange.register(self.handleForegroundChange)
        extensionPoints.post_caretMove.register(self.handleCaretMove)
        extensionPoints.post_browseModeMove.register(self.handleBrowseModeMove)
        extensionPoints.post_reviewMove.register(self.handleReviewMove)
        extensionPoints.post_mouseMove.register(self.handleMouseMove)
        extensionPoints.post_coreCycle.register(self.handleCoreCycle)

    def __init__(self):
        super().__init__()
        log.debug("")

    def terminate(self):
        log.debug("")
        super().terminate()

    def handleObjectUpdate(self, obj: NVDAObject, property: str):
        log.debug(f"{obj} {property}")

    def handleFocusChange(self, obj: NVDAObject):
        log.debug(f"{obj}")

    def handleForegroundChange(self, obj: NVDAObject):
        log.debug(f"{obj}")

    def handleCaretMove(self, obj: NVDAObject):
        log.debug(f"{obj}")

    def handleBrowseModeMove(self, obj: Optional[CursorManager] = None):
        log.debug(f"{obj}")

    def handleReviewMove(self, context: Context):
        log.debug(f"{context}")

    def handleMouseMove(self, obj: NVDAObject):
        log.debug(f"{obj}")

    def handleCoreCycle(self):
        log.debug("")


VisionEnhancementProvider = Provider
