from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Validate_authentication_configurationPostRequest(BaseModel):
	endpointConfiguration: Optional[CustomExtensionEndpointConfiguration] = Field(default=None,alias="endpointConfiguration",)
	authenticationConfiguration: Optional[CustomExtensionAuthenticationConfiguration] = Field(default=None,alias="authenticationConfiguration",)

from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration
from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration

