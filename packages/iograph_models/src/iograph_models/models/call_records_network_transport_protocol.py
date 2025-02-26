from __future__ import annotations
from enum import Enum


class CallRecordsNetworkTransportProtocol(Enum):
	unknown = "unknown"
	udp = "udp"
	tcp = "tcp"
	unknownFutureValue = "unknownFutureValue"

