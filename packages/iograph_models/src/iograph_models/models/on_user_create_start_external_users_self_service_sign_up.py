from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnUserCreateStartExternalUsersSelfServiceSignUp(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	userTypeToCreate: Optional[UserType] = Field(default=None,alias="userTypeToCreate",)

from .user_type import UserType

