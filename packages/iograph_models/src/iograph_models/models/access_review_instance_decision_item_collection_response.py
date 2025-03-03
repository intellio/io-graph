from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewInstanceDecisionItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AccessReviewInstanceDecisionItem]] = Field(default=None,alias="value",)

from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem

