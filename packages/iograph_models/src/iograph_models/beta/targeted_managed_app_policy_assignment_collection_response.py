from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TargetedManagedAppPolicyAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TargetedManagedAppPolicyAssignment]] = Field(alias="value", default=None,)

from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
