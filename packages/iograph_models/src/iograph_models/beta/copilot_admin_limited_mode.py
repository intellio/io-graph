from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CopilotAdminLimitedMode(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.copilotAdminLimitedMode"] = Field(alias="@odata.type",)
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	isEnabledForGroup: Optional[bool] = Field(alias="isEnabledForGroup", default=None,)

