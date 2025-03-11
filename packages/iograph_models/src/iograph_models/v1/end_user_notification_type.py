from __future__ import annotations
from enum import StrEnum


class EndUserNotificationType(StrEnum):
	unknown = "unknown"
	positiveReinforcement = "positiveReinforcement"
	noTraining = "noTraining"
	trainingAssignment = "trainingAssignment"
	trainingReminder = "trainingReminder"
	unknownFutureValue = "unknownFutureValue"

