from __future__ import annotations
from enum import StrEnum


class SamlSLOBindingType(StrEnum):
	httpRedirect = "httpRedirect"
	httpPost = "httpPost"
	unknownFutureValue = "unknownFutureValue"

