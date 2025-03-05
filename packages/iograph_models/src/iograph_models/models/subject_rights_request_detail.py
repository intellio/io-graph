from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequestDetail(BaseModel):
	excludedItemCount: Optional[int] = Field(default=None,alias="excludedItemCount",)
	insightCounts: Optional[list[KeyValuePair]] = Field(default=None,alias="insightCounts",)
	itemCount: Optional[int] = Field(default=None,alias="itemCount",)
	itemNeedReview: Optional[int] = Field(default=None,alias="itemNeedReview",)
	productItemCounts: Optional[list[KeyValuePair]] = Field(default=None,alias="productItemCounts",)
	signedOffItemCount: Optional[int] = Field(default=None,alias="signedOffItemCount",)
	totalItemSize: Optional[int] = Field(default=None,alias="totalItemSize",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .key_value_pair import KeyValuePair
from .key_value_pair import KeyValuePair

