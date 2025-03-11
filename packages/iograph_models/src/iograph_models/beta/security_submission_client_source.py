from __future__ import annotations
from enum import StrEnum


class SecuritySubmissionClientSource(StrEnum):
	microsoft = "microsoft"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

