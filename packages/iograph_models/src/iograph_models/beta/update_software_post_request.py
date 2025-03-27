from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_softwarePostRequest(BaseModel):
	softwareType: Optional[TeamworkSoftwareType | str] = Field(alias="softwareType", default=None,)
	softwareVersion: Optional[str] = Field(alias="softwareVersion", default=None,)

from .teamwork_software_type import TeamworkSoftwareType

