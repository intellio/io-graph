from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class OperationApprovalPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.operationApprovalPolicy"] = Field(alias="@odata.type",)
	approverGroupIds: Optional[list[str]] = Field(alias="approverGroupIds", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	policyPlatform: Optional[OperationApprovalPolicyPlatform | str] = Field(alias="policyPlatform", default=None,)
	policySet: Optional[OperationApprovalPolicySet] = Field(alias="policySet", default=None,)
	policyType: Optional[OperationApprovalPolicyType | str] = Field(alias="policyType", default=None,)

from .operation_approval_policy_platform import OperationApprovalPolicyPlatform
from .operation_approval_policy_set import OperationApprovalPolicySet
from .operation_approval_policy_type import OperationApprovalPolicyType
