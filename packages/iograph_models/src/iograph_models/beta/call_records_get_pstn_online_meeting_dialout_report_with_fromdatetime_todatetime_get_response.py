from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Call_records_get_pstn_online_meeting_dialout_report_with_fromdatetime_todatetimeGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CallRecordsPstnOnlineMeetingDialoutReport]] = Field(alias="value", default=None,)

from .call_records_pstn_online_meeting_dialout_report import CallRecordsPstnOnlineMeetingDialoutReport
