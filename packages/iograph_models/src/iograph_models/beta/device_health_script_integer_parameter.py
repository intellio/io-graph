from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceHealthScriptIntegerParameter(BaseModel):
	applyDefaultValueWhenNotAssigned: Optional[bool] = Field(alias="applyDefaultValueWhenNotAssigned", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.deviceHealthScriptIntegerParameter"] = Field(alias="@odata.type", default="#microsoft.graph.deviceHealthScriptIntegerParameter")
	defaultValue: Optional[int] = Field(alias="defaultValue", default=None,)

