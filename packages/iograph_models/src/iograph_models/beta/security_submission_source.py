from __future__ import annotations
from enum import StrEnum


class SecuritySubmissionSource(StrEnum):
	user = "user"
	administrator = "administrator"
	unknownFutureValue = "unknownFutureValue"

