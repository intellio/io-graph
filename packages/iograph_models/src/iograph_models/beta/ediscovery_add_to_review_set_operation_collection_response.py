from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EdiscoveryAddToReviewSetOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EdiscoveryAddToReviewSetOperation]] = Field(alias="value", default=None,)

from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
