from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationRedirectSettingDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accessTypes: Optional[DeviceManagementConfigurationSettingAccessTypes | str] = Field(alias="accessTypes",default=None,)
	applicability: SerializeAsAny[Optional[DeviceManagementConfigurationSettingApplicability]] = Field(alias="applicability",default=None,)
	baseUri: Optional[str] = Field(alias="baseUri",default=None,)
	categoryId: Optional[str] = Field(alias="categoryId",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	helpText: Optional[str] = Field(alias="helpText",default=None,)
	infoUrls: Optional[list[str]] = Field(alias="infoUrls",default=None,)
	keywords: Optional[list[str]] = Field(alias="keywords",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	occurrence: Optional[DeviceManagementConfigurationSettingOccurrence] = Field(alias="occurrence",default=None,)
	offsetUri: Optional[str] = Field(alias="offsetUri",default=None,)
	referredSettingInformationList: Optional[list[DeviceManagementConfigurationReferredSettingInformation]] = Field(alias="referredSettingInformationList",default=None,)
	riskLevel: Optional[DeviceManagementConfigurationSettingRiskLevel | str] = Field(alias="riskLevel",default=None,)
	rootDefinitionId: Optional[str] = Field(alias="rootDefinitionId",default=None,)
	settingUsage: Optional[DeviceManagementConfigurationSettingUsage | str] = Field(alias="settingUsage",default=None,)
	uxBehavior: Optional[DeviceManagementConfigurationControlType | str] = Field(alias="uxBehavior",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	visibility: Optional[DeviceManagementConfigurationSettingVisibility | str] = Field(alias="visibility",default=None,)
	deepLink: Optional[str] = Field(alias="deepLink",default=None,)
	redirectMessage: Optional[str] = Field(alias="redirectMessage",default=None,)
	redirectReason: Optional[str] = Field(alias="redirectReason",default=None,)

from .device_management_configuration_setting_access_types import DeviceManagementConfigurationSettingAccessTypes
from .device_management_configuration_setting_applicability import DeviceManagementConfigurationSettingApplicability
from .device_management_configuration_setting_occurrence import DeviceManagementConfigurationSettingOccurrence
from .device_management_configuration_referred_setting_information import DeviceManagementConfigurationReferredSettingInformation
from .device_management_configuration_setting_risk_level import DeviceManagementConfigurationSettingRiskLevel
from .device_management_configuration_setting_usage import DeviceManagementConfigurationSettingUsage
from .device_management_configuration_control_type import DeviceManagementConfigurationControlType
from .device_management_configuration_setting_visibility import DeviceManagementConfigurationSettingVisibility

