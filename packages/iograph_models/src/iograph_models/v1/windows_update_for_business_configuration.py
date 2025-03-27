from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdateForBusinessConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdateForBusinessConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdateForBusinessConfiguration")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments", default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries", default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses", default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview", default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses", default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview", default=None,)
	allowWindows11Upgrade: Optional[bool] = Field(alias="allowWindows11Upgrade", default=None,)
	automaticUpdateMode: Optional[AutomaticUpdateMode | str] = Field(alias="automaticUpdateMode", default=None,)
	autoRestartNotificationDismissal: Optional[AutoRestartNotificationDismissalMethod | str] = Field(alias="autoRestartNotificationDismissal", default=None,)
	businessReadyUpdatesOnly: Optional[WindowsUpdateType | str] = Field(alias="businessReadyUpdatesOnly", default=None,)
	deadlineForFeatureUpdatesInDays: Optional[int] = Field(alias="deadlineForFeatureUpdatesInDays", default=None,)
	deadlineForQualityUpdatesInDays: Optional[int] = Field(alias="deadlineForQualityUpdatesInDays", default=None,)
	deadlineGracePeriodInDays: Optional[int] = Field(alias="deadlineGracePeriodInDays", default=None,)
	deliveryOptimizationMode: Optional[WindowsDeliveryOptimizationMode | str] = Field(alias="deliveryOptimizationMode", default=None,)
	driversExcluded: Optional[bool] = Field(alias="driversExcluded", default=None,)
	engagedRestartDeadlineInDays: Optional[int] = Field(alias="engagedRestartDeadlineInDays", default=None,)
	engagedRestartSnoozeScheduleInDays: Optional[int] = Field(alias="engagedRestartSnoozeScheduleInDays", default=None,)
	engagedRestartTransitionScheduleInDays: Optional[int] = Field(alias="engagedRestartTransitionScheduleInDays", default=None,)
	featureUpdatesDeferralPeriodInDays: Optional[int] = Field(alias="featureUpdatesDeferralPeriodInDays", default=None,)
	featureUpdatesPaused: Optional[bool] = Field(alias="featureUpdatesPaused", default=None,)
	featureUpdatesPauseExpiryDateTime: Optional[datetime] = Field(alias="featureUpdatesPauseExpiryDateTime", default=None,)
	featureUpdatesPauseStartDate: Optional[str] = Field(alias="featureUpdatesPauseStartDate", default=None,)
	featureUpdatesRollbackStartDateTime: Optional[datetime] = Field(alias="featureUpdatesRollbackStartDateTime", default=None,)
	featureUpdatesRollbackWindowInDays: Optional[int] = Field(alias="featureUpdatesRollbackWindowInDays", default=None,)
	featureUpdatesWillBeRolledBack: Optional[bool] = Field(alias="featureUpdatesWillBeRolledBack", default=None,)
	installationSchedule: Optional[Union[WindowsUpdateActiveHoursInstall, WindowsUpdateScheduledInstall]] = Field(alias="installationSchedule", default=None,discriminator="odata_type", )
	microsoftUpdateServiceAllowed: Optional[bool] = Field(alias="microsoftUpdateServiceAllowed", default=None,)
	postponeRebootUntilAfterDeadline: Optional[bool] = Field(alias="postponeRebootUntilAfterDeadline", default=None,)
	prereleaseFeatures: Optional[PrereleaseFeatures | str] = Field(alias="prereleaseFeatures", default=None,)
	qualityUpdatesDeferralPeriodInDays: Optional[int] = Field(alias="qualityUpdatesDeferralPeriodInDays", default=None,)
	qualityUpdatesPaused: Optional[bool] = Field(alias="qualityUpdatesPaused", default=None,)
	qualityUpdatesPauseExpiryDateTime: Optional[datetime] = Field(alias="qualityUpdatesPauseExpiryDateTime", default=None,)
	qualityUpdatesPauseStartDate: Optional[str] = Field(alias="qualityUpdatesPauseStartDate", default=None,)
	qualityUpdatesRollbackStartDateTime: Optional[datetime] = Field(alias="qualityUpdatesRollbackStartDateTime", default=None,)
	qualityUpdatesWillBeRolledBack: Optional[bool] = Field(alias="qualityUpdatesWillBeRolledBack", default=None,)
	scheduleImminentRestartWarningInMinutes: Optional[int] = Field(alias="scheduleImminentRestartWarningInMinutes", default=None,)
	scheduleRestartWarningInHours: Optional[int] = Field(alias="scheduleRestartWarningInHours", default=None,)
	skipChecksBeforeRestart: Optional[bool] = Field(alias="skipChecksBeforeRestart", default=None,)
	updateNotificationLevel: Optional[WindowsUpdateNotificationDisplayOption | str] = Field(alias="updateNotificationLevel", default=None,)
	updateWeeks: Optional[WindowsUpdateForBusinessUpdateWeeks | str] = Field(alias="updateWeeks", default=None,)
	userPauseAccess: Optional[Enablement | str] = Field(alias="userPauseAccess", default=None,)
	userWindowsUpdateScanAccess: Optional[Enablement | str] = Field(alias="userWindowsUpdateScanAccess", default=None,)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .automatic_update_mode import AutomaticUpdateMode
from .auto_restart_notification_dismissal_method import AutoRestartNotificationDismissalMethod
from .windows_update_type import WindowsUpdateType
from .windows_delivery_optimization_mode import WindowsDeliveryOptimizationMode
from .windows_update_active_hours_install import WindowsUpdateActiveHoursInstall
from .windows_update_scheduled_install import WindowsUpdateScheduledInstall
from .prerelease_features import PrereleaseFeatures
from .windows_update_notification_display_option import WindowsUpdateNotificationDisplayOption
from .windows_update_for_business_update_weeks import WindowsUpdateForBusinessUpdateWeeks
from .enablement import Enablement
from .enablement import Enablement

