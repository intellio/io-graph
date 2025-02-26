from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PhoneAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	phoneNumber: Optional[str] = Field(default=None,alias="phoneNumber",)
	phoneType: Optional[AuthenticationPhoneType] = Field(default=None,alias="phoneType",)
	smsSignInState: Optional[AuthenticationMethodSignInState] = Field(default=None,alias="smsSignInState",)

from .authentication_phone_type import AuthenticationPhoneType
from .authentication_method_sign_in_state import AuthenticationMethodSignInState

