from __future__ import annotations
from enum import StrEnum


class NetworkType(StrEnum):
	intranet = "intranet"
	extranet = "extranet"
	namedNetwork = "namedNetwork"
	trusted = "trusted"
	trustedNamedLocation = "trustedNamedLocation"
	unknownFutureValue = "unknownFutureValue"

