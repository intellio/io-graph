from __future__ import annotations
from enum import StrEnum


class SecurityHostPortProtocol(StrEnum):
	tcp = "tcp"
	udp = "udp"
	unknownFutureValue = "unknownFutureValue"

