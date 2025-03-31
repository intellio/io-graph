from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NoTrainingSetting(BaseModel):
	settingType: Optional[TrainingSettingType | str] = Field(alias="settingType", default=None,)
	odata_type: Literal["#microsoft.graph.noTrainingSetting"] = Field(alias="@odata.type", default="#microsoft.graph.noTrainingSetting")

from .training_setting_type import TrainingSettingType
