from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnTokenIssuanceStartCustomExtension(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authenticationConfiguration: Optional[CustomExtensionAuthenticationConfiguration] = Field(default=None,alias="authenticationConfiguration",)
	clientConfiguration: Optional[CustomExtensionClientConfiguration] = Field(default=None,alias="clientConfiguration",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endpointConfiguration: Optional[CustomExtensionEndpointConfiguration] = Field(default=None,alias="endpointConfiguration",)
	claimsForTokenConfiguration: list[OnTokenIssuanceStartReturnClaim] = Field(alias="claimsForTokenConfiguration",)

from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
from .custom_extension_client_configuration import CustomExtensionClientConfiguration
from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration
from .on_token_issuance_start_return_claim import OnTokenIssuanceStartReturnClaim

