from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyPresentationComboBox(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	label: Optional[str] = Field(alias="label",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	definition: Optional[GroupPolicyDefinition] = Field(alias="definition",default=None,)
	defaultValue: Optional[str] = Field(alias="defaultValue",default=None,)
	maxLength: Optional[int] = Field(alias="maxLength",default=None,)
	required: Optional[bool] = Field(alias="required",default=None,)
	suggestions: Optional[list[str]] = Field(alias="suggestions",default=None,)

from .group_policy_definition import GroupPolicyDefinition

