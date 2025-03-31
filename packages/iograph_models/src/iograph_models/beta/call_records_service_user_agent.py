from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CallRecordsServiceUserAgent(BaseModel):
	applicationVersion: Optional[str] = Field(alias="applicationVersion", default=None,)
	headerValue: Optional[str] = Field(alias="headerValue", default=None,)
	odata_type: Literal["#microsoft.graph.callRecords.serviceUserAgent"] = Field(alias="@odata.type", default="#microsoft.graph.callRecords.serviceUserAgent")
	role: Optional[CallRecordsServiceRole | str] = Field(alias="role", default=None,)

from .call_records_service_role import CallRecordsServiceRole
