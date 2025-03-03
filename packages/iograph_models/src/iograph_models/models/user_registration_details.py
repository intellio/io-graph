from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserRegistrationDetails(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isAdmin: Optional[bool] = Field(default=None,alias="isAdmin",)
	isMfaCapable: Optional[bool] = Field(default=None,alias="isMfaCapable",)
	isMfaRegistered: Optional[bool] = Field(default=None,alias="isMfaRegistered",)
	isPasswordlessCapable: Optional[bool] = Field(default=None,alias="isPasswordlessCapable",)
	isSsprCapable: Optional[bool] = Field(default=None,alias="isSsprCapable",)
	isSsprEnabled: Optional[bool] = Field(default=None,alias="isSsprEnabled",)
	isSsprRegistered: Optional[bool] = Field(default=None,alias="isSsprRegistered",)
	isSystemPreferredAuthenticationMethodEnabled: Optional[bool] = Field(default=None,alias="isSystemPreferredAuthenticationMethodEnabled",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	methodsRegistered: Optional[list[str]] = Field(default=None,alias="methodsRegistered",)
	systemPreferredAuthenticationMethods: Optional[list[str]] = Field(default=None,alias="systemPreferredAuthenticationMethods",)
	userDisplayName: Optional[str] = Field(default=None,alias="userDisplayName",)
	userPreferredMethodForSecondaryAuthentication: Optional[UserDefaultAuthenticationMethod] = Field(default=None,alias="userPreferredMethodForSecondaryAuthentication",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	userType: Optional[SignInUserType] = Field(default=None,alias="userType",)

from .user_default_authentication_method import UserDefaultAuthenticationMethod
from .sign_in_user_type import SignInUserType

