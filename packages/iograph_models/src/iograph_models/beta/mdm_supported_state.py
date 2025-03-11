from __future__ import annotations
from enum import StrEnum


class MdmSupportedState(StrEnum):
	unknown = "unknown"
	supported = "supported"
	unsupported = "unsupported"
	deprecated = "deprecated"

