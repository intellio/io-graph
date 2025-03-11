from __future__ import annotations
from enum import StrEnum


class AndroidWorkProfileCrossProfileDataSharingType(StrEnum):
	deviceDefault = "deviceDefault"
	preventAny = "preventAny"
	allowPersonalToWork = "allowPersonalToWork"
	noRestrictions = "noRestrictions"

