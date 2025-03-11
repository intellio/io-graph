from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftCustomTrainingSetting(BaseModel):
	settingType: Optional[TrainingSettingType | str] = Field(alias="settingType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime",default=None,)
	trainingAssignmentMappings: Optional[list[MicrosoftTrainingAssignmentMapping]] = Field(alias="trainingAssignmentMappings",default=None,)
	trainingCompletionDuration: Optional[TrainingCompletionDuration | str] = Field(alias="trainingCompletionDuration",default=None,)

from .training_setting_type import TrainingSettingType
from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping
from .training_completion_duration import TrainingCompletionDuration

