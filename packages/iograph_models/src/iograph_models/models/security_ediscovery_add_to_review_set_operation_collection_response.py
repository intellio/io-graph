from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityEdiscoveryAddToReviewSetOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SecurityEdiscoveryAddToReviewSetOperation]] = Field(default=None,alias="value",)

from .security_ediscovery_add_to_review_set_operation import SecurityEdiscoveryAddToReviewSetOperation

