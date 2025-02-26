from __future__ import annotations
from enum import Enum


class SubjectRightsRequestStage(Enum):
	contentRetrieval = "contentRetrieval"
	contentReview = "contentReview"
	generateReport = "generateReport"
	contentDeletion = "contentDeletion"
	caseResolved = "caseResolved"
	contentEstimate = "contentEstimate"
	unknownFutureValue = "unknownFutureValue"
	approval = "approval"

