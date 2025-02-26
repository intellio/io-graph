from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityEdiscoveryReviewSetQueryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityEdiscoveryReviewSetQuery] = Field(alias="value",)

from .security_ediscovery_review_set_query import SecurityEdiscoveryReviewSetQuery

