from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ApprovalItemRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.approvalItemRequest"] = Field(alias="@odata.type", default="#microsoft.graph.approvalItemRequest")
	approver: Optional[ApprovalIdentitySet] = Field(alias="approver", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isReassigned: Optional[bool] = Field(alias="isReassigned", default=None,)
	reassignedFrom: Optional[ApprovalIdentitySet] = Field(alias="reassignedFrom", default=None,)

from .approval_identity_set import ApprovalIdentitySet
