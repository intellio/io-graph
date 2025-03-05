from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsFailureInfo(BaseModel):
	reason: Optional[str] = Field(default=None,alias="reason",)
	stage: Optional[CallRecordsFailureStage] = Field(default=None,alias="stage",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .call_records_failure_stage import CallRecordsFailureStage

