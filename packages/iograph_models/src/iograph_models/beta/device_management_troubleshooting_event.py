from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DeviceManagementTroubleshootingEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	additionalInformation: Optional[list[KeyValuePair]] = Field(alias="additionalInformation", default=None,)
	correlationId: Optional[str] = Field(alias="correlationId", default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	eventName: Optional[str] = Field(alias="eventName", default=None,)
	troubleshootingErrorDetails: Optional[DeviceManagementTroubleshootingErrorDetails] = Field(alias="troubleshootingErrorDetails", default=None,)

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
			if mapping_key == "#microsoft.graph.appleVppTokenTroubleshootingEvent":
				from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent
				return AppleVppTokenTroubleshootingEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.enrollmentTroubleshootingEvent":
				from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
				return EnrollmentTroubleshootingEvent.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppTroubleshootingEvent":
				from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
				return MobileAppTroubleshootingEvent.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .key_value_pair import KeyValuePair
from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
