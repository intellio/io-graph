from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RestrictedAppsViolation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	deviceConfigurationId: Optional[str] = Field(alias="deviceConfigurationId", default=None,)
	deviceConfigurationName: Optional[str] = Field(alias="deviceConfigurationName", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	platformType: Optional[PolicyPlatformType | str] = Field(alias="platformType", default=None,)
	restrictedApps: Optional[list[ManagedDeviceReportedApp]] = Field(alias="restrictedApps", default=None,)
	restrictedAppsState: Optional[RestrictedAppsState | str] = Field(alias="restrictedAppsState", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)

from .policy_platform_type import PolicyPlatformType
from .managed_device_reported_app import ManagedDeviceReportedApp
from .restricted_apps_state import RestrictedAppsState

