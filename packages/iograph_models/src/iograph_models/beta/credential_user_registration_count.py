from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CredentialUserRegistrationCount(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.credentialUserRegistrationCount"] = Field(alias="@odata.type", default="#microsoft.graph.credentialUserRegistrationCount")
	totalUserCount: Optional[int] = Field(alias="totalUserCount", default=None,)
	userRegistrationCounts: Optional[list[UserRegistrationCount]] = Field(alias="userRegistrationCounts", default=None,)

from .user_registration_count import UserRegistrationCount
