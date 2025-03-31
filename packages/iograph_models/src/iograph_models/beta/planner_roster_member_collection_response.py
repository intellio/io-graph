from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PlannerRosterMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PlannerRosterMember]] = Field(alias="value", default=None,)

from .planner_roster_member import PlannerRosterMember
