from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodsRegistrationCampaignIncludeTarget(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	targetedAuthenticationMethod: Optional[str] = Field(default=None,alias="targetedAuthenticationMethod",)
	targetType: Optional[AuthenticationMethodTargetType] = Field(default=None,alias="targetType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_method_target_type import AuthenticationMethodTargetType

