from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class VirtualMachineWithAwsStorageBucketAccessFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.virtualMachineWithAwsStorageBucketAccessFinding"] = Field(alias="@odata.type", default="#microsoft.graph.virtualMachineWithAwsStorageBucketAccessFinding")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	accessibleCount: Optional[int] = Field(alias="accessibleCount", default=None,)
	bucketCount: Optional[int] = Field(alias="bucketCount", default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex", default=None,)
	ec2Instance: Optional[Union[AwsAuthorizationSystemResource, AzureAuthorizationSystemResource, GcpAuthorizationSystemResource]] = Field(alias="ec2Instance", default=None,discriminator="odata_type", )
	role: Optional[AwsRole] = Field(alias="role", default=None,)

from .permissions_creep_index import PermissionsCreepIndex
from .aws_authorization_system_resource import AwsAuthorizationSystemResource
from .azure_authorization_system_resource import AzureAuthorizationSystemResource
from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
from .aws_role import AwsRole
