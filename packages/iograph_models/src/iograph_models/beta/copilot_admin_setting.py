from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CopilotAdminSetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.copilotAdminSetting"] = Field(alias="@odata.type",)
	limitedMode: Optional[CopilotAdminLimitedMode] = Field(alias="limitedMode", default=None,)

from .copilot_admin_limited_mode import CopilotAdminLimitedMode
