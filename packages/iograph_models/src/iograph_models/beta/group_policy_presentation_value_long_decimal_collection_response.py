from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GroupPolicyPresentationValueLongDecimalCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[GroupPolicyPresentationValueLongDecimal]] = Field(alias="value", default=None,)

from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
