from __future__ import annotations
from enum import StrEnum


class VpnTrafficDirection(StrEnum):
	outbound = "outbound"
	inbound = "inbound"
	unknownFutureValue = "unknownFutureValue"

