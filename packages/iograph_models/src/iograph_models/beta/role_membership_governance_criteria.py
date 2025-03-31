from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class RoleMembershipGovernanceCriteria(BaseModel):
	odata_type: Literal["#microsoft.graph.roleMembershipGovernanceCriteria"] = Field(alias="@odata.type", default="#microsoft.graph.roleMembershipGovernanceCriteria")
	roleId: Optional[str] = Field(alias="roleId", default=None,)
	roleTemplateId: Optional[str] = Field(alias="roleTemplateId", default=None,)

