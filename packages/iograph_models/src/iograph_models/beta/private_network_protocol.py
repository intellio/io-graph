from __future__ import annotations
from enum import StrEnum


class PrivateNetworkProtocol(StrEnum):
	tcp = "tcp"
	udp = "udp"
	unknownFutureValue = "unknownFutureValue"

