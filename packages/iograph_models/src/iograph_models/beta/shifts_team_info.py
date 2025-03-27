from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ShiftsTeamInfo(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	teamId: Optional[str] = Field(alias="teamId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


