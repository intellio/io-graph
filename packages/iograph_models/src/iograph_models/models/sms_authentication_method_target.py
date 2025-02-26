from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SmsAuthenticationMethodTarget(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isRegistrationRequired: Optional[bool] = Field(default=None,alias="isRegistrationRequired",)
	targetType: Optional[AuthenticationMethodTargetType] = Field(default=None,alias="targetType",)
	isUsableForSignIn: Optional[bool] = Field(default=None,alias="isUsableForSignIn",)

from .authentication_method_target_type import AuthenticationMethodTargetType

