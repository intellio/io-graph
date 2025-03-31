from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceEnrollmentPlatformRestrictionsConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[EnrollmentConfigurationAssignment]] = Field(alias="assignments", default=None,)
	androidRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="androidRestriction", default=None,)
	iosRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="iosRestriction", default=None,)
	macOSRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="macOSRestriction", default=None,)
	windowsMobileRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="windowsMobileRestriction", default=None,)
	windowsRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="windowsRestriction", default=None,)

from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
