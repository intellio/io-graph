from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceEnrollmentPlatformRestrictionsConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	deviceEnrollmentConfigurationType: Optional[DeviceEnrollmentConfigurationType | str] = Field(alias="deviceEnrollmentConfigurationType",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[EnrollmentConfigurationAssignment]] = Field(alias="assignments",default=None,)
	androidForWorkRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="androidForWorkRestriction",default=None,)
	androidRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="androidRestriction",default=None,)
	iosRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="iosRestriction",default=None,)
	macOSRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="macOSRestriction",default=None,)
	macRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="macRestriction",default=None,)
	tvosRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="tvosRestriction",default=None,)
	visionOSRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="visionOSRestriction",default=None,)
	windowsHomeSkuRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="windowsHomeSkuRestriction",default=None,)
	windowsMobileRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="windowsMobileRestriction",default=None,)
	windowsRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="windowsRestriction",default=None,)

from .device_enrollment_configuration_type import DeviceEnrollmentConfigurationType
from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction

