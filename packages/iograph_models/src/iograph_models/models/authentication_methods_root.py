from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodsRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	userRegistrationDetails: Optional[list[UserRegistrationDetails]] = Field(default=None,alias="userRegistrationDetails",)

from .user_registration_details import UserRegistrationDetails

