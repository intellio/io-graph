from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkSystemConfiguration(BaseModel):
	dateTimeConfiguration: Optional[TeamworkDateTimeConfiguration] = Field(alias="dateTimeConfiguration", default=None,)
	defaultPassword: Optional[str] = Field(alias="defaultPassword", default=None,)
	deviceLockTimeout: Optional[str] = Field(alias="deviceLockTimeout", default=None,)
	isDeviceLockEnabled: Optional[bool] = Field(alias="isDeviceLockEnabled", default=None,)
	isLoggingEnabled: Optional[bool] = Field(alias="isLoggingEnabled", default=None,)
	isPowerSavingEnabled: Optional[bool] = Field(alias="isPowerSavingEnabled", default=None,)
	isScreenCaptureEnabled: Optional[bool] = Field(alias="isScreenCaptureEnabled", default=None,)
	isSilentModeEnabled: Optional[bool] = Field(alias="isSilentModeEnabled", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	lockPin: Optional[str] = Field(alias="lockPin", default=None,)
	loggingLevel: Optional[str] = Field(alias="loggingLevel", default=None,)
	networkConfiguration: Optional[TeamworkNetworkConfiguration] = Field(alias="networkConfiguration", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teamwork_date_time_configuration import TeamworkDateTimeConfiguration
from .teamwork_network_configuration import TeamworkNetworkConfiguration

