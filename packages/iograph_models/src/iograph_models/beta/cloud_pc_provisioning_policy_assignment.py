from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcProvisioningPolicyAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	target: Optional[Union[CloudPcManagementGroupAssignmentTarget]] = Field(alias="target", default=None,discriminator="odata_type", )
	assignedUsers: Optional[list[User]] = Field(alias="assignedUsers", default=None,)

from .cloud_pc_management_group_assignment_target import CloudPcManagementGroupAssignmentTarget
from .user import User

