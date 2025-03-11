from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsParticipantEndpoint(BaseModel):
	userAgent: SerializeAsAny[Optional[CallRecordsUserAgent]] = Field(alias="userAgent",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	associatedIdentity: SerializeAsAny[Optional[Identity]] = Field(alias="associatedIdentity",default=None,)
	cpuCoresCount: Optional[int] = Field(alias="cpuCoresCount",default=None,)
	cpuName: Optional[str] = Field(alias="cpuName",default=None,)
	cpuProcessorSpeedInMhz: Optional[int] = Field(alias="cpuProcessorSpeedInMhz",default=None,)
	feedback: Optional[CallRecordsUserFeedback] = Field(alias="feedback",default=None,)
	identity: SerializeAsAny[Optional[IdentitySet]] = Field(alias="identity",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)

from .call_records_user_agent import CallRecordsUserAgent
from .identity import Identity
from .call_records_user_feedback import CallRecordsUserFeedback
from .identity_set import IdentitySet

