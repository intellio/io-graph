from __future__ import annotations
from enum import Enum


class PrintJobStateDetail(Enum):
	uploadPending = "uploadPending"
	transforming = "transforming"
	completedSuccessfully = "completedSuccessfully"
	completedWithWarnings = "completedWithWarnings"
	completedWithErrors = "completedWithErrors"
	releaseWait = "releaseWait"
	interpreting = "interpreting"
	unknownFutureValue = "unknownFutureValue"

