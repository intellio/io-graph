from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StopRecordingOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[StopRecordingOperation]] = Field(alias="value",default=None,)

from .stop_recording_operation import StopRecordingOperation

