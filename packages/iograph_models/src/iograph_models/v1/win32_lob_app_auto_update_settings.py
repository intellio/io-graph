from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppAutoUpdateSettings(BaseModel):
	autoUpdateSupersededAppsState: Optional[Win32LobAutoUpdateSupersededAppsState | str] = Field(alias="autoUpdateSupersededAppsState",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .win32_lob_auto_update_superseded_apps_state import Win32LobAutoUpdateSupersededAppsState

