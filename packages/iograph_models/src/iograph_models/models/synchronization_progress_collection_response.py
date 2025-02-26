from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationProgressCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SynchronizationProgress] = Field(alias="value",)

from .synchronization_progress import SynchronizationProgress

