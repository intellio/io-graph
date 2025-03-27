from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CalendarSharingMessageAction(BaseModel):
	action: Optional[CalendarSharingAction | str] = Field(alias="action", default=None,)
	actionType: Optional[CalendarSharingActionType | str] = Field(alias="actionType", default=None,)
	importance: Optional[CalendarSharingActionImportance | str] = Field(alias="importance", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .calendar_sharing_action import CalendarSharingAction
from .calendar_sharing_action_type import CalendarSharingActionType
from .calendar_sharing_action_importance import CalendarSharingActionImportance

