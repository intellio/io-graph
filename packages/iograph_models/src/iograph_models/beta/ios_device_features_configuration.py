from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosDeviceFeaturesConfiguration(BaseModel):
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
	airPrintDestinations: Optional[list[AirPrintDestination]] = Field(alias="airPrintDestinations",default=None,)
	assetTagTemplate: Optional[str] = Field(alias="assetTagTemplate",default=None,)
	contentFilterSettings: SerializeAsAny[Optional[IosWebContentFilterBase]] = Field(alias="contentFilterSettings",default=None,)
	homeScreenDockIcons: SerializeAsAny[Optional[list[IosHomeScreenItem]]] = Field(alias="homeScreenDockIcons",default=None,)
	homeScreenGridHeight: Optional[int] = Field(alias="homeScreenGridHeight",default=None,)
	homeScreenGridWidth: Optional[int] = Field(alias="homeScreenGridWidth",default=None,)
	homeScreenPages: Optional[list[IosHomeScreenPage]] = Field(alias="homeScreenPages",default=None,)
	iosSingleSignOnExtension: SerializeAsAny[Optional[IosSingleSignOnExtension]] = Field(alias="iosSingleSignOnExtension",default=None,)
	lockScreenFootnote: Optional[str] = Field(alias="lockScreenFootnote",default=None,)
	notificationSettings: Optional[list[IosNotificationSettings]] = Field(alias="notificationSettings",default=None,)
	singleSignOnExtension: SerializeAsAny[Optional[SingleSignOnExtension]] = Field(alias="singleSignOnExtension",default=None,)
	singleSignOnSettings: Optional[IosSingleSignOnSettings] = Field(alias="singleSignOnSettings",default=None,)
	wallpaperDisplayLocation: Optional[IosWallpaperDisplayLocation | str] = Field(alias="wallpaperDisplayLocation",default=None,)
	wallpaperImage: Optional[MimeContent] = Field(alias="wallpaperImage",default=None,)
	identityCertificateForClientAuthentication: SerializeAsAny[Optional[IosCertificateProfileBase]] = Field(alias="identityCertificateForClientAuthentication",default=None,)
	singleSignOnExtensionPkinitCertificate: SerializeAsAny[Optional[IosCertificateProfileBase]] = Field(alias="singleSignOnExtensionPkinitCertificate",default=None,)

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
from .air_print_destination import AirPrintDestination
from .ios_web_content_filter_base import IosWebContentFilterBase
from .ios_home_screen_item import IosHomeScreenItem
from .ios_home_screen_page import IosHomeScreenPage
from .ios_single_sign_on_extension import IosSingleSignOnExtension
from .ios_notification_settings import IosNotificationSettings
from .single_sign_on_extension import SingleSignOnExtension
from .ios_single_sign_on_settings import IosSingleSignOnSettings
from .ios_wallpaper_display_location import IosWallpaperDisplayLocation
from .mime_content import MimeContent
from .ios_certificate_profile_base import IosCertificateProfileBase
from .ios_certificate_profile_base import IosCertificateProfileBase

