from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets",default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	openIdConnectSetting: Optional[OpenIdConnectSetting] = Field(alias="openIdConnectSetting",default=None,)
	includeTargets: SerializeAsAny[Optional[list[AuthenticationMethodTarget]]] = Field(alias="includeTargets",default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .open_id_connect_setting import OpenIdConnectSetting
from .authentication_method_target import AuthenticationMethodTarget

