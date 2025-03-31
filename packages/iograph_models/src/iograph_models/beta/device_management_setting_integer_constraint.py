from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementSettingIntegerConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingIntegerConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingIntegerConstraint")
	maximumValue: Optional[int] = Field(alias="maximumValue", default=None,)
	minimumValue: Optional[int] = Field(alias="minimumValue", default=None,)

