from __future__ import annotations
from enum import StrEnum


class NetworkaccessDhGroup(StrEnum):
	dhGroup14 = "dhGroup14"
	dhGroup24 = "dhGroup24"
	dhGroup2048 = "dhGroup2048"
	ecp256 = "ecp256"
	ecp384 = "ecp384"
	unknownFutureValue = "unknownFutureValue"

