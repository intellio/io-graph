from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnUserCreateStartExternalUsersSelfServiceSignUp(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	userTypeToCreate: Optional[UserType | str] = Field(alias="userTypeToCreate",default=None,)

from .user_type import UserType

