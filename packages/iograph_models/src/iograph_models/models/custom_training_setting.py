from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomTrainingSetting(BaseModel):
	settingType: Optional[TrainingSettingType] = Field(default=None,alias="settingType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	assignedTo: Optional[TrainingAssignedTo] = Field(default=None,alias="assignedTo",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	durationInMinutes: Optional[int] = Field(default=None,alias="durationInMinutes",)
	url: Optional[str] = Field(default=None,alias="url",)

from .training_setting_type import TrainingSettingType
from .training_assigned_to import TrainingAssignedTo

