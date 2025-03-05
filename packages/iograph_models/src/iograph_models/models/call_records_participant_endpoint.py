from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsParticipantEndpoint(BaseModel):
	userAgent: SerializeAsAny[Optional[CallRecordsUserAgent]] = Field(default=None,alias="userAgent",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	associatedIdentity: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="associatedIdentity",)
	cpuCoresCount: Optional[int] = Field(default=None,alias="cpuCoresCount",)
	cpuName: Optional[str] = Field(default=None,alias="cpuName",)
	cpuProcessorSpeedInMhz: Optional[int] = Field(default=None,alias="cpuProcessorSpeedInMhz",)
	feedback: Optional[CallRecordsUserFeedback] = Field(default=None,alias="feedback",)
	identity: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="identity",)
	name: Optional[str] = Field(default=None,alias="name",)

from .call_records_user_agent import CallRecordsUserAgent
from .identity import Identity
from .call_records_user_feedback import CallRecordsUserFeedback
from .identity_set import IdentitySet

