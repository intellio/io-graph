from __future__ import annotations
from enum import StrEnum


class SecurityFileProcessingStatus(StrEnum):
	success = "success"
	internalError = "internalError"
	unknownError = "unknownError"
	processingTimeout = "processingTimeout"
	invalidFileId = "invalidFileId"
	fileSizeIsZero = "fileSizeIsZero"
	fileSizeIsTooLarge = "fileSizeIsTooLarge"
	fileDepthLimitExceeded = "fileDepthLimitExceeded"
	fileBodyIsTooLong = "fileBodyIsTooLong"
	fileTypeIsUnknown = "fileTypeIsUnknown"
	fileTypeIsNotSupported = "fileTypeIsNotSupported"
	malformedFile = "malformedFile"
	protectedFile = "protectedFile"
	poisonFile = "poisonFile"
	noReviewSetSummaryGenerated = "noReviewSetSummaryGenerated"
	extractionException = "extractionException"
	ocrProcessingTimeout = "ocrProcessingTimeout"
	ocrFileSizeExceedsLimit = "ocrFileSizeExceedsLimit"
	unknownFutureValue = "unknownFutureValue"

