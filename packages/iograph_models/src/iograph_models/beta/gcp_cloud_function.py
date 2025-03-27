from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class GcpCloudFunction(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.gcpCloudFunction"] = Field(alias="@odata.type", default="#microsoft.graph.gcpCloudFunction")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	source: Optional[Union[AadSource, AwsSource, AzureSource, GsuiteSource, UnknownSource]] = Field(alias="source", default=None,discriminator="odata_type", )
	authorizationSystem: Optional[Union[AwsAuthorizationSystem, AzureAuthorizationSystem, GcpAuthorizationSystem]] = Field(alias="authorizationSystem", default=None,discriminator="odata_type", )
	resource: Optional[GcpAuthorizationSystemResource] = Field(alias="resource", default=None,)

from .aad_source import AadSource
from .aws_source import AwsSource
from .azure_source import AzureSource
from .gsuite_source import GsuiteSource
from .unknown_source import UnknownSource
from .aws_authorization_system import AwsAuthorizationSystem
from .azure_authorization_system import AzureAuthorizationSystem
from .gcp_authorization_system import GcpAuthorizationSystem
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource

