from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class NetworkaccessAlertFrequencyPoint(BaseModel):
	highSeverityCount: Optional[int] = Field(alias="highSeverityCount", default=None,)
	informationalSeverityCount: Optional[int] = Field(alias="informationalSeverityCount", default=None,)
	lowSeverityCount: Optional[int] = Field(alias="lowSeverityCount", default=None,)
	mediumSeverityCount: Optional[int] = Field(alias="mediumSeverityCount", default=None,)
	timeStampDateTime: Optional[datetime] = Field(alias="timeStampDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

