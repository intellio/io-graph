from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodsRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	userRegistrationDetails: Optional[list[UserRegistrationDetails]] = Field(alias="userRegistrationDetails",default=None,)

from .user_registration_details import UserRegistrationDetails

