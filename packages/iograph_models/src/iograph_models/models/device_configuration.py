from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: list[DeviceConfigurationAssignment] = Field(alias="assignments",)
	deviceSettingStateSummaries: list[SettingStateDeviceSummary] = Field(alias="deviceSettingStateSummaries",)
	deviceStatuses: list[DeviceConfigurationDeviceStatus] = Field(alias="deviceStatuses",)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(default=None,alias="deviceStatusOverview",)
	userStatuses: list[DeviceConfigurationUserStatus] = Field(alias="userStatuses",)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(default=None,alias="userStatusOverview",)

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
			if mapping_key == "#microsoft.graph.androidCustomConfiguration":
				from .android_custom_configuration import AndroidCustomConfiguration
				return AndroidCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidGeneralDeviceConfiguration":
				from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
				return AndroidGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileCustomConfiguration":
				from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
				return AndroidWorkProfileCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration":
				from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
				return AndroidWorkProfileGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.appleDeviceFeaturesConfigurationBase":
				from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
				return AppleDeviceFeaturesConfigurationBase.model_validate(data)
			if mapping_key == "#microsoft.graph.iosDeviceFeaturesConfiguration":
				from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
				return IosDeviceFeaturesConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSDeviceFeaturesConfiguration":
				from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
				return MacOSDeviceFeaturesConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.editionUpgradeConfiguration":
				from .edition_upgrade_configuration import EditionUpgradeConfiguration
				return EditionUpgradeConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCertificateProfile":
				from .ios_certificate_profile import IosCertificateProfile
				return IosCertificateProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCustomConfiguration":
				from .ios_custom_configuration import IosCustomConfiguration
				return IosCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosGeneralDeviceConfiguration":
				from .ios_general_device_configuration import IosGeneralDeviceConfiguration
				return IosGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosUpdateConfiguration":
				from .ios_update_configuration import IosUpdateConfiguration
				return IosUpdateConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSCustomConfiguration":
				from .mac_o_s_custom_configuration import MacOSCustomConfiguration
				return MacOSCustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSGeneralDeviceConfiguration":
				from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
				return MacOSGeneralDeviceConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.sharedPCConfiguration":
				from .shared_p_c_configuration import SharedPCConfiguration
				return SharedPCConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10CustomConfiguration":
				from .windows10_custom_configuration import Windows10CustomConfiguration
				return Windows10CustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EndpointProtectionConfiguration":
				from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
				return Windows10EndpointProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration":
				from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
				return Windows10EnterpriseModernAppManagementConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10GeneralConfiguration":
				from .windows10_general_configuration import Windows10GeneralConfiguration
				return Windows10GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10SecureAssessmentConfiguration":
				from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
				return Windows10SecureAssessmentConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10TeamGeneralConfiguration":
				from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
				return Windows10TeamGeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81GeneralConfiguration":
				from .windows81_general_configuration import Windows81GeneralConfiguration
				return Windows81GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration":
				from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
				return WindowsDefenderAdvancedThreatProtectionConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81CustomConfiguration":
				from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
				return WindowsPhone81CustomConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81GeneralConfiguration":
				from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
				return WindowsPhone81GeneralConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdateForBusinessConfiguration":
				from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
				return WindowsUpdateForBusinessConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview

