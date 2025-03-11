from __future__ import annotations
from enum import StrEnum


class SearchContent(StrEnum):
	sharedContent = "sharedContent"
	privateContent = "privateContent"
	unknownFutureValue = "unknownFutureValue"

