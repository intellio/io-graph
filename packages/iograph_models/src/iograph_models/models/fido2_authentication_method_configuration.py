from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Fido2AuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	excludeTargets: Optional[list[ExcludeTarget]] = Field(default=None,alias="excludeTargets",)
	state: Optional[AuthenticationMethodState] = Field(default=None,alias="state",)
	isAttestationEnforced: Optional[bool] = Field(default=None,alias="isAttestationEnforced",)
	isSelfServiceRegistrationAllowed: Optional[bool] = Field(default=None,alias="isSelfServiceRegistrationAllowed",)
	keyRestrictions: Optional[Fido2KeyRestrictions] = Field(default=None,alias="keyRestrictions",)
	includeTargets: Optional[list[AuthenticationMethodTarget]] = Field(default=None,alias="includeTargets",)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .fido2_key_restrictions import Fido2KeyRestrictions
from .authentication_method_target import AuthenticationMethodTarget

