from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcProvisioningPolicyAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CloudPcProvisioningPolicyAssignment] = Field(alias="value",)

from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment

