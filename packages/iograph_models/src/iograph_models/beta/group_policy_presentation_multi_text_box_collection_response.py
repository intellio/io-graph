from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyPresentationMultiTextBoxCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[GroupPolicyPresentationMultiTextBox]] = Field(alias="value",default=None,)

from .group_policy_presentation_multi_text_box import GroupPolicyPresentationMultiTextBox

