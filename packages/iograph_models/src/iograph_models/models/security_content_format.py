from __future__ import annotations
from enum import Enum


class SecurityContentFormat(Enum):
	text = "text"
	html = "html"
	markdown = "markdown"
	unknownFutureValue = "unknownFutureValue"

