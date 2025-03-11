from __future__ import annotations
from enum import StrEnum


class SecurityContentFormat(StrEnum):
	text = "text"
	html = "html"
	markdown = "markdown"
	unknownFutureValue = "unknownFutureValue"

