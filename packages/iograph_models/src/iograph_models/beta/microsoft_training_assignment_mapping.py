from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftTrainingAssignmentMapping(BaseModel):
	settingType: Optional[TrainingSettingType | str] = Field(alias="settingType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignedTo: Optional[TrainingAssignedTo | str] = Field(alias="assignedTo",default=None,)
	training: Optional[Training] = Field(alias="training",default=None,)

from .training_setting_type import TrainingSettingType
from .training_assigned_to import TrainingAssignedTo
from .training import Training

