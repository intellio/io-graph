from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Allowed_calendar_sharing_rolesGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CalendarRoleType]] = Field(default=None,alias="value",)

from .calendar_role_type import CalendarRoleType

