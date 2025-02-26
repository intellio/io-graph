from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsServiceUserAgent(BaseModel):
	applicationVersion: Optional[str] = Field(default=None,alias="applicationVersion",)
	headerValue: Optional[str] = Field(default=None,alias="headerValue",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	role: Optional[CallRecordsServiceRole] = Field(default=None,alias="role",)

from .call_records_service_role import CallRecordsServiceRole

