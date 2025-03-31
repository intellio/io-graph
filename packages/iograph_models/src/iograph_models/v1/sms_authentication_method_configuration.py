from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SmsAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.smsAuthenticationMethodConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.smsAuthenticationMethodConfiguration")
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state", default=None,)
	includeTargets: Optional[list[SmsAuthenticationMethodTarget]] = Field(alias="includeTargets", default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .sms_authentication_method_target import SmsAuthenticationMethodTarget
