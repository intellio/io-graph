from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class AssignedComputeInstanceDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.assignedComputeInstanceDetails"] = Field(alias="@odata.type", default="#microsoft.graph.assignedComputeInstanceDetails")
	accessedStorageBuckets: Optional[list[Annotated[Union[AwsAuthorizationSystemResource, AzureAuthorizationSystemResource, GcpAuthorizationSystemResource],Field(discriminator="odata_type")]]] = Field(alias="accessedStorageBuckets", default=None,)
	assignedComputeInstance: Optional[Union[AwsAuthorizationSystemResource, AzureAuthorizationSystemResource, GcpAuthorizationSystemResource]] = Field(alias="assignedComputeInstance", default=None,discriminator="odata_type", )

from .aws_authorization_system_resource import AwsAuthorizationSystemResource
from .azure_authorization_system_resource import AzureAuthorizationSystemResource
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
