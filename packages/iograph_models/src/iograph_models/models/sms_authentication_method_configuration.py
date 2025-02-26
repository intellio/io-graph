from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SmsAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	excludeTargets: list[ExcludeTarget] = Field(alias="excludeTargets",)
	state: Optional[AuthenticationMethodState] = Field(default=None,alias="state",)
	includeTargets: list[SmsAuthenticationMethodTarget] = Field(alias="includeTargets",)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .sms_authentication_method_target import SmsAuthenticationMethodTarget

