from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentWorkflowExtension(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authenticationConfiguration: SerializeAsAny[Optional[CustomExtensionAuthenticationConfiguration]] = Field(alias="authenticationConfiguration",default=None,)
	clientConfiguration: Optional[CustomExtensionClientConfiguration] = Field(alias="clientConfiguration",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	endpointConfiguration: SerializeAsAny[Optional[CustomExtensionEndpointConfiguration]] = Field(alias="endpointConfiguration",default=None,)
	callbackConfiguration: SerializeAsAny[Optional[CustomExtensionCallbackConfiguration]] = Field(alias="callbackConfiguration",default=None,)
	createdBy: Optional[str] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedBy: Optional[str] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)

from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
from .custom_extension_client_configuration import CustomExtensionClientConfiguration
from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration
from .custom_extension_callback_configuration import CustomExtensionCallbackConfiguration

