from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Call_records_get_direct_routing_calls_with_fromdatetime_todatetimeGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CallRecordsDirectRoutingLogRow]] = Field(alias="value", default=None,)

from .call_records_direct_routing_log_row import CallRecordsDirectRoutingLogRow
