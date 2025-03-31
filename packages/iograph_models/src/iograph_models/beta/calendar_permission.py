from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class CalendarPermission(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.calendarPermission"] = Field(alias="@odata.type",)
	allowedRoles: Optional[list[CalendarRoleType | str]] = Field(alias="allowedRoles", default=None,)
	emailAddress: Optional[Union[TypedEmailAddress]] = Field(alias="emailAddress", default=None,discriminator="odata_type", )
	isInsideOrganization: Optional[bool] = Field(alias="isInsideOrganization", default=None,)
	isRemovable: Optional[bool] = Field(alias="isRemovable", default=None,)
	role: Optional[CalendarRoleType | str] = Field(alias="role", default=None,)

from .calendar_role_type import CalendarRoleType
from .typed_email_address import TypedEmailAddress
