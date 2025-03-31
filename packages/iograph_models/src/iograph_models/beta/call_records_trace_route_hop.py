from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsTraceRouteHop(BaseModel):
	hopCount: Optional[int] = Field(alias="hopCount", default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	roundTripTime: Optional[str] = Field(alias="roundTripTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

