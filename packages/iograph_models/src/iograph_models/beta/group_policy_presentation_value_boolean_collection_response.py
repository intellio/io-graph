from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GroupPolicyPresentationValueBooleanCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[GroupPolicyPresentationValueBoolean]] = Field(alias="value", default=None,)

from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
