from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AuthenticationFlowsPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.authenticationFlowsPolicy"] = Field(alias="@odata.type",)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	selfServiceSignUp: Optional[SelfServiceSignUpAuthenticationFlowConfiguration] = Field(alias="selfServiceSignUp", default=None,)

from .self_service_sign_up_authentication_flow_configuration import SelfServiceSignUpAuthenticationFlowConfiguration
