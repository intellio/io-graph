from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SharedPCConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(default=None,alias="assignments",)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(default=None,alias="deviceSettingStateSummaries",)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(default=None,alias="deviceStatuses",)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(default=None,alias="deviceStatusOverview",)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(default=None,alias="userStatuses",)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(default=None,alias="userStatusOverview",)
	accountManagerPolicy: Optional[SharedPCAccountManagerPolicy] = Field(default=None,alias="accountManagerPolicy",)
	allowedAccounts: Optional[SharedPCAllowedAccountType] = Field(default=None,alias="allowedAccounts",)
	allowLocalStorage: Optional[bool] = Field(default=None,alias="allowLocalStorage",)
	disableAccountManager: Optional[bool] = Field(default=None,alias="disableAccountManager",)
	disableEduPolicies: Optional[bool] = Field(default=None,alias="disableEduPolicies",)
	disablePowerPolicies: Optional[bool] = Field(default=None,alias="disablePowerPolicies",)
	disableSignInOnResume: Optional[bool] = Field(default=None,alias="disableSignInOnResume",)
	enabled: Optional[bool] = Field(default=None,alias="enabled",)
	idleTimeBeforeSleepInSeconds: Optional[int] = Field(default=None,alias="idleTimeBeforeSleepInSeconds",)
	kioskAppDisplayName: Optional[str] = Field(default=None,alias="kioskAppDisplayName",)
	kioskAppUserModelId: Optional[str] = Field(default=None,alias="kioskAppUserModelId",)
	maintenanceStartTime: Optional[str] = Field(default=None,alias="maintenanceStartTime",)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .shared_p_c_account_manager_policy import SharedPCAccountManagerPolicy
from .shared_p_c_allowed_account_type import SharedPCAllowedAccountType

