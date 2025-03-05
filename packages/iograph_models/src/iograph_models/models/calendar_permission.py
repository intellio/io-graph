from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CalendarPermission(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowedRoles: Optional[CalendarRoleType] = Field(default=None,alias="allowedRoles",)
	emailAddress: Optional[EmailAddress] = Field(default=None,alias="emailAddress",)
	isInsideOrganization: Optional[bool] = Field(default=None,alias="isInsideOrganization",)
	isRemovable: Optional[bool] = Field(default=None,alias="isRemovable",)
	role: Optional[CalendarRoleType] = Field(default=None,alias="role",)

from .calendar_role_type import CalendarRoleType
from .email_address import EmailAddress
from .calendar_role_type import CalendarRoleType

