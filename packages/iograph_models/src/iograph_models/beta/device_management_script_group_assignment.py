from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementScriptGroupAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementScriptGroupAssignment"] = Field(alias="@odata.type",)
	targetGroupId: Optional[str] = Field(alias="targetGroupId", default=None,)

