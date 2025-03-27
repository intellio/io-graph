from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentWorkflowExtension(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageAssignmentWorkflowExtension"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageAssignmentWorkflowExtension")
	authenticationConfiguration: Optional[Union[AzureAdPopTokenAuthentication, AzureAdTokenAuthentication]] = Field(alias="authenticationConfiguration", default=None,discriminator="odata_type", )
	clientConfiguration: Optional[CustomExtensionClientConfiguration] = Field(alias="clientConfiguration", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endpointConfiguration: Optional[Union[HttpRequestEndpoint, LogicAppTriggerEndpointConfiguration]] = Field(alias="endpointConfiguration", default=None,discriminator="odata_type", )
	callbackConfiguration: Optional[Union[IdentityGovernanceCustomTaskExtensionCallbackConfiguration]] = Field(alias="callbackConfiguration", default=None,discriminator="odata_type", )
	createdBy: Optional[str] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedBy: Optional[str] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)

from .azure_ad_pop_token_authentication import AzureAdPopTokenAuthentication
from .azure_ad_token_authentication import AzureAdTokenAuthentication
from .custom_extension_client_configuration import CustomExtensionClientConfiguration
from .http_request_endpoint import HttpRequestEndpoint
from .logic_app_trigger_endpoint_configuration import LogicAppTriggerEndpointConfiguration
from .identity_governance_custom_task_extension_callback_configuration import IdentityGovernanceCustomTaskExtensionCallbackConfiguration

