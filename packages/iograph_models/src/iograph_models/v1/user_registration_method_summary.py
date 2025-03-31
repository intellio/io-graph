from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserRegistrationMethodSummary(BaseModel):
	totalUserCount: Optional[int] = Field(alias="totalUserCount", default=None,)
	userRegistrationMethodCounts: Optional[list[UserRegistrationMethodCount]] = Field(alias="userRegistrationMethodCounts", default=None,)
	userRoles: Optional[IncludedUserRoles | str] = Field(alias="userRoles", default=None,)
	userTypes: Optional[IncludedUserTypes | str] = Field(alias="userTypes", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .user_registration_method_count import UserRegistrationMethodCount
from .included_user_roles import IncludedUserRoles
from .included_user_types import IncludedUserTypes
