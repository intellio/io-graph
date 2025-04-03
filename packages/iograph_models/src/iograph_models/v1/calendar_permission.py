from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CalendarPermission(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.calendarPermission"] = Field(alias="@odata.type", default="#microsoft.graph.calendarPermission")
	allowedRoles: Optional[list[CalendarRoleType | str]] = Field(alias="allowedRoles", default=None,)
	emailAddress: Optional[EmailAddress] = Field(alias="emailAddress", default=None,)
	isInsideOrganization: Optional[bool] = Field(alias="isInsideOrganization", default=None,)
	isRemovable: Optional[bool] = Field(alias="isRemovable", default=None,)
	role: Optional[CalendarRoleType | str] = Field(alias="role", default=None,)

from .calendar_role_type import CalendarRoleType
from .email_address import EmailAddress
