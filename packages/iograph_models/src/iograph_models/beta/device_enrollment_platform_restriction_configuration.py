from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceEnrollmentPlatformRestrictionConfiguration(BaseModel):
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
	platformRestriction: Optional[DeviceEnrollmentPlatformRestriction] = Field(alias="platformRestriction",default=None,)
	platformType: Optional[EnrollmentRestrictionPlatformType | str] = Field(alias="platformType",default=None,)

from .device_enrollment_configuration_type import DeviceEnrollmentConfigurationType
from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
from .device_enrollment_platform_restriction import DeviceEnrollmentPlatformRestriction
from .enrollment_restriction_platform_type import EnrollmentRestrictionPlatformType

