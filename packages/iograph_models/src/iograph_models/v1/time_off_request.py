from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TimeOffRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.timeOffRequest"] = Field(alias="@odata.type", default="#microsoft.graph.timeOffRequest")
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	assignedTo: Optional[ScheduleChangeRequestActor | str] = Field(alias="assignedTo", default=None,)
	managerActionDateTime: Optional[datetime] = Field(alias="managerActionDateTime", default=None,)
	managerActionMessage: Optional[str] = Field(alias="managerActionMessage", default=None,)
	managerUserId: Optional[str] = Field(alias="managerUserId", default=None,)
	senderDateTime: Optional[datetime] = Field(alias="senderDateTime", default=None,)
	senderMessage: Optional[str] = Field(alias="senderMessage", default=None,)
	senderUserId: Optional[str] = Field(alias="senderUserId", default=None,)
	state: Optional[ScheduleChangeState | str] = Field(alias="state", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	timeOffReasonId: Optional[str] = Field(alias="timeOffReasonId", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .schedule_change_request_actor import ScheduleChangeRequestActor
from .schedule_change_state import ScheduleChangeState
