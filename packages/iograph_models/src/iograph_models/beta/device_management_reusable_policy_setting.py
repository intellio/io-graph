from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementReusablePolicySetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementReusablePolicySetting"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementReusablePolicySetting")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	referencingConfigurationPolicyCount: Optional[int] = Field(alias="referencingConfigurationPolicyCount", default=None,)
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	settingInstance: Optional[Union[DeviceManagementConfigurationChoiceSettingCollectionInstance, DeviceManagementConfigurationChoiceSettingInstance, DeviceManagementConfigurationGroupSettingCollectionInstance, DeviceManagementConfigurationGroupSettingInstance, DeviceManagementConfigurationSettingGroupCollectionInstance, DeviceManagementConfigurationSettingGroupInstance, DeviceManagementConfigurationSimpleSettingCollectionInstance, DeviceManagementConfigurationSimpleSettingInstance]] = Field(alias="settingInstance", default=None,discriminator="odata_type", )
	version: Optional[int] = Field(alias="version", default=None,)
	referencingConfigurationPolicies: Optional[list[DeviceManagementConfigurationPolicy]] = Field(alias="referencingConfigurationPolicies", default=None,)

from .device_management_configuration_choice_setting_collection_instance import DeviceManagementConfigurationChoiceSettingCollectionInstance
from .device_management_configuration_choice_setting_instance import DeviceManagementConfigurationChoiceSettingInstance
from .device_management_configuration_group_setting_collection_instance import DeviceManagementConfigurationGroupSettingCollectionInstance
from .device_management_configuration_group_setting_instance import DeviceManagementConfigurationGroupSettingInstance
from .device_management_configuration_setting_group_collection_instance import DeviceManagementConfigurationSettingGroupCollectionInstance
from .device_management_configuration_setting_group_instance import DeviceManagementConfigurationSettingGroupInstance
from .device_management_configuration_simple_setting_collection_instance import DeviceManagementConfigurationSimpleSettingCollectionInstance
from .device_management_configuration_simple_setting_instance import DeviceManagementConfigurationSimpleSettingInstance
from .device_management_configuration_policy import DeviceManagementConfigurationPolicy
