from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsServiceUserAgent(BaseModel):
	applicationVersion: Optional[str] = Field(alias="applicationVersion",default=None,)
	headerValue: Optional[str] = Field(alias="headerValue",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	role: Optional[str | CallRecordsServiceRole] = Field(alias="role",default=None,)

from .call_records_service_role import CallRecordsServiceRole

