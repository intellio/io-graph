from __future__ import annotations
from enum import StrEnum


class EducationFeedbackResourceOutcomeStatus(StrEnum):
	notPublished = "notPublished"
	pendingPublish = "pendingPublish"
	published = "published"
	failedPublish = "failedPublish"
	unknownFutureValue = "unknownFutureValue"

