from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EngagementAsyncOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[EngagementAsyncOperation] = Field(alias="value",)

from .engagement_async_operation import EngagementAsyncOperation

