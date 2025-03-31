from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppDashboardCardIcon(BaseModel):
	iconUrl: Optional[str] = Field(alias="iconUrl", default=None,)
	officeUIFabricIconName: Optional[str] = Field(alias="officeUIFabricIconName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

