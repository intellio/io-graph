from __future__ import annotations
from enum import StrEnum


class PrintJobStateDetail(StrEnum):
	uploadPending = "uploadPending"
	transforming = "transforming"
	completedSuccessfully = "completedSuccessfully"
	completedWithWarnings = "completedWithWarnings"
	completedWithErrors = "completedWithErrors"
	releaseWait = "releaseWait"
	interpreting = "interpreting"
	unknownFutureValue = "unknownFutureValue"

