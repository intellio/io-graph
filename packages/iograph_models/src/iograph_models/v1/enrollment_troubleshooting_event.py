from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EnrollmentTroubleshootingEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	correlationId: Optional[str] = Field(alias="correlationId", default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	enrollmentType: Optional[DeviceEnrollmentType | str] = Field(alias="enrollmentType", default=None,)
	failureCategory: Optional[DeviceEnrollmentFailureReason | str] = Field(alias="failureCategory", default=None,)
	failureReason: Optional[str] = Field(alias="failureReason", default=None,)
	managedDeviceIdentifier: Optional[str] = Field(alias="managedDeviceIdentifier", default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)

from .device_enrollment_type import DeviceEnrollmentType
from .device_enrollment_failure_reason import DeviceEnrollmentFailureReason

