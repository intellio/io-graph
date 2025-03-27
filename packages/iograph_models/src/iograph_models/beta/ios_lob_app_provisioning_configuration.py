from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosLobAppProvisioningConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	payload: Optional[str] = Field(alias="payload", default=None,)
	payloadFileName: Optional[str] = Field(alias="payloadFileName", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[IosLobAppProvisioningConfigurationAssignment]] = Field(alias="assignments", default=None,)
	deviceStatuses: Optional[list[ManagedDeviceMobileAppConfigurationDeviceStatus]] = Field(alias="deviceStatuses", default=None,)
	groupAssignments: Optional[list[MobileAppProvisioningConfigGroupAssignment]] = Field(alias="groupAssignments", default=None,)
	userStatuses: Optional[list[ManagedDeviceMobileAppConfigurationUserStatus]] = Field(alias="userStatuses", default=None,)

from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
from .mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment
from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus

