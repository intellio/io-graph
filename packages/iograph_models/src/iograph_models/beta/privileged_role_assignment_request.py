from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PrivilegedRoleAssignmentRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.privilegedRoleAssignmentRequest"] = Field(alias="@odata.type", default="#microsoft.graph.privilegedRoleAssignmentRequest")
	assignmentState: Optional[str] = Field(alias="assignmentState", default=None,)
	duration: Optional[str] = Field(alias="duration", default=None,)
	reason: Optional[str] = Field(alias="reason", default=None,)
	requestedDateTime: Optional[datetime] = Field(alias="requestedDateTime", default=None,)
	roleId: Optional[str] = Field(alias="roleId", default=None,)
	schedule: Optional[GovernanceSchedule] = Field(alias="schedule", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	ticketNumber: Optional[str] = Field(alias="ticketNumber", default=None,)
	ticketSystem: Optional[str] = Field(alias="ticketSystem", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	roleInfo: Optional[PrivilegedRole] = Field(alias="roleInfo", default=None,)

from .governance_schedule import GovernanceSchedule
from .privileged_role import PrivilegedRole
