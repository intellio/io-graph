from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class PhoneAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.phoneAuthenticationMethod"] = Field(alias="@odata.type", default="#microsoft.graph.phoneAuthenticationMethod")
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)
	phoneType: Optional[AuthenticationPhoneType | str] = Field(alias="phoneType", default=None,)
	smsSignInState: Optional[AuthenticationMethodSignInState | str] = Field(alias="smsSignInState", default=None,)

from .authentication_phone_type import AuthenticationPhoneType
from .authentication_method_sign_in_state import AuthenticationMethodSignInState

