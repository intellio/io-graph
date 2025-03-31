from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class ParticipantInfo(BaseModel):
	countryCode: Optional[str] = Field(alias="countryCode", default=None,)
	endpointType: Optional[EndpointType | str] = Field(alias="endpointType", default=None,)
	identity: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="identity", default=None,discriminator="odata_type", )
	languageId: Optional[str] = Field(alias="languageId", default=None,)
	nonAnonymizedIdentity: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="nonAnonymizedIdentity", default=None,discriminator="odata_type", )
	participantId: Optional[str] = Field(alias="participantId", default=None,)
	platformId: Optional[str] = Field(alias="platformId", default=None,)
	region: Optional[str] = Field(alias="region", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .endpoint_type import EndpointType
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
