from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TemporaryAccessPassAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets",default=None,)
	state: Optional[str | AuthenticationMethodState] = Field(alias="state",default=None,)
	defaultLength: Optional[int] = Field(alias="defaultLength",default=None,)
	defaultLifetimeInMinutes: Optional[int] = Field(alias="defaultLifetimeInMinutes",default=None,)
	isUsableOnce: Optional[bool] = Field(alias="isUsableOnce",default=None,)
	maximumLifetimeInMinutes: Optional[int] = Field(alias="maximumLifetimeInMinutes",default=None,)
	minimumLifetimeInMinutes: Optional[int] = Field(alias="minimumLifetimeInMinutes",default=None,)
	includeTargets: SerializeAsAny[Optional[list[AuthenticationMethodTarget]]] = Field(alias="includeTargets",default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .authentication_method_target import AuthenticationMethodTarget

