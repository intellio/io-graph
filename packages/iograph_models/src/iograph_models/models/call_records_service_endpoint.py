from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsServiceEndpoint(BaseModel):
	userAgent: Optional[CallRecordsUserAgent] = Field(default=None,alias="userAgent",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .call_records_user_agent import CallRecordsUserAgent

