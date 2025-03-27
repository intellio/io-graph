from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessUsageProfilingPoint(BaseModel):
	internetAccessTrafficCount: Optional[int] = Field(alias="internetAccessTrafficCount", default=None,)
	microsoft365AccessTrafficCount: Optional[int] = Field(alias="microsoft365AccessTrafficCount", default=None,)
	privateAccessTrafficCount: Optional[int] = Field(alias="privateAccessTrafficCount", default=None,)
	timeStampDateTime: Optional[datetime] = Field(alias="timeStampDateTime", default=None,)
	totalTrafficCount: Optional[int] = Field(alias="totalTrafficCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


