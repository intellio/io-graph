from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CopilotAdmin(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.copilotAdmin"] = Field(alias="@odata.type",)
	settings: Optional[CopilotAdminSetting] = Field(alias="settings", default=None,)

from .copilot_admin_setting import CopilotAdminSetting
