from __future__ import annotations
from enum import StrEnum


class ApplicationKeyType(StrEnum):
	clientSecret = "clientSecret"
	certificate = "certificate"
	unknownFutureValue = "unknownFutureValue"

