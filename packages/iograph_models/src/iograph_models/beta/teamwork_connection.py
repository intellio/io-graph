from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TeamworkConnection(BaseModel):
	connectionStatus: Optional[TeamworkConnectionStatus | str] = Field(alias="connectionStatus", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teamwork_connection_status import TeamworkConnectionStatus
