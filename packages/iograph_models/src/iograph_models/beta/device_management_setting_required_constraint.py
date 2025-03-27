from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingRequiredConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingRequiredConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingRequiredConstraint")
	notConfiguredValue: Optional[str] = Field(alias="notConfiguredValue", default=None,)


