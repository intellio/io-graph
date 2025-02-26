from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsUpdateActiveHoursInstall(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activeHoursEnd: Optional[str] = Field(default=None,alias="activeHoursEnd",)
	activeHoursStart: Optional[str] = Field(default=None,alias="activeHoursStart",)


