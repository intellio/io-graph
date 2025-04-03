from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SmsAuthenticationMethodTarget(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.smsAuthenticationMethodTarget"] = Field(alias="@odata.type", default="#microsoft.graph.smsAuthenticationMethodTarget")
	isRegistrationRequired: Optional[bool] = Field(alias="isRegistrationRequired", default=None,)
	targetType: Optional[AuthenticationMethodTargetType | str] = Field(alias="targetType", default=None,)
	isUsableForSignIn: Optional[bool] = Field(alias="isUsableForSignIn", default=None,)

from .authentication_method_target_type import AuthenticationMethodTargetType
