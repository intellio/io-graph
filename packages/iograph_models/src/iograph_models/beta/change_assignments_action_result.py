from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChangeAssignmentsActionResult(BaseModel):
	actionName: Optional[str] = Field(alias="actionName",default=None,)
	actionState: Optional[ActionState | str] = Field(alias="actionState",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceAssignmentItems: Optional[list[DeviceAssignmentItem]] = Field(alias="deviceAssignmentItems",default=None,)

from .action_state import ActionState
from .device_assignment_item import DeviceAssignmentItem

