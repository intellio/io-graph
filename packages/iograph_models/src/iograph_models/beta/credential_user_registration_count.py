from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CredentialUserRegistrationCount(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	totalUserCount: Optional[int] = Field(alias="totalUserCount",default=None,)
	userRegistrationCounts: Optional[list[UserRegistrationCount]] = Field(alias="userRegistrationCounts",default=None,)

from .user_registration_count import UserRegistrationCount

