from __future__ import annotations
from enum import Enum


class WindowsInformationProtectionPinCharacterRequirements(Enum):
	notAllow = "notAllow"
	requireAtLeastOne = "requireAtLeastOne"
	allow = "allow"

