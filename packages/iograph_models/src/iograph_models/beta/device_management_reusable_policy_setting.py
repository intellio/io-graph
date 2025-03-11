from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementReusablePolicySetting(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	referencingConfigurationPolicyCount: Optional[int] = Field(alias="referencingConfigurationPolicyCount",default=None,)
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId",default=None,)
	settingInstance: SerializeAsAny[Optional[DeviceManagementConfigurationSettingInstance]] = Field(alias="settingInstance",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	referencingConfigurationPolicies: Optional[list[DeviceManagementConfigurationPolicy]] = Field(alias="referencingConfigurationPolicies",default=None,)

from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance
from .device_management_configuration_policy import DeviceManagementConfigurationPolicy

