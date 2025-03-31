from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamSummary(BaseModel):
	guestsCount: Optional[int] = Field(alias="guestsCount", default=None,)
	membersCount: Optional[int] = Field(alias="membersCount", default=None,)
	ownersCount: Optional[int] = Field(alias="ownersCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

