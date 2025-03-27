from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CopilotAdminSetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	limitedMode: Optional[CopilotAdminLimitedMode] = Field(alias="limitedMode", default=None,)

from .copilot_admin_limited_mode import CopilotAdminLimitedMode

