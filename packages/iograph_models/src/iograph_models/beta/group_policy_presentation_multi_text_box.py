from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GroupPolicyPresentationMultiTextBox(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupPolicyPresentationMultiTextBox"] = Field(alias="@odata.type", default="#microsoft.graph.groupPolicyPresentationMultiTextBox")
	label: Optional[str] = Field(alias="label", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	definition: Optional[GroupPolicyDefinition] = Field(alias="definition", default=None,)
	maxLength: Optional[int] = Field(alias="maxLength", default=None,)
	maxStrings: Optional[int] = Field(alias="maxStrings", default=None,)
	required: Optional[bool] = Field(alias="required", default=None,)

from .group_policy_definition import GroupPolicyDefinition
