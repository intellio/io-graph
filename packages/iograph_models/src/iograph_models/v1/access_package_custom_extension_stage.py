from __future__ import annotations
from enum import StrEnum


class AccessPackageCustomExtensionStage(StrEnum):
	assignmentRequestCreated = "assignmentRequestCreated"
	assignmentRequestApproved = "assignmentRequestApproved"
	assignmentRequestGranted = "assignmentRequestGranted"
	assignmentRequestRemoved = "assignmentRequestRemoved"
	assignmentFourteenDaysBeforeExpiration = "assignmentFourteenDaysBeforeExpiration"
	assignmentOneDayBeforeExpiration = "assignmentOneDayBeforeExpiration"
	unknownFutureValue = "unknownFutureValue"

