from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkDevice(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activityState: Optional[TeamworkDeviceActivityState | str] = Field(alias="activityState",default=None,)
	companyAssetTag: Optional[str] = Field(alias="companyAssetTag",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	currentUser: Optional[TeamworkUserIdentity] = Field(alias="currentUser",default=None,)
	deviceType: Optional[TeamworkDeviceType | str] = Field(alias="deviceType",default=None,)
	hardwareDetail: Optional[TeamworkHardwareDetail] = Field(alias="hardwareDetail",default=None,)
	healthStatus: Optional[TeamworkDeviceHealthStatus | str] = Field(alias="healthStatus",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	notes: Optional[str] = Field(alias="notes",default=None,)
	activity: Optional[TeamworkDeviceActivity] = Field(alias="activity",default=None,)
	configuration: Optional[TeamworkDeviceConfiguration] = Field(alias="configuration",default=None,)
	health: Optional[TeamworkDeviceHealth] = Field(alias="health",default=None,)
	operations: Optional[list[TeamworkDeviceOperation]] = Field(alias="operations",default=None,)

from .teamwork_device_activity_state import TeamworkDeviceActivityState
from .identity_set import IdentitySet
from .teamwork_user_identity import TeamworkUserIdentity
from .teamwork_device_type import TeamworkDeviceType
from .teamwork_hardware_detail import TeamworkHardwareDetail
from .teamwork_device_health_status import TeamworkDeviceHealthStatus
from .identity_set import IdentitySet
from .teamwork_device_activity import TeamworkDeviceActivity
from .teamwork_device_configuration import TeamworkDeviceConfiguration
from .teamwork_device_health import TeamworkDeviceHealth
from .teamwork_device_operation import TeamworkDeviceOperation

