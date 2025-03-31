from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MicrosoftCustomTrainingSetting(BaseModel):
	settingType: Optional[TrainingSettingType | str] = Field(alias="settingType", default=None,)
	odata_type: Literal["#microsoft.graph.microsoftCustomTrainingSetting"] = Field(alias="@odata.type", default="#microsoft.graph.microsoftCustomTrainingSetting")
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime", default=None,)
	trainingAssignmentMappings: Optional[list[MicrosoftTrainingAssignmentMapping]] = Field(alias="trainingAssignmentMappings", default=None,)
	trainingCompletionDuration: Optional[TrainingCompletionDuration | str] = Field(alias="trainingCompletionDuration", default=None,)

from .training_setting_type import TrainingSettingType
from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping
from .training_completion_duration import TrainingCompletionDuration
