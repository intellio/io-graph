from __future__ import annotations
from enum import Enum


class TrainingSettingType(Enum):
	microsoftCustom = "microsoftCustom"
	microsoftManaged = "microsoftManaged"
	noTraining = "noTraining"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

