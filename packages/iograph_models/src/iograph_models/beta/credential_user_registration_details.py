from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CredentialUserRegistrationDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.credentialUserRegistrationDetails"] = Field(alias="@odata.type", default="#microsoft.graph.credentialUserRegistrationDetails")
	authMethods: Optional[list[RegistrationAuthMethod | str]] = Field(alias="authMethods", default=None,)
	isCapable: Optional[bool] = Field(alias="isCapable", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	isMfaRegistered: Optional[bool] = Field(alias="isMfaRegistered", default=None,)
	isRegistered: Optional[bool] = Field(alias="isRegistered", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .registration_auth_method import RegistrationAuthMethod
