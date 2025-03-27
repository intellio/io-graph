from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ApprovalItemRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	approver: Optional[ApprovalIdentitySet] = Field(alias="approver", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isReassigned: Optional[bool] = Field(alias="isReassigned", default=None,)
	reassignedFrom: Optional[ApprovalIdentitySet] = Field(alias="reassignedFrom", default=None,)

from .approval_identity_set import ApprovalIdentitySet
from .approval_identity_set import ApprovalIdentitySet

