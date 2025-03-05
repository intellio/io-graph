from __future__ import annotations
from enum import StrEnum


class IosNotificationAlertType(StrEnum):
	deviceDefault = "deviceDefault"
	banner = "banner"
	modal = "modal"
	none = "none"

