from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftTrainingAssignmentMapping(BaseModel):
	settingType: Optional[TrainingSettingType] = Field(default=None,alias="settingType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	assignedTo: Optional[TrainingAssignedTo] = Field(default=None,alias="assignedTo",)
	training: Optional[Training] = Field(default=None,alias="training",)

from .training_setting_type import TrainingSettingType
from .training_assigned_to import TrainingAssignedTo
from .training import Training

