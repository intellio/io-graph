from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class VoiceAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.voiceAuthenticationMethodConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.voiceAuthenticationMethodConfiguration")
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state", default=None,)
	isOfficePhoneAllowed: Optional[bool] = Field(alias="isOfficePhoneAllowed", default=None,)
	includeTargets: Optional[list[VoiceAuthenticationMethodTarget]] = Field(alias="includeTargets", default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .voice_authentication_method_target import VoiceAuthenticationMethodTarget
