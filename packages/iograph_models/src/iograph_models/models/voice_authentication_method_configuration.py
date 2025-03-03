from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VoiceAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	excludeTargets: Optional[list[ExcludeTarget]] = Field(default=None,alias="excludeTargets",)
	state: Optional[AuthenticationMethodState] = Field(default=None,alias="state",)
	isOfficePhoneAllowed: Optional[bool] = Field(default=None,alias="isOfficePhoneAllowed",)
	includeTargets: Optional[list[AuthenticationMethodTarget]] = Field(default=None,alias="includeTargets",)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .authentication_method_target import AuthenticationMethodTarget

