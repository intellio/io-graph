from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamworkDeviceSoftwareVersions(BaseModel):
	adminAgentSoftwareVersion: Optional[str] = Field(alias="adminAgentSoftwareVersion", default=None,)
	firmwareSoftwareVersion: Optional[str] = Field(alias="firmwareSoftwareVersion", default=None,)
	operatingSystemSoftwareVersion: Optional[str] = Field(alias="operatingSystemSoftwareVersion", default=None,)
	partnerAgentSoftwareVersion: Optional[str] = Field(alias="partnerAgentSoftwareVersion", default=None,)
	teamsClientSoftwareVersion: Optional[str] = Field(alias="teamsClientSoftwareVersion", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

