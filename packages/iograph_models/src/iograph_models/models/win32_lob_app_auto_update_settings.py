from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Win32LobAppAutoUpdateSettings(BaseModel):
	autoUpdateSupersededAppsState: Optional[Win32LobAutoUpdateSupersededAppsState] = Field(default=None,alias="autoUpdateSupersededAppsState",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .win32_lob_auto_update_superseded_apps_state import Win32LobAutoUpdateSupersededAppsState

