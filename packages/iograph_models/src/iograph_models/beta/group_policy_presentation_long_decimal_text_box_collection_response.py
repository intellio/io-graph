from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyPresentationLongDecimalTextBoxCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[GroupPolicyPresentationLongDecimalTextBox]] = Field(alias="value",default=None,)

from .group_policy_presentation_long_decimal_text_box import GroupPolicyPresentationLongDecimalTextBox

