from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DeviceEnrollmentConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[EnrollmentConfigurationAssignment]] = Field(alias="assignments", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.deviceEnrollmentLimitConfiguration":
				from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
				return DeviceEnrollmentLimitConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration":
				from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
				return DeviceEnrollmentPlatformRestrictionsConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration":
				from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
				return DeviceEnrollmentWindowsHelloForBusinessConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EnrollmentCompletionPageConfiguration":
				from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
				return Windows10EnrollmentCompletionPageConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
