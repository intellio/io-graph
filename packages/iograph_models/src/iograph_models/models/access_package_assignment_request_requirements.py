from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageAssignmentRequestRequirements(BaseModel):
	allowCustomAssignmentSchedule: Optional[bool] = Field(default=None,alias="allowCustomAssignmentSchedule",)
	isApprovalRequiredForAdd: Optional[bool] = Field(default=None,alias="isApprovalRequiredForAdd",)
	isApprovalRequiredForUpdate: Optional[bool] = Field(default=None,alias="isApprovalRequiredForUpdate",)
	policyDescription: Optional[str] = Field(default=None,alias="policyDescription",)
	policyDisplayName: Optional[str] = Field(default=None,alias="policyDisplayName",)
	policyId: Optional[str] = Field(default=None,alias="policyId",)
	schedule: Optional[EntitlementManagementSchedule] = Field(default=None,alias="schedule",)
	questions: Optional[list[AccessPackageQuestion]] = Field(default=None,alias="questions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .entitlement_management_schedule import EntitlementManagementSchedule
from .access_package_question import AccessPackageQuestion

