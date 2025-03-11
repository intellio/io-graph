from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyDefinitionFileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[GroupPolicyDefinitionFile]]] = Field(alias="value",default=None,)

from .group_policy_definition_file import GroupPolicyDefinitionFile

