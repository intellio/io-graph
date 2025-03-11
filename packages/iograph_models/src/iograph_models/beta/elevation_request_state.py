from __future__ import annotations
from enum import StrEnum


class ElevationRequestState(StrEnum):
	none = "none"
	pending = "pending"
	approved = "approved"
	denied = "denied"
	expired = "expired"
	unknownFutureValue = "unknownFutureValue"
	revoked = "revoked"
	completed = "completed"

