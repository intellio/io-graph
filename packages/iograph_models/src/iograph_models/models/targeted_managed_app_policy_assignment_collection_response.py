from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TargetedManagedAppPolicyAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[TargetedManagedAppPolicyAssignment] = Field(alias="value",)

from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

