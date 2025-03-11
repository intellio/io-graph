from __future__ import annotations
from enum import StrEnum


class TrainingSettingType(StrEnum):
	microsoftCustom = "microsoftCustom"
	microsoftManaged = "microsoftManaged"
	noTraining = "noTraining"
	custom = "custom"
	unknownFutureValue = "unknownFutureValue"

