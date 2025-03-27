from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsFailureInfo(BaseModel):
	reason: Optional[str] = Field(alias="reason", default=None,)
	stage: Optional[CallRecordsFailureStage | str] = Field(alias="stage", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .call_records_failure_stage import CallRecordsFailureStage

