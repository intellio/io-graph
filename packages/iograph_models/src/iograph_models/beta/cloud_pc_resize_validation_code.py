from __future__ import annotations
from enum import StrEnum


class CloudPcResizeValidationCode(StrEnum):
	success = "success"
	cloudPcNotFound = "cloudPcNotFound"
	operationConflict = "operationConflict"
	operationNotSupported = "operationNotSupported"
	targetLicenseHasAssigned = "targetLicenseHasAssigned"
	internalServerError = "internalServerError"
	unknownFutureValue = "unknownFutureValue"

