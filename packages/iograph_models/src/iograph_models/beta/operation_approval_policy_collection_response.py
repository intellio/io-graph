from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OperationApprovalPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OperationApprovalPolicy]] = Field(alias="value", default=None,)

from .operation_approval_policy import OperationApprovalPolicy
