from __future__ import annotations
from enum import StrEnum


class ExternalItemContentType(StrEnum):
	text = "text"
	html = "html"
	unknownFutureValue = "unknownFutureValue"

