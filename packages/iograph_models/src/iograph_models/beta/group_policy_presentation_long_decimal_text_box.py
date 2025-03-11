from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyPresentationLongDecimalTextBox(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	label: Optional[str] = Field(alias="label",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	definition: Optional[GroupPolicyDefinition] = Field(alias="definition",default=None,)
	defaultValue: Optional[int] = Field(alias="defaultValue",default=None,)
	maxValue: Optional[int] = Field(alias="maxValue",default=None,)
	minValue: Optional[int] = Field(alias="minValue",default=None,)
	required: Optional[bool] = Field(alias="required",default=None,)
	spin: Optional[bool] = Field(alias="spin",default=None,)
	spinStep: Optional[int] = Field(alias="spinStep",default=None,)

from .group_policy_definition import GroupPolicyDefinition

