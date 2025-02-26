from __future__ import annotations
from enum import Enum


class AndroidWorkProfileCrossProfileDataSharingType(Enum):
	deviceDefault = "deviceDefault"
	preventAny = "preventAny"
	allowPersonalToWork = "allowPersonalToWork"
	noRestrictions = "noRestrictions"

