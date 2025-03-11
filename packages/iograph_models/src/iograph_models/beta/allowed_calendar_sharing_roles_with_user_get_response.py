from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Allowed_calendar_sharing_roles_with_userGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[CalendarRoleType | str]] = Field(alias="value",default=None,)

from .calendar_role_type import CalendarRoleType

