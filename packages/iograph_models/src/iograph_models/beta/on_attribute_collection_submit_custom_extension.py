from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnAttributeCollectionSubmitCustomExtension(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authenticationConfiguration: SerializeAsAny[Optional[CustomExtensionAuthenticationConfiguration]] = Field(alias="authenticationConfiguration",default=None,)
	clientConfiguration: Optional[CustomExtensionClientConfiguration] = Field(alias="clientConfiguration",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	endpointConfiguration: SerializeAsAny[Optional[CustomExtensionEndpointConfiguration]] = Field(alias="endpointConfiguration",default=None,)
	behaviorOnError: SerializeAsAny[Optional[CustomExtensionBehaviorOnError]] = Field(alias="behaviorOnError",default=None,)

from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
from .custom_extension_client_configuration import CustomExtensionClientConfiguration
from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration
from .custom_extension_behavior_on_error import CustomExtensionBehaviorOnError

