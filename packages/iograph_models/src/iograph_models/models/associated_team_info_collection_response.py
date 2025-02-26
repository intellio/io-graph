from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AssociatedTeamInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AssociatedTeamInfo] = Field(alias="value",)

from .associated_team_info import AssociatedTeamInfo

