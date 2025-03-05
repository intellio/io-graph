from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NoTrainingSetting(BaseModel):
	settingType: Optional[str | TrainingSettingType] = Field(alias="settingType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .training_setting_type import TrainingSettingType

