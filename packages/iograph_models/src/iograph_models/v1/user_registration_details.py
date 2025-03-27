from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserRegistrationDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	isAdmin: Optional[bool] = Field(alias="isAdmin", default=None,)
	isMfaCapable: Optional[bool] = Field(alias="isMfaCapable", default=None,)
	isMfaRegistered: Optional[bool] = Field(alias="isMfaRegistered", default=None,)
	isPasswordlessCapable: Optional[bool] = Field(alias="isPasswordlessCapable", default=None,)
	isSsprCapable: Optional[bool] = Field(alias="isSsprCapable", default=None,)
	isSsprEnabled: Optional[bool] = Field(alias="isSsprEnabled", default=None,)
	isSsprRegistered: Optional[bool] = Field(alias="isSsprRegistered", default=None,)
	isSystemPreferredAuthenticationMethodEnabled: Optional[bool] = Field(alias="isSystemPreferredAuthenticationMethodEnabled", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	methodsRegistered: Optional[list[str]] = Field(alias="methodsRegistered", default=None,)
	systemPreferredAuthenticationMethods: Optional[list[str]] = Field(alias="systemPreferredAuthenticationMethods", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userPreferredMethodForSecondaryAuthentication: Optional[UserDefaultAuthenticationMethod | str] = Field(alias="userPreferredMethodForSecondaryAuthentication", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	userType: Optional[SignInUserType | str] = Field(alias="userType", default=None,)

from .user_default_authentication_method import UserDefaultAuthenticationMethod
from .sign_in_user_type import SignInUserType

