from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryReviewSetQueryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SecurityEdiscoveryReviewSetQuery]] = Field(alias="value",default=None,)

from .security_ediscovery_review_set_query import SecurityEdiscoveryReviewSetQuery

