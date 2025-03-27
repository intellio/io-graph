from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TeamTemplateDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	audience: Optional[TeamTemplateAudience | str] = Field(alias="audience", default=None,)
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	iconUrl: Optional[str] = Field(alias="iconUrl", default=None,)
	languageTag: Optional[str] = Field(alias="languageTag", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	parentTemplateId: Optional[str] = Field(alias="parentTemplateId", default=None,)
	publisherName: Optional[str] = Field(alias="publisherName", default=None,)
	shortDescription: Optional[str] = Field(alias="shortDescription", default=None,)
	teamDefinition: Optional[Team] = Field(alias="teamDefinition", default=None,)

from .team_template_audience import TeamTemplateAudience
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .team import Team

