from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceEnrollmentConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	priority: Optional[int] = Field(default=None,alias="priority",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: list[EnrollmentConfigurationAssignment] = Field(alias="assignments",)

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

