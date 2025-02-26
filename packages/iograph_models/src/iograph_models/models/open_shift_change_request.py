from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class OpenShiftChangeRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	assignedTo: Optional[ScheduleChangeRequestActor] = Field(default=None,alias="assignedTo",)
	managerActionDateTime: Optional[datetime] = Field(default=None,alias="managerActionDateTime",)
	managerActionMessage: Optional[str] = Field(default=None,alias="managerActionMessage",)
	managerUserId: Optional[str] = Field(default=None,alias="managerUserId",)
	senderDateTime: Optional[datetime] = Field(default=None,alias="senderDateTime",)
	senderMessage: Optional[str] = Field(default=None,alias="senderMessage",)
	senderUserId: Optional[str] = Field(default=None,alias="senderUserId",)
	state: Optional[ScheduleChangeState] = Field(default=None,alias="state",)
	openShiftId: Optional[str] = Field(default=None,alias="openShiftId",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .schedule_change_request_actor import ScheduleChangeRequestActor
from .schedule_change_state import ScheduleChangeState

