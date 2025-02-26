from __future__ import annotations
from enum import Enum


class VolumeType(Enum):
	operatingSystemVolume = "operatingSystemVolume"
	fixedDataVolume = "fixedDataVolume"
	removableDataVolume = "removableDataVolume"
	unknownFutureValue = "unknownFutureValue"

