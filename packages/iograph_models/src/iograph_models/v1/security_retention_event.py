from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityRetentionEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.retentionEvent"] = Field(alias="@odata.type",)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	eventPropagationResults: Optional[list[SecurityEventPropagationResult]] = Field(alias="eventPropagationResults", default=None,)
	eventQueries: Optional[list[SecurityEventQuery]] = Field(alias="eventQueries", default=None,)
	eventStatus: Optional[SecurityRetentionEventStatus] = Field(alias="eventStatus", default=None,)
	eventTriggerDateTime: Optional[datetime] = Field(alias="eventTriggerDateTime", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	lastStatusUpdateDateTime: Optional[datetime] = Field(alias="lastStatusUpdateDateTime", default=None,)
	retentionEventType: Optional[SecurityRetentionEventType] = Field(alias="retentionEventType", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .security_event_propagation_result import SecurityEventPropagationResult
from .security_event_query import SecurityEventQuery
from .security_retention_event_status import SecurityRetentionEventStatus
from .security_retention_event_type import SecurityRetentionEventType
