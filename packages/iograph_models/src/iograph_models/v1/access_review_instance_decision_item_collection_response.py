from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewInstanceDecisionItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AccessReviewInstanceDecisionItem]] = Field(alias="value", default=None,)

from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
