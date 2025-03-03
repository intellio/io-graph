from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOsLobAppAssignmentSettings(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	uninstallOnDeviceRemoval: Optional[bool] = Field(default=None,alias="uninstallOnDeviceRemoval",)


