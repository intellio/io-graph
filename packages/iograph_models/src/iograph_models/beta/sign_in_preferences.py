from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SignInPreferences(BaseModel):
	isSystemPreferredAuthenticationMethodEnabled: Optional[bool] = Field(alias="isSystemPreferredAuthenticationMethodEnabled", default=None,)
	userPreferredMethodForSecondaryAuthentication: Optional[UserDefaultAuthenticationMethodType | str] = Field(alias="userPreferredMethodForSecondaryAuthentication", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .user_default_authentication_method_type import UserDefaultAuthenticationMethodType
