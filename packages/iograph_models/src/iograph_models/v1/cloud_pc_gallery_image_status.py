from __future__ import annotations
from enum import StrEnum


class CloudPcGalleryImageStatus(StrEnum):
	supported = "supported"
	supportedWithWarning = "supportedWithWarning"
	notSupported = "notSupported"
	unknownFutureValue = "unknownFutureValue"

