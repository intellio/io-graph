from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Filter_by_current_user_with_onGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AccessReviewInstance]] = Field(alias="value", default=None,)

from .access_review_instance import AccessReviewInstance
