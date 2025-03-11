from __future__ import annotations
from enum import StrEnum


class EdiscoveryCaseAction(StrEnum):
	contentExport = "contentExport"
	applyTags = "applyTags"
	convertToPdf = "convertToPdf"
	index = "index"
	estimateStatistics = "estimateStatistics"
	addToReviewSet = "addToReviewSet"
	holdUpdate = "holdUpdate"
	unknownFutureValue = "unknownFutureValue"
	purgeData = "purgeData"

