from __future__ import annotations
from enum import StrEnum


class WindowsInformationProtectionPinCharacterRequirements(StrEnum):
	notAllow = "notAllow"
	requireAtLeastOne = "requireAtLeastOne"
	allow = "allow"

