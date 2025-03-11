from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsAutopilotSettings(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastManualSyncTriggerDateTime: Optional[datetime] = Field(alias="lastManualSyncTriggerDateTime",default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime",default=None,)
	syncStatus: Optional[WindowsAutopilotSyncStatus | str] = Field(alias="syncStatus",default=None,)

from .windows_autopilot_sync_status import WindowsAutopilotSyncStatus

