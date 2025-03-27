from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingAbstractImplementationConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingAbstractImplementationConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingAbstractImplementationConstraint")
	allowedAbstractImplementationDefinitionIds: Optional[list[str]] = Field(alias="allowedAbstractImplementationDefinitionIds", default=None,)


