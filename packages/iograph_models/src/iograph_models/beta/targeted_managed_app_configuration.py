from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TargetedManagedAppConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	customSettings: Optional[list[KeyValuePair]] = Field(alias="customSettings",default=None,)
	settings: Optional[list[DeviceManagementConfigurationSetting]] = Field(alias="settings",default=None,)
	appGroupType: Optional[TargetedManagedAppGroupType | str] = Field(alias="appGroupType",default=None,)
	deployedAppCount: Optional[int] = Field(alias="deployedAppCount",default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned",default=None,)
	targetedAppManagementLevels: Optional[AppManagementLevel | str] = Field(alias="targetedAppManagementLevels",default=None,)
	apps: Optional[list[ManagedMobileApp]] = Field(alias="apps",default=None,)
	assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = Field(alias="assignments",default=None,)
	deploymentSummary: Optional[ManagedAppPolicyDeploymentSummary] = Field(alias="deploymentSummary",default=None,)

from .key_value_pair import KeyValuePair
from .device_management_configuration_setting import DeviceManagementConfigurationSetting
from .targeted_managed_app_group_type import TargetedManagedAppGroupType
from .app_management_level import AppManagementLevel
from .managed_mobile_app import ManagedMobileApp
from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary

