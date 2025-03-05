from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceCustomTaskExtension(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authenticationConfiguration: SerializeAsAny[Optional[CustomExtensionAuthenticationConfiguration]] = Field(default=None,alias="authenticationConfiguration",)
	clientConfiguration: Optional[CustomExtensionClientConfiguration] = Field(default=None,alias="clientConfiguration",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endpointConfiguration: SerializeAsAny[Optional[CustomExtensionEndpointConfiguration]] = Field(default=None,alias="endpointConfiguration",)
	callbackConfiguration: SerializeAsAny[Optional[CustomExtensionCallbackConfiguration]] = Field(default=None,alias="callbackConfiguration",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	createdBy: Optional[User] = Field(default=None,alias="createdBy",)
	lastModifiedBy: Optional[User] = Field(default=None,alias="lastModifiedBy",)

from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
from .custom_extension_client_configuration import CustomExtensionClientConfiguration
from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration
from .custom_extension_callback_configuration import CustomExtensionCallbackConfiguration
from .user import User
from .user import User

