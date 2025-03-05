from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PhoneAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber",default=None,)
	phoneType: Optional[str | AuthenticationPhoneType] = Field(alias="phoneType",default=None,)
	smsSignInState: Optional[str | AuthenticationMethodSignInState] = Field(alias="smsSignInState",default=None,)

from .authentication_phone_type import AuthenticationPhoneType
from .authentication_method_sign_in_state import AuthenticationMethodSignInState

