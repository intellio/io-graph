from __future__ import annotations
from enum import StrEnum


class RoadmapItemDeliveryStage(StrEnum):
	privatePreview = "privatePreview"
	publicPreview = "publicPreview"
	ga = "ga"
	unknownFutureValue = "unknownFutureValue"

