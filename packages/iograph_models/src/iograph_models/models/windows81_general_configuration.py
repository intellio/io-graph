from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows81GeneralConfiguration(BaseModel):
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
	accountsBlockAddingNonMicrosoftAccountEmail: Optional[bool] = Field(default=None,alias="accountsBlockAddingNonMicrosoftAccountEmail",)
	applyOnlyToWindows81: Optional[bool] = Field(default=None,alias="applyOnlyToWindows81",)
	browserBlockAutofill: Optional[bool] = Field(default=None,alias="browserBlockAutofill",)
	browserBlockAutomaticDetectionOfIntranetSites: Optional[bool] = Field(default=None,alias="browserBlockAutomaticDetectionOfIntranetSites",)
	browserBlockEnterpriseModeAccess: Optional[bool] = Field(default=None,alias="browserBlockEnterpriseModeAccess",)
	browserBlockJavaScript: Optional[bool] = Field(default=None,alias="browserBlockJavaScript",)
	browserBlockPlugins: Optional[bool] = Field(default=None,alias="browserBlockPlugins",)
	browserBlockPopups: Optional[bool] = Field(default=None,alias="browserBlockPopups",)
	browserBlockSendingDoNotTrackHeader: Optional[bool] = Field(default=None,alias="browserBlockSendingDoNotTrackHeader",)
	browserBlockSingleWordEntryOnIntranetSites: Optional[bool] = Field(default=None,alias="browserBlockSingleWordEntryOnIntranetSites",)
	browserEnterpriseModeSiteListLocation: Optional[str] = Field(default=None,alias="browserEnterpriseModeSiteListLocation",)
	browserInternetSecurityLevel: Optional[InternetSiteSecurityLevel] = Field(default=None,alias="browserInternetSecurityLevel",)
	browserIntranetSecurityLevel: Optional[SiteSecurityLevel] = Field(default=None,alias="browserIntranetSecurityLevel",)
	browserLoggingReportLocation: Optional[str] = Field(default=None,alias="browserLoggingReportLocation",)
	browserRequireFirewall: Optional[bool] = Field(default=None,alias="browserRequireFirewall",)
	browserRequireFraudWarning: Optional[bool] = Field(default=None,alias="browserRequireFraudWarning",)
	browserRequireHighSecurityForRestrictedSites: Optional[bool] = Field(default=None,alias="browserRequireHighSecurityForRestrictedSites",)
	browserRequireSmartScreen: Optional[bool] = Field(default=None,alias="browserRequireSmartScreen",)
	browserTrustedSitesSecurityLevel: Optional[SiteSecurityLevel] = Field(default=None,alias="browserTrustedSitesSecurityLevel",)
	cellularBlockDataRoaming: Optional[bool] = Field(default=None,alias="cellularBlockDataRoaming",)
	diagnosticsBlockDataSubmission: Optional[bool] = Field(default=None,alias="diagnosticsBlockDataSubmission",)
	passwordBlockPicturePasswordAndPin: Optional[bool] = Field(default=None,alias="passwordBlockPicturePasswordAndPin",)
	passwordExpirationDays: Optional[int] = Field(default=None,alias="passwordExpirationDays",)
	passwordMinimumCharacterSetCount: Optional[int] = Field(default=None,alias="passwordMinimumCharacterSetCount",)
	passwordMinimumLength: Optional[int] = Field(default=None,alias="passwordMinimumLength",)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(default=None,alias="passwordMinutesOfInactivityBeforeScreenTimeout",)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(default=None,alias="passwordPreviousPasswordBlockCount",)
	passwordRequiredType: Optional[RequiredPasswordType] = Field(default=None,alias="passwordRequiredType",)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(default=None,alias="passwordSignInFailureCountBeforeFactoryReset",)
	storageRequireDeviceEncryption: Optional[bool] = Field(default=None,alias="storageRequireDeviceEncryption",)
	updatesRequireAutomaticUpdates: Optional[bool] = Field(default=None,alias="updatesRequireAutomaticUpdates",)
	userAccountControlSettings: Optional[WindowsUserAccountControlSettings] = Field(default=None,alias="userAccountControlSettings",)
	workFoldersUrl: Optional[str] = Field(default=None,alias="workFoldersUrl",)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .internet_site_security_level import InternetSiteSecurityLevel
from .site_security_level import SiteSecurityLevel
from .site_security_level import SiteSecurityLevel
from .required_password_type import RequiredPasswordType
from .windows_user_account_control_settings import WindowsUserAccountControlSettings

