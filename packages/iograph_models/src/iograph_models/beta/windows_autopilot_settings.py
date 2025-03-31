from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsAutopilotSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsAutopilotSettings"] = Field(alias="@odata.type",)
	lastManualSyncTriggerDateTime: Optional[datetime] = Field(alias="lastManualSyncTriggerDateTime", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	syncStatus: Optional[WindowsAutopilotSyncStatus | str] = Field(alias="syncStatus", default=None,)

from .windows_autopilot_sync_status import WindowsAutopilotSyncStatus
