from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class IdentitySet(BaseModel):
	application: SerializeAsAny[Optional[Identity]] = Field(alias="application",default=None,)
	device: SerializeAsAny[Optional[Identity]] = Field(alias="device",default=None,)
	user: SerializeAsAny[Optional[Identity]] = Field(alias="user",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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
			if mapping_key == "#microsoft.graph.aiInteractionMentionedIdentitySet":
				from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
				return AiInteractionMentionedIdentitySet.model_validate(data)
			if mapping_key == "#microsoft.graph.approvalIdentitySet":
				from .approval_identity_set import ApprovalIdentitySet
				return ApprovalIdentitySet.model_validate(data)
			if mapping_key == "#microsoft.graph.chatMessageFromIdentitySet":
				from .chat_message_from_identity_set import ChatMessageFromIdentitySet
				return ChatMessageFromIdentitySet.model_validate(data)
			if mapping_key == "#microsoft.graph.chatMessageMentionedIdentitySet":
				from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
				return ChatMessageMentionedIdentitySet.model_validate(data)
			if mapping_key == "#microsoft.graph.chatMessageReactionIdentitySet":
				from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
				return ChatMessageReactionIdentitySet.model_validate(data)
			if mapping_key == "#microsoft.graph.communicationsIdentitySet":
				from .communications_identity_set import CommunicationsIdentitySet
				return CommunicationsIdentitySet.model_validate(data)
			if mapping_key == "#microsoft.graph.sharePointIdentitySet":
				from .share_point_identity_set import SharePointIdentitySet
				return SharePointIdentitySet.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity import Identity
from .identity import Identity
from .identity import Identity

