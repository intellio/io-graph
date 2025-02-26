from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RecordOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[RecordOperation] = Field(alias="value",)

from .record_operation import RecordOperation

