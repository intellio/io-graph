from __future__ import annotations
from enum import StrEnum


class MacOSSoftwareUpdateCategory(StrEnum):
	critical = "critical"
	configurationDataFile = "configurationDataFile"
	firmware = "firmware"
	other = "other"

