from __future__ import annotations
from enum import Enum


class SubjectRightsRequestStatus(Enum):
	active = "active"
	closed = "closed"
	unknownFutureValue = "unknownFutureValue"

