from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EnrollmentTroubleshootingEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.enrollmentTroubleshootingEvent"] = Field(alias="@odata.type", default="#microsoft.graph.enrollmentTroubleshootingEvent")
	additionalInformation: Optional[list[KeyValuePair]] = Field(alias="additionalInformation", default=None,)
	correlationId: Optional[str] = Field(alias="correlationId", default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	eventName: Optional[str] = Field(alias="eventName", default=None,)
	troubleshootingErrorDetails: Optional[DeviceManagementTroubleshootingErrorDetails] = Field(alias="troubleshootingErrorDetails", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	enrollmentType: Optional[DeviceEnrollmentType | str] = Field(alias="enrollmentType", default=None,)
	failureCategory: Optional[DeviceEnrollmentFailureReason | str] = Field(alias="failureCategory", default=None,)
	failureReason: Optional[str] = Field(alias="failureReason", default=None,)
	managedDeviceIdentifier: Optional[str] = Field(alias="managedDeviceIdentifier", default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)

from .key_value_pair import KeyValuePair
from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
from .device_enrollment_type import DeviceEnrollmentType
from .device_enrollment_failure_reason import DeviceEnrollmentFailureReason
