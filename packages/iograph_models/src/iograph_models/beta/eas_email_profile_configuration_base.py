from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class EasEmailProfileConfigurationBase(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.easEmailProfileConfigurationBase"] = Field(alias="@odata.type", default="#microsoft.graph.easEmailProfileConfigurationBase")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceManagementApplicabilityRuleDeviceMode: Optional[DeviceManagementApplicabilityRuleDeviceMode] = Field(alias="deviceManagementApplicabilityRuleDeviceMode", default=None,)
	deviceManagementApplicabilityRuleOsEdition: Optional[DeviceManagementApplicabilityRuleOsEdition] = Field(alias="deviceManagementApplicabilityRuleOsEdition", default=None,)
	deviceManagementApplicabilityRuleOsVersion: Optional[DeviceManagementApplicabilityRuleOsVersion] = Field(alias="deviceManagementApplicabilityRuleOsVersion", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	supportsScopeTags: Optional[bool] = Field(alias="supportsScopeTags", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments", default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries", default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses", default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview", default=None,)
	groupAssignments: Optional[list[DeviceConfigurationGroupAssignment]] = Field(alias="groupAssignments", default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses", default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview", default=None,)
	customDomainName: Optional[str] = Field(alias="customDomainName", default=None,)
	userDomainNameSource: Optional[DomainNameSource | str] = Field(alias="userDomainNameSource", default=None,)
	usernameAADSource: Optional[UsernameSource | str] = Field(alias="usernameAADSource", default=None,)
	usernameSource: Optional[UserEmailSource | str] = Field(alias="usernameSource", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.iosEasEmailProfileConfiguration":
				from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
				return IosEasEmailProfileConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EasEmailProfileConfiguration":
				from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
				return Windows10EasEmailProfileConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhoneEASEmailProfileConfiguration":
				from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
				return WindowsPhoneEASEmailProfileConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

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
from .domain_name_source import DomainNameSource
from .username_source import UsernameSource
from .user_email_source import UserEmailSource
