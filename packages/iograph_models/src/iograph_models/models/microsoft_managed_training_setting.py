from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MicrosoftManagedTrainingSetting(BaseModel):
	settingType: Optional[TrainingSettingType] = Field(default=None,alias="settingType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completionDateTime: Optional[datetime] = Field(default=None,alias="completionDateTime",)
	trainingCompletionDuration: Optional[TrainingCompletionDuration] = Field(default=None,alias="trainingCompletionDuration",)

from .training_setting_type import TrainingSettingType
from .training_completion_duration import TrainingCompletionDuration

