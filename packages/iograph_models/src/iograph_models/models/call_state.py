from __future__ import annotations
from enum import Enum


class CallState(Enum):
	incoming = "incoming"
	establishing = "establishing"
	established = "established"
	hold = "hold"
	transferring = "transferring"
	transferAccepted = "transferAccepted"
	redirecting = "redirecting"
	terminating = "terminating"
	terminated = "terminated"
	unknownFutureValue = "unknownFutureValue"

