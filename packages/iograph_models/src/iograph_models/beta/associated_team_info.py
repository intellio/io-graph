from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AssociatedTeamInfo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.associatedTeamInfo"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	team: Optional[Team] = Field(alias="team", default=None,)

from .team import Team
