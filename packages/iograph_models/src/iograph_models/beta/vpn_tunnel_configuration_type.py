from __future__ import annotations
from enum import StrEnum


class VpnTunnelConfigurationType(StrEnum):
	wifiAndCellular = "wifiAndCellular"
	cellular = "cellular"
	wifi = "wifi"

