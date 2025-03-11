from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OpenShiftChangeRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	assignedTo: Optional[ScheduleChangeRequestActor | str] = Field(alias="assignedTo",default=None,)
	managerActionDateTime: Optional[datetime] = Field(alias="managerActionDateTime",default=None,)
	managerActionMessage: Optional[str] = Field(alias="managerActionMessage",default=None,)
	managerUserId: Optional[str] = Field(alias="managerUserId",default=None,)
	senderDateTime: Optional[datetime] = Field(alias="senderDateTime",default=None,)
	senderMessage: Optional[str] = Field(alias="senderMessage",default=None,)
	senderUserId: Optional[str] = Field(alias="senderUserId",default=None,)
	state: Optional[ScheduleChangeState | str] = Field(alias="state",default=None,)
	openShiftId: Optional[str] = Field(alias="openShiftId",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .schedule_change_request_actor import ScheduleChangeRequestActor
from .schedule_change_state import ScheduleChangeState

