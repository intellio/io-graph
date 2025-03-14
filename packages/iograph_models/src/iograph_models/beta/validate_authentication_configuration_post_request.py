from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Validate_authentication_configurationPostRequest(BaseModel):
	endpointConfiguration: SerializeAsAny[Optional[CustomExtensionEndpointConfiguration]] = Field(alias="endpointConfiguration",default=None,)
	authenticationConfiguration: SerializeAsAny[Optional[CustomExtensionAuthenticationConfiguration]] = Field(alias="authenticationConfiguration",default=None,)

from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration
from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration

