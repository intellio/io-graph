from __future__ import annotations
from enum import StrEnum


class CloudPcProductType(StrEnum):
	enterprise = "enterprise"
	frontline = "frontline"
	devBox = "devBox"
	powerAutomate = "powerAutomate"
	business = "business"
	unknownFutureValue = "unknownFutureValue"

