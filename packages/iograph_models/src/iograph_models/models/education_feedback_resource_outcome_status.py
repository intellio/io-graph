from __future__ import annotations
from enum import Enum


class EducationFeedbackResourceOutcomeStatus(Enum):
	notPublished = "notPublished"
	pendingPublish = "pendingPublish"
	published = "published"
	failedPublish = "failedPublish"
	unknownFutureValue = "unknownFutureValue"

