from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserRegistrationMethodSummary(BaseModel):
	totalUserCount: Optional[int] = Field(default=None,alias="totalUserCount",)
	userRegistrationMethodCounts: Optional[list[UserRegistrationMethodCount]] = Field(default=None,alias="userRegistrationMethodCounts",)
	userRoles: Optional[IncludedUserRoles] = Field(default=None,alias="userRoles",)
	userTypes: Optional[IncludedUserTypes] = Field(default=None,alias="userTypes",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .user_registration_method_count import UserRegistrationMethodCount
from .included_user_roles import IncludedUserRoles
from .included_user_types import IncludedUserTypes

