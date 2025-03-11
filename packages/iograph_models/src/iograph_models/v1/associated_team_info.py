from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssociatedTeamInfo(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	team: Optional[Team] = Field(alias="team",default=None,)

from .team import Team

