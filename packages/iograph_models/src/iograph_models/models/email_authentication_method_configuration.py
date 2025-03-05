from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EmailAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets",default=None,)
	state: Optional[str | AuthenticationMethodState] = Field(alias="state",default=None,)
	allowExternalIdToUseEmailOtp: Optional[str | ExternalEmailOtpState] = Field(alias="allowExternalIdToUseEmailOtp",default=None,)
	includeTargets: SerializeAsAny[Optional[list[AuthenticationMethodTarget]]] = Field(alias="includeTargets",default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .external_email_otp_state import ExternalEmailOtpState
from .authentication_method_target import AuthenticationMethodTarget

