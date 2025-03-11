from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CalendarPermission(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowedRoles: Optional[CalendarRoleType | str] = Field(alias="allowedRoles",default=None,)
	emailAddress: SerializeAsAny[Optional[EmailAddress]] = Field(alias="emailAddress",default=None,)
	isInsideOrganization: Optional[bool] = Field(alias="isInsideOrganization",default=None,)
	isRemovable: Optional[bool] = Field(alias="isRemovable",default=None,)
	role: Optional[CalendarRoleType | str] = Field(alias="role",default=None,)

from .calendar_role_type import CalendarRoleType
from .email_address import EmailAddress
from .calendar_role_type import CalendarRoleType

