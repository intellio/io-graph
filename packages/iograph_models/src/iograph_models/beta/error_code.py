from __future__ import annotations
from enum import StrEnum


class ErrorCode(StrEnum):
	noError = "noError"
	unauthorized = "unauthorized"
	notFound = "notFound"
	deleted = "deleted"

