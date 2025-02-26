from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ApprovalSettings(BaseModel):
	approvalMode: Optional[str] = Field(default=None,alias="approvalMode",)
	approvalStages: list[UnifiedApprovalStage] = Field(alias="approvalStages",)
	isApprovalRequired: Optional[bool] = Field(default=None,alias="isApprovalRequired",)
	isApprovalRequiredForExtension: Optional[bool] = Field(default=None,alias="isApprovalRequiredForExtension",)
	isRequestorJustificationRequired: Optional[bool] = Field(default=None,alias="isRequestorJustificationRequired",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .unified_approval_stage import UnifiedApprovalStage

