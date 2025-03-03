from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcProvisioningPolicyAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	target: Optional[CloudPcManagementAssignmentTarget] = Field(default=None,alias="target",)
	assignedUsers: Optional[list[User]] = Field(default=None,alias="assignedUsers",)

from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget
from .user import User

