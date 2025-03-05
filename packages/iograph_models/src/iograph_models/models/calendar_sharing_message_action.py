from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CalendarSharingMessageAction(BaseModel):
	action: Optional[CalendarSharingAction] = Field(default=None,alias="action",)
	actionType: Optional[CalendarSharingActionType] = Field(default=None,alias="actionType",)
	importance: Optional[CalendarSharingActionImportance] = Field(default=None,alias="importance",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .calendar_sharing_action import CalendarSharingAction
from .calendar_sharing_action_type import CalendarSharingActionType
from .calendar_sharing_action_importance import CalendarSharingActionImportance

