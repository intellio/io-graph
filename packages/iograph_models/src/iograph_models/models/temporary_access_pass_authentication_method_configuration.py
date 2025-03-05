from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TemporaryAccessPassAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	excludeTargets: Optional[list[ExcludeTarget]] = Field(default=None,alias="excludeTargets",)
	state: Optional[AuthenticationMethodState] = Field(default=None,alias="state",)
	defaultLength: Optional[int] = Field(default=None,alias="defaultLength",)
	defaultLifetimeInMinutes: Optional[int] = Field(default=None,alias="defaultLifetimeInMinutes",)
	isUsableOnce: Optional[bool] = Field(default=None,alias="isUsableOnce",)
	maximumLifetimeInMinutes: Optional[int] = Field(default=None,alias="maximumLifetimeInMinutes",)
	minimumLifetimeInMinutes: Optional[int] = Field(default=None,alias="minimumLifetimeInMinutes",)
	includeTargets: SerializeAsAny[Optional[list[AuthenticationMethodTarget]]] = Field(default=None,alias="includeTargets",)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .authentication_method_target import AuthenticationMethodTarget

