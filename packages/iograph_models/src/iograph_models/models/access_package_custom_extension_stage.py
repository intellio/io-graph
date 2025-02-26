from __future__ import annotations
from enum import Enum


class AccessPackageCustomExtensionStage(Enum):
	assignmentRequestCreated = "assignmentRequestCreated"
	assignmentRequestApproved = "assignmentRequestApproved"
	assignmentRequestGranted = "assignmentRequestGranted"
	assignmentRequestRemoved = "assignmentRequestRemoved"
	assignmentFourteenDaysBeforeExpiration = "assignmentFourteenDaysBeforeExpiration"
	assignmentOneDayBeforeExpiration = "assignmentOneDayBeforeExpiration"
	unknownFutureValue = "unknownFutureValue"

