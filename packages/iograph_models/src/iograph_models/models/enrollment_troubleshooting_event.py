from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EnrollmentTroubleshootingEvent(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	correlationId: Optional[str] = Field(default=None,alias="correlationId",)
	eventDateTime: Optional[datetime] = Field(default=None,alias="eventDateTime",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	enrollmentType: Optional[DeviceEnrollmentType] = Field(default=None,alias="enrollmentType",)
	failureCategory: Optional[DeviceEnrollmentFailureReason] = Field(default=None,alias="failureCategory",)
	failureReason: Optional[str] = Field(default=None,alias="failureReason",)
	managedDeviceIdentifier: Optional[str] = Field(default=None,alias="managedDeviceIdentifier",)
	operatingSystem: Optional[str] = Field(default=None,alias="operatingSystem",)
	osVersion: Optional[str] = Field(default=None,alias="osVersion",)
	userId: Optional[str] = Field(default=None,alias="userId",)

from .device_enrollment_type import DeviceEnrollmentType
from .device_enrollment_failure_reason import DeviceEnrollmentFailureReason

