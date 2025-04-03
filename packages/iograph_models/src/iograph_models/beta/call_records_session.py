from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CallRecordsSession(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.callRecords.session"] = Field(alias="@odata.type", default="#microsoft.graph.callRecords.session")
	callee: Optional[Union[CallRecordsParticipantEndpoint, CallRecordsServiceEndpoint]] = Field(alias="callee", default=None,discriminator="odata_type", )
	caller: Optional[Union[CallRecordsParticipantEndpoint, CallRecordsServiceEndpoint]] = Field(alias="caller", default=None,discriminator="odata_type", )
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	failureInfo: Optional[CallRecordsFailureInfo] = Field(alias="failureInfo", default=None,)
	isTest: Optional[bool] = Field(alias="isTest", default=None,)
	modalities: Optional[list[CallRecordsModality | str]] = Field(alias="modalities", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	segments: Optional[list[CallRecordsSegment]] = Field(alias="segments", default=None,)

from .call_records_participant_endpoint import CallRecordsParticipantEndpoint
from .call_records_service_endpoint import CallRecordsServiceEndpoint
from .call_records_failure_info import CallRecordsFailureInfo
from .call_records_modality import CallRecordsModality
from .call_records_segment import CallRecordsSegment
