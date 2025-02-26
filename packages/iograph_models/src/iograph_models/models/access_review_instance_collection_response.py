from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewInstanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AccessReviewInstance] = Field(alias="value",)

from .access_review_instance import AccessReviewInstance

