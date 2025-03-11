from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SharedPCConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	deviceManagementApplicabilityRuleDeviceMode: Optional[DeviceManagementApplicabilityRuleDeviceMode] = Field(alias="deviceManagementApplicabilityRuleDeviceMode",default=None,)
	deviceManagementApplicabilityRuleOsEdition: Optional[DeviceManagementApplicabilityRuleOsEdition] = Field(alias="deviceManagementApplicabilityRuleOsEdition",default=None,)
	deviceManagementApplicabilityRuleOsVersion: Optional[DeviceManagementApplicabilityRuleOsVersion] = Field(alias="deviceManagementApplicabilityRuleOsVersion",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	supportsScopeTags: Optional[bool] = Field(alias="supportsScopeTags",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments",default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries",default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview",default=None,)
	groupAssignments: Optional[list[DeviceConfigurationGroupAssignment]] = Field(alias="groupAssignments",default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview",default=None,)
	accountManagerPolicy: Optional[SharedPCAccountManagerPolicy] = Field(alias="accountManagerPolicy",default=None,)
	allowedAccounts: Optional[SharedPCAllowedAccountType | str] = Field(alias="allowedAccounts",default=None,)
	allowLocalStorage: Optional[bool] = Field(alias="allowLocalStorage",default=None,)
	disableAccountManager: Optional[bool] = Field(alias="disableAccountManager",default=None,)
	disableEduPolicies: Optional[bool] = Field(alias="disableEduPolicies",default=None,)
	disablePowerPolicies: Optional[bool] = Field(alias="disablePowerPolicies",default=None,)
	disableSignInOnResume: Optional[bool] = Field(alias="disableSignInOnResume",default=None,)
	enabled: Optional[bool] = Field(alias="enabled",default=None,)
	fastFirstSignIn: Optional[Enablement | str] = Field(alias="fastFirstSignIn",default=None,)
	idleTimeBeforeSleepInSeconds: Optional[int] = Field(alias="idleTimeBeforeSleepInSeconds",default=None,)
	kioskAppDisplayName: Optional[str] = Field(alias="kioskAppDisplayName",default=None,)
	kioskAppUserModelId: Optional[str] = Field(alias="kioskAppUserModelId",default=None,)
	localStorage: Optional[Enablement | str] = Field(alias="localStorage",default=None,)
	maintenanceStartTime: Optional[str] = Field(alias="maintenanceStartTime",default=None,)
	setAccountManager: Optional[Enablement | str] = Field(alias="setAccountManager",default=None,)
	setEduPolicies: Optional[Enablement | str] = Field(alias="setEduPolicies",default=None,)
	setPowerPolicies: Optional[Enablement | str] = Field(alias="setPowerPolicies",default=None,)
	signInOnResume: Optional[Enablement | str] = Field(alias="signInOnResume",default=None,)

from .device_management_applicability_rule_device_mode import DeviceManagementApplicabilityRuleDeviceMode
from .device_management_applicability_rule_os_edition import DeviceManagementApplicabilityRuleOsEdition
from .device_management_applicability_rule_os_version import DeviceManagementApplicabilityRuleOsVersion
from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .shared_p_c_account_manager_policy import SharedPCAccountManagerPolicy
from .shared_p_c_allowed_account_type import SharedPCAllowedAccountType
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement
from .enablement import Enablement

