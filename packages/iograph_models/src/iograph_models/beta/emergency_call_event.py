from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EmergencyCallEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.emergencyCallEvent"] = Field(alias="@odata.type",)
	callEventType: Optional[CallEventType | str] = Field(alias="callEventType", default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	participants: Optional[list[Participant]] = Field(alias="participants", default=None,)
	callerInfo: Optional[EmergencyCallerInfo] = Field(alias="callerInfo", default=None,)
	emergencyNumberDialed: Optional[str] = Field(alias="emergencyNumberDialed", default=None,)
	policyName: Optional[str] = Field(alias="policyName", default=None,)

from .call_event_type import CallEventType
from .participant import Participant
from .emergency_caller_info import EmergencyCallerInfo
