from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsMediaStreamCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CallRecordsMediaStream]] = Field(alias="value", default=None,)

from .call_records_media_stream import CallRecordsMediaStream
