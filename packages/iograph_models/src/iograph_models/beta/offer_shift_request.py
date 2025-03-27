from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OfferShiftRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.offerShiftRequest"] = Field(alias="@odata.type", default="#microsoft.graph.offerShiftRequest")
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	assignedTo: Optional[ScheduleChangeRequestActor | str] = Field(alias="assignedTo", default=None,)
	managerActionDateTime: Optional[datetime] = Field(alias="managerActionDateTime", default=None,)
	managerActionMessage: Optional[str] = Field(alias="managerActionMessage", default=None,)
	managerUserId: Optional[str] = Field(alias="managerUserId", default=None,)
	senderDateTime: Optional[datetime] = Field(alias="senderDateTime", default=None,)
	senderMessage: Optional[str] = Field(alias="senderMessage", default=None,)
	senderUserId: Optional[str] = Field(alias="senderUserId", default=None,)
	state: Optional[ScheduleChangeState | str] = Field(alias="state", default=None,)
	recipientActionDateTime: Optional[datetime] = Field(alias="recipientActionDateTime", default=None,)
	recipientActionMessage: Optional[str] = Field(alias="recipientActionMessage", default=None,)
	recipientUserId: Optional[str] = Field(alias="recipientUserId", default=None,)
	senderShiftId: Optional[str] = Field(alias="senderShiftId", default=None,)

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
			if mapping_key == "#microsoft.graph.swapShiftsChangeRequest":
				from .swap_shifts_change_request import SwapShiftsChangeRequest
				return SwapShiftsChangeRequest.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .schedule_change_request_actor import ScheduleChangeRequestActor
from .schedule_change_state import ScheduleChangeState

