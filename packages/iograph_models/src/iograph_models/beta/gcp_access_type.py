from __future__ import annotations
from enum import StrEnum


class GcpAccessType(StrEnum):
	public = "public"
	subjectToObjectAcls = "subjectToObjectAcls"
	private = "private"
	unknownFutureValue = "unknownFutureValue"

