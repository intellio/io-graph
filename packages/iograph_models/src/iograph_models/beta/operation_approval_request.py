from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OperationApprovalRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	approvalJustification: Optional[str] = Field(alias="approvalJustification",default=None,)
	approver: SerializeAsAny[Optional[IdentitySet]] = Field(alias="approver",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	requestDateTime: Optional[datetime] = Field(alias="requestDateTime",default=None,)
	requestJustification: Optional[str] = Field(alias="requestJustification",default=None,)
	requestor: SerializeAsAny[Optional[IdentitySet]] = Field(alias="requestor",default=None,)
	requiredOperationApprovalPolicyTypes: Optional[list[OperationApprovalPolicyType | str]] = Field(alias="requiredOperationApprovalPolicyTypes",default=None,)
	status: Optional[OperationApprovalRequestStatus | str] = Field(alias="status",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .operation_approval_policy_type import OperationApprovalPolicyType
from .operation_approval_request_status import OperationApprovalRequestStatus

