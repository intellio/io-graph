from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsTraceRouteHopCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CallRecordsTraceRouteHop]] = Field(default=None,alias="value",)

from .call_records_trace_route_hop import CallRecordsTraceRouteHop

