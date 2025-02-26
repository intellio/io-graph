from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsTraceRouteHop(BaseModel):
	hopCount: Optional[int] = Field(default=None,alias="hopCount",)
	ipAddress: Optional[str] = Field(default=None,alias="ipAddress",)
	roundTripTime: Optional[str] = Field(default=None,alias="roundTripTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


