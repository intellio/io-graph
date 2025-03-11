from __future__ import annotations
from enum import StrEnum


class CallRecordsCallType(StrEnum):
	unknown = "unknown"
	groupCall = "groupCall"
	peerToPeer = "peerToPeer"
	unknownFutureValue = "unknownFutureValue"

