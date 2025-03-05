from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows81GeneralConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments",default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries",default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview",default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview",default=None,)
	accountsBlockAddingNonMicrosoftAccountEmail: Optional[bool] = Field(alias="accountsBlockAddingNonMicrosoftAccountEmail",default=None,)
	applyOnlyToWindows81: Optional[bool] = Field(alias="applyOnlyToWindows81",default=None,)
	browserBlockAutofill: Optional[bool] = Field(alias="browserBlockAutofill",default=None,)
	browserBlockAutomaticDetectionOfIntranetSites: Optional[bool] = Field(alias="browserBlockAutomaticDetectionOfIntranetSites",default=None,)
	browserBlockEnterpriseModeAccess: Optional[bool] = Field(alias="browserBlockEnterpriseModeAccess",default=None,)
	browserBlockJavaScript: Optional[bool] = Field(alias="browserBlockJavaScript",default=None,)
	browserBlockPlugins: Optional[bool] = Field(alias="browserBlockPlugins",default=None,)
	browserBlockPopups: Optional[bool] = Field(alias="browserBlockPopups",default=None,)
	browserBlockSendingDoNotTrackHeader: Optional[bool] = Field(alias="browserBlockSendingDoNotTrackHeader",default=None,)
	browserBlockSingleWordEntryOnIntranetSites: Optional[bool] = Field(alias="browserBlockSingleWordEntryOnIntranetSites",default=None,)
	browserEnterpriseModeSiteListLocation: Optional[str] = Field(alias="browserEnterpriseModeSiteListLocation",default=None,)
	browserInternetSecurityLevel: Optional[str | InternetSiteSecurityLevel] = Field(alias="browserInternetSecurityLevel",default=None,)
	browserIntranetSecurityLevel: Optional[str | SiteSecurityLevel] = Field(alias="browserIntranetSecurityLevel",default=None,)
	browserLoggingReportLocation: Optional[str] = Field(alias="browserLoggingReportLocation",default=None,)
	browserRequireFirewall: Optional[bool] = Field(alias="browserRequireFirewall",default=None,)
	browserRequireFraudWarning: Optional[bool] = Field(alias="browserRequireFraudWarning",default=None,)
	browserRequireHighSecurityForRestrictedSites: Optional[bool] = Field(alias="browserRequireHighSecurityForRestrictedSites",default=None,)
	browserRequireSmartScreen: Optional[bool] = Field(alias="browserRequireSmartScreen",default=None,)
	browserTrustedSitesSecurityLevel: Optional[str | SiteSecurityLevel] = Field(alias="browserTrustedSitesSecurityLevel",default=None,)
	cellularBlockDataRoaming: Optional[bool] = Field(alias="cellularBlockDataRoaming",default=None,)
	diagnosticsBlockDataSubmission: Optional[bool] = Field(alias="diagnosticsBlockDataSubmission",default=None,)
	passwordBlockPicturePasswordAndPin: Optional[bool] = Field(alias="passwordBlockPicturePasswordAndPin",default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays",default=None,)
	passwordMinimumCharacterSetCount: Optional[int] = Field(alias="passwordMinimumCharacterSetCount",default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength",default=None,)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeScreenTimeout",default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount",default=None,)
	passwordRequiredType: Optional[str | RequiredPasswordType] = Field(alias="passwordRequiredType",default=None,)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="passwordSignInFailureCountBeforeFactoryReset",default=None,)
	storageRequireDeviceEncryption: Optional[bool] = Field(alias="storageRequireDeviceEncryption",default=None,)
	updatesRequireAutomaticUpdates: Optional[bool] = Field(alias="updatesRequireAutomaticUpdates",default=None,)
	userAccountControlSettings: Optional[str | WindowsUserAccountControlSettings] = Field(alias="userAccountControlSettings",default=None,)
	workFoldersUrl: Optional[str] = Field(alias="workFoldersUrl",default=None,)

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

