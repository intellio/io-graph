from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualMachineWithAwsStorageBucketAccessFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	accessibleCount: Optional[int] = Field(alias="accessibleCount",default=None,)
	bucketCount: Optional[int] = Field(alias="bucketCount",default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex",default=None,)
	ec2Instance: SerializeAsAny[Optional[AuthorizationSystemResource]] = Field(alias="ec2Instance",default=None,)
	role: Optional[AwsRole] = Field(alias="role",default=None,)

from .permissions_creep_index import PermissionsCreepIndex
from .authorization_system_resource import AuthorizationSystemResource
from .aws_role import AwsRole

