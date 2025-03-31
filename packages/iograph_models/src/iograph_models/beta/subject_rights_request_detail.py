from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SubjectRightsRequestDetail(BaseModel):
	excludedItemCount: Optional[int] = Field(alias="excludedItemCount", default=None,)
	insightCounts: Optional[list[KeyValuePair]] = Field(alias="insightCounts", default=None,)
	itemCount: Optional[int] = Field(alias="itemCount", default=None,)
	itemNeedReview: Optional[int] = Field(alias="itemNeedReview", default=None,)
	productItemCounts: Optional[list[KeyValuePair]] = Field(alias="productItemCounts", default=None,)
	signedOffItemCount: Optional[int] = Field(alias="signedOffItemCount", default=None,)
	totalItemSize: Optional[int] = Field(alias="totalItemSize", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .key_value_pair import KeyValuePair
