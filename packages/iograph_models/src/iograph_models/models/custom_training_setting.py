from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomTrainingSetting(BaseModel):
	settingType: Optional[TrainingSettingType | str] = Field(alias="settingType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignedTo: Optional[TrainingAssignedTo | str] = Field(alias="assignedTo",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	durationInMinutes: Optional[int] = Field(alias="durationInMinutes",default=None,)
	url: Optional[str] = Field(alias="url",default=None,)

from .training_setting_type import TrainingSettingType
from .training_assigned_to import TrainingAssignedTo

