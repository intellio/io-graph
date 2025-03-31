from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PasskeyAuthenticationMethodTarget(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.passkeyAuthenticationMethodTarget"] = Field(alias="@odata.type",)
	isRegistrationRequired: Optional[bool] = Field(alias="isRegistrationRequired", default=None,)
	targetType: Optional[AuthenticationMethodTargetType | str] = Field(alias="targetType", default=None,)

from .authentication_method_target_type import AuthenticationMethodTargetType
