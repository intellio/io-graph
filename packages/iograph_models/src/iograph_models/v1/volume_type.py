from __future__ import annotations
from enum import StrEnum


class VolumeType(StrEnum):
	operatingSystemVolume = "operatingSystemVolume"
	fixedDataVolume = "fixedDataVolume"
	removableDataVolume = "removableDataVolume"
	unknownFutureValue = "unknownFutureValue"

