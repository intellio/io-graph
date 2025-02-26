from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EmailAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	excludeTargets: list[ExcludeTarget] = Field(alias="excludeTargets",)
	state: Optional[AuthenticationMethodState] = Field(default=None,alias="state",)
	allowExternalIdToUseEmailOtp: Optional[ExternalEmailOtpState] = Field(default=None,alias="allowExternalIdToUseEmailOtp",)
	includeTargets: list[AuthenticationMethodTarget] = Field(alias="includeTargets",)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .external_email_otp_state import ExternalEmailOtpState
from .authentication_method_target import AuthenticationMethodTarget

