from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsServiceEndpoint(BaseModel):
	userAgent: SerializeAsAny[Optional[CallRecordsUserAgent]] = Field(alias="userAgent",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .call_records_user_agent import CallRecordsUserAgent

