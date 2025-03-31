from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ApprovePostRequest(BaseModel):
	justification: Optional[str] = Field(alias="justification", default=None,)
	approvalSource: Optional[OperationApprovalSource | str] = Field(alias="approvalSource", default=None,)

from .operation_approval_source import OperationApprovalSource
