from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class TeamworkNotificationRecipient(BaseModel):
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
			if mapping_key == "#microsoft.graph.aadUserNotificationRecipient":
				from .aad_user_notification_recipient import AadUserNotificationRecipient
				return AadUserNotificationRecipient.model_validate(data)
			if mapping_key == "#microsoft.graph.channelMembersNotificationRecipient":
				from .channel_members_notification_recipient import ChannelMembersNotificationRecipient
				return ChannelMembersNotificationRecipient.model_validate(data)
			if mapping_key == "#microsoft.graph.chatMembersNotificationRecipient":
				from .chat_members_notification_recipient import ChatMembersNotificationRecipient
				return ChatMembersNotificationRecipient.model_validate(data)
			if mapping_key == "#microsoft.graph.teamMembersNotificationRecipient":
				from .team_members_notification_recipient import TeamMembersNotificationRecipient
				return TeamMembersNotificationRecipient.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

