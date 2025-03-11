from __future__ import annotations
from enum import StrEnum


class SubjectRightsRequestStage(StrEnum):
	contentRetrieval = "contentRetrieval"
	contentReview = "contentReview"
	generateReport = "generateReport"
	contentDeletion = "contentDeletion"
	caseResolved = "caseResolved"
	contentEstimate = "contentEstimate"
	unknownFutureValue = "unknownFutureValue"
	approval = "approval"

