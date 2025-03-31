from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GroupPolicyPresentationCheckBox(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupPolicyPresentationCheckBox"] = Field(alias="@odata.type", default="#microsoft.graph.groupPolicyPresentationCheckBox")
	label: Optional[str] = Field(alias="label", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	definition: Optional[GroupPolicyDefinition] = Field(alias="definition", default=None,)
	defaultChecked: Optional[bool] = Field(alias="defaultChecked", default=None,)

from .group_policy_definition import GroupPolicyDefinition
