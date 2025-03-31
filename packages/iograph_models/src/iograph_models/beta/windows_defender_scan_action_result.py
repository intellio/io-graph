from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsDefenderScanActionResult(BaseModel):
	actionName: Optional[str] = Field(alias="actionName", default=None,)
	actionState: Optional[ActionState | str] = Field(alias="actionState", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	odata_type: Literal["#microsoft.graph.windowsDefenderScanActionResult"] = Field(alias="@odata.type",)
	scanType: Optional[str] = Field(alias="scanType", default=None,)

from .action_state import ActionState
