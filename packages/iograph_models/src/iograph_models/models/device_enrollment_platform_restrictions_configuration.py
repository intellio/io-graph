from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceEnrollmentPlatformRestrictionsConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	priority: Optional[int] = Field(default=None,alias="priority",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: list[EnrollmentConfigurationAssignment] = Field(alias="assignments",)
	androidRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(default=None,alias="androidRestriction",)
	iosRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(default=None,alias="iosRestriction",)
	macOSRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(default=None,alias="macOSRestriction",)
	windowsMobileRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(default=None,alias="windowsMobileRestriction",)
	windowsRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(default=None,alias="windowsRestriction",)

from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction

