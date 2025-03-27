from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ApprovalSettings(BaseModel):
	approvalMode: Optional[str] = Field(alias="approvalMode", default=None,)
	approvalStages: Optional[list[UnifiedApprovalStage]] = Field(alias="approvalStages", default=None,)
	isApprovalRequired: Optional[bool] = Field(alias="isApprovalRequired", default=None,)
	isApprovalRequiredForExtension: Optional[bool] = Field(alias="isApprovalRequiredForExtension", default=None,)
	isRequestorJustificationRequired: Optional[bool] = Field(alias="isRequestorJustificationRequired", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .unified_approval_stage import UnifiedApprovalStage

