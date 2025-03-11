from __future__ import annotations
from enum import StrEnum


class SubjectRightsRequestStatus(StrEnum):
	active = "active"
	closed = "closed"
	unknownFutureValue = "unknownFutureValue"

