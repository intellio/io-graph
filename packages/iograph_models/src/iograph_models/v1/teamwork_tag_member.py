from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamworkTagMember(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamworkTagMember"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)

