from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkSoftwareUpdateStatus(BaseModel):
	availableVersion: Optional[str] = Field(alias="availableVersion", default=None,)
	currentVersion: Optional[str] = Field(alias="currentVersion", default=None,)
	softwareFreshness: Optional[TeamworkSoftwareFreshness | str] = Field(alias="softwareFreshness", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teamwork_software_freshness import TeamworkSoftwareFreshness

