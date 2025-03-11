from __future__ import annotations
from enum import StrEnum


class CallRecordsWifiRadioType(StrEnum):
	unknown = "unknown"
	wifi80211a = "wifi80211a"
	wifi80211b = "wifi80211b"
	wifi80211g = "wifi80211g"
	wifi80211n = "wifi80211n"
	wifi80211ac = "wifi80211ac"
	wifi80211ax = "wifi80211ax"
	unknownFutureValue = "unknownFutureValue"

