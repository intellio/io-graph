from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsSegment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	callee: SerializeAsAny[Optional[CallRecordsEndpoint]] = Field(alias="callee",default=None,)
	caller: SerializeAsAny[Optional[CallRecordsEndpoint]] = Field(alias="caller",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	failureInfo: Optional[CallRecordsFailureInfo] = Field(alias="failureInfo",default=None,)
	media: Optional[list[CallRecordsMedia]] = Field(alias="media",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)

from .call_records_endpoint import CallRecordsEndpoint
from .call_records_endpoint import CallRecordsEndpoint
from .call_records_failure_info import CallRecordsFailureInfo
from .call_records_media import CallRecordsMedia

