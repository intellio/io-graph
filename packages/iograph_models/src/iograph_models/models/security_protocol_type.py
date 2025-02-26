from __future__ import annotations
from enum import Enum


class SecurityProtocolType(Enum):
	tcp = "tcp"
	udp = "udp"
	unknownFutureValue = "unknownFutureValue"

