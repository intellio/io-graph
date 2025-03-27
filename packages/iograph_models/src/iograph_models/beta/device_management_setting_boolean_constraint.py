from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingBooleanConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingBooleanConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingBooleanConstraint")
	value: Optional[bool] = Field(alias="value", default=None,)


