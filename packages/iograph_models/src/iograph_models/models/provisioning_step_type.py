from __future__ import annotations
from enum import Enum


class ProvisioningStepType(Enum):
	import_ = "import_"
	scoping = "scoping"
	matching = "matching"
	processing = "processing"
	referenceResolution = "referenceResolution"
	export = "export"
	unknownFutureValue = "unknownFutureValue"

