from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GroupPolicyPresentationDropdownList(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupPolicyPresentationDropdownList"] = Field(alias="@odata.type", default="#microsoft.graph.groupPolicyPresentationDropdownList")
	label: Optional[str] = Field(alias="label", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	definition: Optional[GroupPolicyDefinition] = Field(alias="definition", default=None,)
	defaultItem: Optional[GroupPolicyPresentationDropdownListItem] = Field(alias="defaultItem", default=None,)
	items: Optional[list[GroupPolicyPresentationDropdownListItem]] = Field(alias="items", default=None,)
	required: Optional[bool] = Field(alias="required", default=None,)

from .group_policy_definition import GroupPolicyDefinition
from .group_policy_presentation_dropdown_list_item import GroupPolicyPresentationDropdownListItem
