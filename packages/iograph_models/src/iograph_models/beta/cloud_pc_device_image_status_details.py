from __future__ import annotations
from enum import StrEnum


class CloudPcDeviceImageStatusDetails(StrEnum):
	internalServerError = "internalServerError"
	sourceImageNotFound = "sourceImageNotFound"
	osVersionNotSupported = "osVersionNotSupported"
	sourceImageInvalid = "sourceImageInvalid"
	sourceImageNotGeneralized = "sourceImageNotGeneralized"
	unknownFutureValue = "unknownFutureValue"
	vmAlreadyAzureAdjoined = "vmAlreadyAzureAdjoined"
	paidSourceImageNotSupport = "paidSourceImageNotSupport"
	sourceImageNotSupportCustomizeVMName = "sourceImageNotSupportCustomizeVMName"
	sourceImageSizeExceedsLimitation = "sourceImageSizeExceedsLimitation"

