from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class MeetingParticipantInfo(BaseModel):
	identity: Optional[IdentitySet] = Field(default=None,alias="identity",)
	role: Optional[OnlineMeetingRole] = Field(default=None,alias="role",)
	upn: Optional[str] = Field(default=None,alias="upn",)
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
			if mapping_key == "#microsoft.graph.virtualEventPresenterInfo":
				from .virtual_event_presenter_info import VirtualEventPresenterInfo
				return VirtualEventPresenterInfo.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet
from .online_meeting_role import OnlineMeetingRole

