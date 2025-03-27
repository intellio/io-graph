from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingCollectionConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingCollectionConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingCollectionConstraint")
	maximumLength: Optional[int] = Field(alias="maximumLength", default=None,)
	minimumLength: Optional[int] = Field(alias="minimumLength", default=None,)


