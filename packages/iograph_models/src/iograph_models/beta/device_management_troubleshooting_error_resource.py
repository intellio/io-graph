from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementTroubleshootingErrorResource(BaseModel):
	link: Optional[str] = Field(alias="link", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

