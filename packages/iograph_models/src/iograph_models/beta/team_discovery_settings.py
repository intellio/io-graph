from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamDiscoverySettings(BaseModel):
	showInTeamsSearchAndSuggestions: Optional[bool] = Field(alias="showInTeamsSearchAndSuggestions",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


