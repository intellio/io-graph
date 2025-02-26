from __future__ import annotations
from enum import Enum


class SecurityHostPortProtocol(Enum):
	tcp = "tcp"
	udp = "udp"
	unknownFutureValue = "unknownFutureValue"

