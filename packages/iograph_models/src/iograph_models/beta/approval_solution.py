from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ApprovalSolution(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	provisioningStatus: Optional[ProvisionState | str] = Field(alias="provisioningStatus",default=None,)
	approvalItems: Optional[list[ApprovalItem]] = Field(alias="approvalItems",default=None,)
	operations: Optional[list[ApprovalOperation]] = Field(alias="operations",default=None,)

from .provision_state import ProvisionState
from .approval_item import ApprovalItem
from .approval_operation import ApprovalOperation

