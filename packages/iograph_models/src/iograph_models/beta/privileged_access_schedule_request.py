from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessScheduleRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.privilegedAccessScheduleRequest"] = Field(alias="@odata.type", default="#microsoft.graph.privilegedAccessScheduleRequest")
	approvalId: Optional[str] = Field(alias="approvalId", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	customData: Optional[str] = Field(alias="customData", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	action: Optional[ScheduleRequestActions | str] = Field(alias="action", default=None,)
	isValidationOnly: Optional[bool] = Field(alias="isValidationOnly", default=None,)
	justification: Optional[str] = Field(alias="justification", default=None,)
	scheduleInfo: Optional[RequestSchedule] = Field(alias="scheduleInfo", default=None,)
	ticketInfo: Optional[TicketInfo] = Field(alias="ticketInfo", default=None,)

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
			if mapping_key == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest":
				from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
				return PrivilegedAccessGroupAssignmentScheduleRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest":
				from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
				return PrivilegedAccessGroupEligibilityScheduleRequest.model_validate(data)
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
from .schedule_request_actions import ScheduleRequestActions
from .request_schedule import RequestSchedule
from .ticket_info import TicketInfo

