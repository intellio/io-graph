from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Fido2AuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets",default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state",default=None,)
	isAttestationEnforced: Optional[bool] = Field(alias="isAttestationEnforced",default=None,)
	isSelfServiceRegistrationAllowed: Optional[bool] = Field(alias="isSelfServiceRegistrationAllowed",default=None,)
	keyRestrictions: Optional[Fido2KeyRestrictions] = Field(alias="keyRestrictions",default=None,)
	includeTargets: SerializeAsAny[Optional[list[AuthenticationMethodTarget]]] = Field(alias="includeTargets",default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .fido2_key_restrictions import Fido2KeyRestrictions
from .authentication_method_target import AuthenticationMethodTarget

