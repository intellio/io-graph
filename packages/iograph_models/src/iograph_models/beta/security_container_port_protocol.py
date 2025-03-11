from __future__ import annotations
from enum import StrEnum


class SecurityContainerPortProtocol(StrEnum):
	udp = "udp"
	tcp = "tcp"
	sctp = "sctp"
	unknownFutureValue = "unknownFutureValue"

