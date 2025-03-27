from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OnTokenIssuanceStartCustomExtension(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onTokenIssuanceStartCustomExtension"] = Field(alias="@odata.type", default="#microsoft.graph.onTokenIssuanceStartCustomExtension")
	authenticationConfiguration: Optional[Union[AzureAdPopTokenAuthentication, AzureAdTokenAuthentication]] = Field(alias="authenticationConfiguration", default=None,discriminator="odata_type", )
	clientConfiguration: Optional[CustomExtensionClientConfiguration] = Field(alias="clientConfiguration", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endpointConfiguration: Optional[Union[HttpRequestEndpoint, LogicAppTriggerEndpointConfiguration]] = Field(alias="endpointConfiguration", default=None,discriminator="odata_type", )
	claimsForTokenConfiguration: Optional[list[OnTokenIssuanceStartReturnClaim]] = Field(alias="claimsForTokenConfiguration", default=None,)

from .azure_ad_pop_token_authentication import AzureAdPopTokenAuthentication
from .azure_ad_token_authentication import AzureAdTokenAuthentication
from .custom_extension_client_configuration import CustomExtensionClientConfiguration
from .http_request_endpoint import HttpRequestEndpoint
from .logic_app_trigger_endpoint_configuration import LogicAppTriggerEndpointConfiguration
from .on_token_issuance_start_return_claim import OnTokenIssuanceStartReturnClaim

