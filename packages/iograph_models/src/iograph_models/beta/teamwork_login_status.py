from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkLoginStatus(BaseModel):
	exchangeConnection: Optional[TeamworkConnection] = Field(alias="exchangeConnection", default=None,)
	skypeConnection: Optional[TeamworkConnection] = Field(alias="skypeConnection", default=None,)
	teamsConnection: Optional[TeamworkConnection] = Field(alias="teamsConnection", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teamwork_connection import TeamworkConnection
from .teamwork_connection import TeamworkConnection
from .teamwork_connection import TeamworkConnection

