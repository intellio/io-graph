from __future__ import annotations
from enum import StrEnum


class PrintEvent(StrEnum):
	jobStarted = "jobStarted"
	unknownFutureValue = "unknownFutureValue"

