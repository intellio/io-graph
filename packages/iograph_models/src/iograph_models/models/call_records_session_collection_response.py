from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsSessionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CallRecordsSession] = Field(alias="value",)

from .call_records_session import CallRecordsSession

