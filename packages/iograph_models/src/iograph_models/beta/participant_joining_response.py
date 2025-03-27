from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class ParticipantJoiningResponse(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.acceptJoinResponse":
				from .accept_join_response import AcceptJoinResponse
				return AcceptJoinResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.inviteNewBotResponse":
				from .invite_new_bot_response import InviteNewBotResponse
				return InviteNewBotResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.rejectJoinResponse":
				from .reject_join_response import RejectJoinResponse
				return RejectJoinResponse.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


