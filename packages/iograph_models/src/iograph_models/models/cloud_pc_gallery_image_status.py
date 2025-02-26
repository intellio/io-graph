from __future__ import annotations
from enum import Enum


class CloudPcGalleryImageStatus(Enum):
	supported = "supported"
	supportedWithWarning = "supportedWithWarning"
	notSupported = "notSupported"
	unknownFutureValue = "unknownFutureValue"

