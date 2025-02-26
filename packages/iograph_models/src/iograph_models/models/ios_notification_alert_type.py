from __future__ import annotations
from enum import Enum


class IosNotificationAlertType(Enum):
	deviceDefault = "deviceDefault"
	banner = "banner"
	modal = "modal"
	none = "none"

