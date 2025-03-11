from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_enrollment_notification_configurationPostRequest(BaseModel):
	deviceEnrollmentNotificationConfigurations: SerializeAsAny[Optional[list[DeviceEnrollmentConfiguration]]] = Field(alias="deviceEnrollmentNotificationConfigurations",default=None,)

from .device_enrollment_configuration import DeviceEnrollmentConfiguration

