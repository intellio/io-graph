from __future__ import annotations
from enum import Enum


class EndUserNotificationType(Enum):
	unknown = "unknown"
	positiveReinforcement = "positiveReinforcement"
	noTraining = "noTraining"
	trainingAssignment = "trainingAssignment"
	trainingReminder = "trainingReminder"
	unknownFutureValue = "unknownFutureValue"

