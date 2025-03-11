from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedApproval(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	approvalDuration: Optional[str] = Field(alias="approvalDuration",default=None,)
	approvalState: Optional[ApprovalState | str] = Field(alias="approvalState",default=None,)
	approvalType: Optional[str] = Field(alias="approvalType",default=None,)
	approverReason: Optional[str] = Field(alias="approverReason",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	requestorReason: Optional[str] = Field(alias="requestorReason",default=None,)
	roleId: Optional[str] = Field(alias="roleId",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	request: Optional[PrivilegedRoleAssignmentRequest] = Field(alias="request",default=None,)
	roleInfo: Optional[PrivilegedRole] = Field(alias="roleInfo",default=None,)

from .approval_state import ApprovalState
from .privileged_role_assignment_request import PrivilegedRoleAssignmentRequest
from .privileged_role import PrivilegedRole

