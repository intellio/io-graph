from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DeviceManagementConfigurationSimpleSettingDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	accessTypes: Optional[DeviceManagementConfigurationSettingAccessTypes | str] = Field(alias="accessTypes", default=None,)
	applicability: Optional[Union[DeviceManagementConfigurationApplicationSettingApplicability, DeviceManagementConfigurationExchangeOnlineSettingApplicability, DeviceManagementConfigurationWindowsSettingApplicability]] = Field(alias="applicability", default=None,discriminator="odata_type", )
	baseUri: Optional[str] = Field(alias="baseUri", default=None,)
	categoryId: Optional[str] = Field(alias="categoryId", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	helpText: Optional[str] = Field(alias="helpText", default=None,)
	infoUrls: Optional[list[str]] = Field(alias="infoUrls", default=None,)
	keywords: Optional[list[str]] = Field(alias="keywords", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	occurrence: Optional[DeviceManagementConfigurationSettingOccurrence] = Field(alias="occurrence", default=None,)
	offsetUri: Optional[str] = Field(alias="offsetUri", default=None,)
	referredSettingInformationList: Optional[list[DeviceManagementConfigurationReferredSettingInformation]] = Field(alias="referredSettingInformationList", default=None,)
	riskLevel: Optional[DeviceManagementConfigurationSettingRiskLevel | str] = Field(alias="riskLevel", default=None,)
	rootDefinitionId: Optional[str] = Field(alias="rootDefinitionId", default=None,)
	settingUsage: Optional[DeviceManagementConfigurationSettingUsage | str] = Field(alias="settingUsage", default=None,)
	uxBehavior: Optional[DeviceManagementConfigurationControlType | str] = Field(alias="uxBehavior", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	visibility: Optional[DeviceManagementConfigurationSettingVisibility | str] = Field(alias="visibility", default=None,)
	defaultValue: Optional[Union[DeviceManagementConfigurationChoiceSettingValue, DeviceManagementConfigurationGroupSettingValue, DeviceManagementConfigurationIntegerSettingValue, DeviceManagementConfigurationSecretSettingValue, DeviceManagementConfigurationReferenceSettingValue]] = Field(alias="defaultValue", default=None,discriminator="odata_type", )
	dependedOnBy: Optional[list[DeviceManagementConfigurationSettingDependedOnBy]] = Field(alias="dependedOnBy", default=None,)
	dependentOn: Optional[list[DeviceManagementConfigurationDependentOn]] = Field(alias="dependentOn", default=None,)
	valueDefinition: Optional[Union[DeviceManagementConfigurationIntegerSettingValueDefinition, DeviceManagementConfigurationStringSettingValueDefinition]] = Field(alias="valueDefinition", default=None,discriminator="odata_type", )

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
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionDefinition":
				from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
				return DeviceManagementConfigurationSimpleSettingCollectionDefinition.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_management_configuration_setting_access_types import DeviceManagementConfigurationSettingAccessTypes
from .device_management_configuration_application_setting_applicability import DeviceManagementConfigurationApplicationSettingApplicability
from .device_management_configuration_exchange_online_setting_applicability import DeviceManagementConfigurationExchangeOnlineSettingApplicability
from .device_management_configuration_windows_setting_applicability import DeviceManagementConfigurationWindowsSettingApplicability
from .device_management_configuration_setting_occurrence import DeviceManagementConfigurationSettingOccurrence
from .device_management_configuration_referred_setting_information import DeviceManagementConfigurationReferredSettingInformation
from .device_management_configuration_setting_risk_level import DeviceManagementConfigurationSettingRiskLevel
from .device_management_configuration_setting_usage import DeviceManagementConfigurationSettingUsage
from .device_management_configuration_control_type import DeviceManagementConfigurationControlType
from .device_management_configuration_setting_visibility import DeviceManagementConfigurationSettingVisibility
from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue
from .device_management_configuration_integer_setting_value import DeviceManagementConfigurationIntegerSettingValue
from .device_management_configuration_secret_setting_value import DeviceManagementConfigurationSecretSettingValue
from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
from .device_management_configuration_integer_setting_value_definition import DeviceManagementConfigurationIntegerSettingValueDefinition
from .device_management_configuration_string_setting_value_definition import DeviceManagementConfigurationStringSettingValueDefinition
