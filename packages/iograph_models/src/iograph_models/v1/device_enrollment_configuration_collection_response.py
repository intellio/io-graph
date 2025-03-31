from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class DeviceEnrollmentConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DeviceEnrollmentLimitConfiguration, DeviceEnrollmentPlatformRestrictionsConfiguration, DeviceEnrollmentWindowsHelloForBusinessConfiguration, Windows10EnrollmentCompletionPageConfiguration],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
