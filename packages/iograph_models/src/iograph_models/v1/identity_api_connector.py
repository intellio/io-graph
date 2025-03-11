from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityApiConnector(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authenticationConfiguration: SerializeAsAny[Optional[ApiAuthenticationConfigurationBase]] = Field(alias="authenticationConfiguration",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	targetUrl: Optional[str] = Field(alias="targetUrl",default=None,)

from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase

