from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftManagedTrainingSetting(BaseModel):
	settingType: Optional[TrainingSettingType | str] = Field(alias="settingType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime",default=None,)
	trainingCompletionDuration: Optional[TrainingCompletionDuration | str] = Field(alias="trainingCompletionDuration",default=None,)

from .training_setting_type import TrainingSettingType
from .training_completion_duration import TrainingCompletionDuration

