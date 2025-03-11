from __future__ import annotations
from enum import StrEnum


class ZebraFotaNetworkType(StrEnum):
	any = "any"
	wifi = "wifi"
	cellular = "cellular"
	wifiAndCellular = "wifiAndCellular"
	unknownFutureValue = "unknownFutureValue"

