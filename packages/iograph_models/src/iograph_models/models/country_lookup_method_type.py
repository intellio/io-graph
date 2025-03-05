from __future__ import annotations
from enum import StrEnum


class CountryLookupMethodType(StrEnum):
	clientIpAddress = "clientIpAddress"
	authenticatorAppGps = "authenticatorAppGps"
	unknownFutureValue = "unknownFutureValue"

