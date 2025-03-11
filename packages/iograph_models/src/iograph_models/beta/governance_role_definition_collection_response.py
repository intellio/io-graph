from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GovernanceRoleDefinitionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[GovernanceRoleDefinition]] = Field(alias="value",default=None,)

from .governance_role_definition import GovernanceRoleDefinition

