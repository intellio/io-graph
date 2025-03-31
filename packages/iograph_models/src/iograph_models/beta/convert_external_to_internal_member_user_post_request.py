from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Convert_external_to_internal_member_userPostRequest(BaseModel):
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	mail: Optional[str] = Field(alias="mail", default=None,)
	passwordProfile: Optional[PasswordProfile] = Field(alias="passwordProfile", default=None,)

from .password_profile import PasswordProfile
