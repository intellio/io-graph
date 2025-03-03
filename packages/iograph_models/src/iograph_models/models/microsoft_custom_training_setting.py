from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MicrosoftCustomTrainingSetting(BaseModel):
	settingType: Optional[TrainingSettingType] = Field(default=None,alias="settingType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completionDateTime: Optional[datetime] = Field(default=None,alias="completionDateTime",)
	trainingAssignmentMappings: Optional[list[MicrosoftTrainingAssignmentMapping]] = Field(default=None,alias="trainingAssignmentMappings",)
	trainingCompletionDuration: Optional[TrainingCompletionDuration] = Field(default=None,alias="trainingCompletionDuration",)

from .training_setting_type import TrainingSettingType
from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping
from .training_completion_duration import TrainingCompletionDuration

