from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAppDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	authorization: Optional[TeamsAppAuthorization] = Field(alias="authorization", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	publishingState: Optional[TeamsAppPublishingState | str] = Field(alias="publishingState", default=None,)
	shortDescription: Optional[str] = Field(alias="shortDescription", default=None,)
	teamsAppId: Optional[str] = Field(alias="teamsAppId", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	bot: Optional[TeamworkBot] = Field(alias="bot", default=None,)

from .teams_app_authorization import TeamsAppAuthorization
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .teams_app_publishing_state import TeamsAppPublishingState
from .teamwork_bot import TeamworkBot

