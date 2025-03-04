from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Call_records_get_pstn_calls_with_fromdatetime_todatetimeGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CallRecordsPstnCallLogRow]] = Field(default=None,alias="value",)

from .call_records_pstn_call_log_row import CallRecordsPstnCallLogRow

