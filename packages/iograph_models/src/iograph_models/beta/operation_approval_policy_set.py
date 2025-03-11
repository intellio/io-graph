from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OperationApprovalPolicySet(BaseModel):
	policyPlatform: Optional[OperationApprovalPolicyPlatform | str] = Field(alias="policyPlatform",default=None,)
	policyType: Optional[OperationApprovalPolicyType | str] = Field(alias="policyType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .operation_approval_policy_platform import OperationApprovalPolicyPlatform
from .operation_approval_policy_type import OperationApprovalPolicyType

