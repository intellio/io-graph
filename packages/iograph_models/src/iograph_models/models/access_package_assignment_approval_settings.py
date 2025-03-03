from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageAssignmentApprovalSettings(BaseModel):
	isApprovalRequiredForAdd: Optional[bool] = Field(default=None,alias="isApprovalRequiredForAdd",)
	isApprovalRequiredForUpdate: Optional[bool] = Field(default=None,alias="isApprovalRequiredForUpdate",)
	stages: Optional[list[AccessPackageApprovalStage]] = Field(default=None,alias="stages",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .access_package_approval_stage import AccessPackageApprovalStage

