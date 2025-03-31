from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceHealthScriptBooleanParameter(BaseModel):
	applyDefaultValueWhenNotAssigned: Optional[bool] = Field(alias="applyDefaultValueWhenNotAssigned", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.deviceHealthScriptBooleanParameter"] = Field(alias="@odata.type", default="#microsoft.graph.deviceHealthScriptBooleanParameter")
	defaultValue: Optional[bool] = Field(alias="defaultValue", default=None,)

