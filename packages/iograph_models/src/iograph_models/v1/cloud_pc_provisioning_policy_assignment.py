from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcProvisioningPolicyAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	target: SerializeAsAny[Optional[CloudPcManagementAssignmentTarget]] = Field(alias="target",default=None,)
	assignedUsers: Optional[list[User]] = Field(alias="assignedUsers",default=None,)

from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget
from .user import User

