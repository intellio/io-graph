from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsSegment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	callee: SerializeAsAny[Optional[CallRecordsEndpoint]] = Field(default=None,alias="callee",)
	caller: SerializeAsAny[Optional[CallRecordsEndpoint]] = Field(default=None,alias="caller",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	failureInfo: Optional[CallRecordsFailureInfo] = Field(default=None,alias="failureInfo",)
	media: Optional[list[CallRecordsMedia]] = Field(default=None,alias="media",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)

from .call_records_endpoint import CallRecordsEndpoint
from .call_records_endpoint import CallRecordsEndpoint
from .call_records_failure_info import CallRecordsFailureInfo
from .call_records_media import CallRecordsMedia

