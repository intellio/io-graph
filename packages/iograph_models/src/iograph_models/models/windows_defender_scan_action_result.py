from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsDefenderScanActionResult(BaseModel):
	actionName: Optional[str] = Field(alias="actionName",default=None,)
	actionState: Optional[str | ActionState] = Field(alias="actionState",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	scanType: Optional[str] = Field(alias="scanType",default=None,)

from .action_state import ActionState

