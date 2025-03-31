from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GroupPolicyPresentationListBox(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupPolicyPresentationListBox"] = Field(alias="@odata.type", default="#microsoft.graph.groupPolicyPresentationListBox")
	label: Optional[str] = Field(alias="label", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	definition: Optional[GroupPolicyDefinition] = Field(alias="definition", default=None,)
	explicitValue: Optional[bool] = Field(alias="explicitValue", default=None,)
	valuePrefix: Optional[str] = Field(alias="valuePrefix", default=None,)

from .group_policy_definition import GroupPolicyDefinition
