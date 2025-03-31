from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerRosterMember(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerRosterMember"] = Field(alias="@odata.type",)
	roles: Optional[list[str]] = Field(alias="roles", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)

