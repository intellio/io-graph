from __future__ import annotations
from enum import StrEnum


class SensitiveTypeScope(StrEnum):
	fullDocument = "fullDocument"
	partialDocument = "partialDocument"

