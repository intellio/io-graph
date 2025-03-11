from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyPresentationValueMultiTextCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[GroupPolicyPresentationValueMultiText]] = Field(alias="value",default=None,)

from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText

