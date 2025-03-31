from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageAssignmentApprovalSettings(BaseModel):
	isApprovalRequiredForAdd: Optional[bool] = Field(alias="isApprovalRequiredForAdd", default=None,)
	isApprovalRequiredForUpdate: Optional[bool] = Field(alias="isApprovalRequiredForUpdate", default=None,)
	stages: Optional[list[AccessPackageApprovalStage]] = Field(alias="stages", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_package_approval_stage import AccessPackageApprovalStage
