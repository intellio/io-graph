from __future__ import annotations
from enum import Enum


class CallRecordsCallType(Enum):
	unknown = "unknown"
	groupCall = "groupCall"
	peerToPeer = "peerToPeer"
	unknownFutureValue = "unknownFutureValue"

