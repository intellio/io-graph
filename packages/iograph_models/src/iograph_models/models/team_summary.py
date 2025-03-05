from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamSummary(BaseModel):
	guestsCount: Optional[int] = Field(default=None,alias="guestsCount",)
	membersCount: Optional[int] = Field(default=None,alias="membersCount",)
	ownersCount: Optional[int] = Field(default=None,alias="ownersCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


