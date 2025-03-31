from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Retrieve_operations_requiring_approvalGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OperationApprovalPolicySet]] = Field(alias="value", default=None,)

from .operation_approval_policy_set import OperationApprovalPolicySet
