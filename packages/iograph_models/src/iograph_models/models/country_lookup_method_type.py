from __future__ import annotations
from enum import Enum


class CountryLookupMethodType(Enum):
	clientIpAddress = "clientIpAddress"
	authenticatorAppGps = "authenticatorAppGps"
	unknownFutureValue = "unknownFutureValue"

