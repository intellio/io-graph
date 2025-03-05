from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class CallOptions(BaseModel):
	hideBotAfterEscalation: Optional[bool] = Field(default=None,alias="hideBotAfterEscalation",)
	isContentSharingNotificationEnabled: Optional[bool] = Field(default=None,alias="isContentSharingNotificationEnabled",)
	isDeltaRosterEnabled: Optional[bool] = Field(default=None,alias="isDeltaRosterEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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
			if mapping_key == "#microsoft.graph.incomingCallOptions":
				from .incoming_call_options import IncomingCallOptions
				return IncomingCallOptions.model_validate(data)
			if mapping_key == "#microsoft.graph.outgoingCallOptions":
				from .outgoing_call_options import OutgoingCallOptions
				return OutgoingCallOptions.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


