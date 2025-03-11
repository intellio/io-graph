from __future__ import annotations
from enum import StrEnum


class AndroidForWorkCrossProfileDataSharingType(StrEnum):
	deviceDefault = "deviceDefault"
	preventAny = "preventAny"
	allowPersonalToWork = "allowPersonalToWork"
	noRestrictions = "noRestrictions"

