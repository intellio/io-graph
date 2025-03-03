from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityEdiscoveryReviewTagCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SecurityEdiscoveryReviewTag]] = Field(default=None,alias="value",)

from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag

