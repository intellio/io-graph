from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MacOSGeneralDeviceConfiguration(BaseModel):
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
	compliantAppListType: Optional[AppListType] = Field(default=None,alias="compliantAppListType",)
	compliantAppsList: list[AppListItem] = Field(alias="compliantAppsList",)
	emailInDomainSuffixes: list[Optional[str]] = Field(alias="emailInDomainSuffixes",)
	passwordBlockSimple: Optional[bool] = Field(default=None,alias="passwordBlockSimple",)
	passwordExpirationDays: Optional[int] = Field(default=None,alias="passwordExpirationDays",)
	passwordMinimumCharacterSetCount: Optional[int] = Field(default=None,alias="passwordMinimumCharacterSetCount",)
	passwordMinimumLength: Optional[int] = Field(default=None,alias="passwordMinimumLength",)
	passwordMinutesOfInactivityBeforeLock: Optional[int] = Field(default=None,alias="passwordMinutesOfInactivityBeforeLock",)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(default=None,alias="passwordMinutesOfInactivityBeforeScreenTimeout",)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(default=None,alias="passwordPreviousPasswordBlockCount",)
	passwordRequired: Optional[bool] = Field(default=None,alias="passwordRequired",)
	passwordRequiredType: Optional[RequiredPasswordType] = Field(default=None,alias="passwordRequiredType",)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .app_list_type import AppListType
from .app_list_item import AppListItem
from .required_password_type import RequiredPasswordType

