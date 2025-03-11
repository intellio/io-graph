from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkDeviceHealth(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	connection: Optional[TeamworkConnection] = Field(alias="connection",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	hardwareHealth: Optional[TeamworkHardwareHealth] = Field(alias="hardwareHealth",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	loginStatus: Optional[TeamworkLoginStatus] = Field(alias="loginStatus",default=None,)
	peripheralsHealth: Optional[TeamworkPeripheralsHealth] = Field(alias="peripheralsHealth",default=None,)
	softwareUpdateHealth: Optional[TeamworkSoftwareUpdateHealth] = Field(alias="softwareUpdateHealth",default=None,)

from .teamwork_connection import TeamworkConnection
from .identity_set import IdentitySet
from .teamwork_hardware_health import TeamworkHardwareHealth
from .identity_set import IdentitySet
from .teamwork_login_status import TeamworkLoginStatus
from .teamwork_peripherals_health import TeamworkPeripheralsHealth
from .teamwork_software_update_health import TeamworkSoftwareUpdateHealth

