from __future__ import annotations
from enum import StrEnum


class ServiceUpdateCategory(StrEnum):
	preventOrFixIssue = "preventOrFixIssue"
	planForChange = "planForChange"
	stayInformed = "stayInformed"
	unknownFutureValue = "unknownFutureValue"

