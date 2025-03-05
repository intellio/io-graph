from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Call_records_get_direct_routing_calls_with_fromdatetime_todatetimeGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CallRecordsDirectRoutingLogRow]] = Field(default=None,alias="value",)

from .call_records_direct_routing_log_row import CallRecordsDirectRoutingLogRow

