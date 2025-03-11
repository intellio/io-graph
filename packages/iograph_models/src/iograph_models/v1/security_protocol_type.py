from __future__ import annotations
from enum import StrEnum


class SecurityProtocolType(StrEnum):
	tcp = "tcp"
	udp = "udp"
	unknownFutureValue = "unknownFutureValue"

