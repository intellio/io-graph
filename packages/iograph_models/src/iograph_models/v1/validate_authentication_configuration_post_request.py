from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class Validate_authentication_configurationPostRequest(BaseModel):
	endpointConfiguration: Optional[Union[HttpRequestEndpoint, LogicAppTriggerEndpointConfiguration]] = Field(alias="endpointConfiguration", default=None,discriminator="odata_type", )
	authenticationConfiguration: Optional[Union[AzureAdPopTokenAuthentication, AzureAdTokenAuthentication]] = Field(alias="authenticationConfiguration", default=None,discriminator="odata_type", )

from .http_request_endpoint import HttpRequestEndpoint
from .logic_app_trigger_endpoint_configuration import LogicAppTriggerEndpointConfiguration
from .azure_ad_pop_token_authentication import AzureAdPopTokenAuthentication
from .azure_ad_token_authentication import AzureAdTokenAuthentication
