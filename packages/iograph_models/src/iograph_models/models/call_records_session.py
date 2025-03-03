from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CallRecordsSession(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	callee: Optional[CallRecordsEndpoint] = Field(default=None,alias="callee",)
	caller: Optional[CallRecordsEndpoint] = Field(default=None,alias="caller",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	failureInfo: Optional[CallRecordsFailureInfo] = Field(default=None,alias="failureInfo",)
	isTest: Optional[bool] = Field(default=None,alias="isTest",)
	modalities: Optional[list[CallRecordsModality]] = Field(default=None,alias="modalities",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	segments: Optional[list[CallRecordsSegment]] = Field(default=None,alias="segments",)

from .call_records_endpoint import CallRecordsEndpoint
from .call_records_endpoint import CallRecordsEndpoint
from .call_records_failure_info import CallRecordsFailureInfo
from .call_records_modality import CallRecordsModality
from .call_records_segment import CallRecordsSegment

