from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityApiConnector(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authenticationConfiguration: Optional[ApiAuthenticationConfigurationBase] = Field(default=None,alias="authenticationConfiguration",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	targetUrl: Optional[str] = Field(default=None,alias="targetUrl",)

from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase

