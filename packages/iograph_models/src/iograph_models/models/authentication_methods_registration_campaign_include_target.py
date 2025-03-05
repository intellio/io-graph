from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodsRegistrationCampaignIncludeTarget(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	targetedAuthenticationMethod: Optional[str] = Field(alias="targetedAuthenticationMethod",default=None,)
	targetType: Optional[str | AuthenticationMethodTargetType] = Field(alias="targetType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authentication_method_target_type import AuthenticationMethodTargetType

