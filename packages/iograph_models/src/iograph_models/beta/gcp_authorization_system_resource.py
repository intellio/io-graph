from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class GcpAuthorizationSystemResource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.gcpAuthorizationSystemResource"] = Field(alias="@odata.type", default="#microsoft.graph.gcpAuthorizationSystemResource")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	resourceType: Optional[str] = Field(alias="resourceType", default=None,)
	authorizationSystem: Optional[Union[AwsAuthorizationSystem, AzureAuthorizationSystem, GcpAuthorizationSystem]] = Field(alias="authorizationSystem", default=None,discriminator="odata_type", )
	service: Optional[AuthorizationSystemTypeService] = Field(alias="service", default=None,)

from .aws_authorization_system import AwsAuthorizationSystem
from .azure_authorization_system import AzureAuthorizationSystem
from .gcp_authorization_system import GcpAuthorizationSystem
from .authorization_system_type_service import AuthorizationSystemTypeService

