from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkSoftwareUpdateHealth(BaseModel):
	adminAgentSoftwareUpdateStatus: Optional[TeamworkSoftwareUpdateStatus] = Field(alias="adminAgentSoftwareUpdateStatus", default=None,)
	companyPortalSoftwareUpdateStatus: Optional[TeamworkSoftwareUpdateStatus] = Field(alias="companyPortalSoftwareUpdateStatus", default=None,)
	firmwareSoftwareUpdateStatus: Optional[TeamworkSoftwareUpdateStatus] = Field(alias="firmwareSoftwareUpdateStatus", default=None,)
	operatingSystemSoftwareUpdateStatus: Optional[TeamworkSoftwareUpdateStatus] = Field(alias="operatingSystemSoftwareUpdateStatus", default=None,)
	partnerAgentSoftwareUpdateStatus: Optional[TeamworkSoftwareUpdateStatus] = Field(alias="partnerAgentSoftwareUpdateStatus", default=None,)
	teamsClientSoftwareUpdateStatus: Optional[TeamworkSoftwareUpdateStatus] = Field(alias="teamsClientSoftwareUpdateStatus", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teamwork_software_update_status import TeamworkSoftwareUpdateStatus
from .teamwork_software_update_status import TeamworkSoftwareUpdateStatus
from .teamwork_software_update_status import TeamworkSoftwareUpdateStatus
from .teamwork_software_update_status import TeamworkSoftwareUpdateStatus
from .teamwork_software_update_status import TeamworkSoftwareUpdateStatus
from .teamwork_software_update_status import TeamworkSoftwareUpdateStatus

