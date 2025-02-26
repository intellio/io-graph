from __future__ import annotations
from enum import Enum


class ServiceUpdateCategory(Enum):
	preventOrFixIssue = "preventOrFixIssue"
	planForChange = "planForChange"
	stayInformed = "stayInformed"
	unknownFutureValue = "unknownFutureValue"

