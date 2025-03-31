from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EngagementAsyncOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EngagementAsyncOperation]] = Field(alias="value", default=None,)

from .engagement_async_operation import EngagementAsyncOperation
