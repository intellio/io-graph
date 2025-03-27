from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UpdateRecordingStatusOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UpdateRecordingStatusOperation]] = Field(alias="value", default=None,)

from .update_recording_status_operation import UpdateRecordingStatusOperation

