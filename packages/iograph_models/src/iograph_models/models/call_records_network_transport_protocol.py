from __future__ import annotations
from enum import StrEnum


class CallRecordsNetworkTransportProtocol(StrEnum):
	unknown = "unknown"
	udp = "udp"
	tcp = "tcp"
	unknownFutureValue = "unknownFutureValue"

