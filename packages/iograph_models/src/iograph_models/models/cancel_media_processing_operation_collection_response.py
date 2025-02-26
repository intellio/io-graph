from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CancelMediaProcessingOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CancelMediaProcessingOperation] = Field(alias="value",)

from .cancel_media_processing_operation import CancelMediaProcessingOperation

