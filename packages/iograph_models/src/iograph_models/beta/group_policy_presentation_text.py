from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyPresentationText(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	label: Optional[str] = Field(alias="label",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	definition: Optional[GroupPolicyDefinition] = Field(alias="definition",default=None,)

from .group_policy_definition import GroupPolicyDefinition

