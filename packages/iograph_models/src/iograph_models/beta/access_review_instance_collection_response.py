from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewInstanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AccessReviewInstance]] = Field(alias="value", default=None,)

from .access_review_instance import AccessReviewInstance
