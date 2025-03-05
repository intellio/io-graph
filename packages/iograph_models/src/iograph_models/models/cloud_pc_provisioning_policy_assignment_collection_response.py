from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcProvisioningPolicyAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CloudPcProvisioningPolicyAssignment]] = Field(default=None,alias="value",)

from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment

