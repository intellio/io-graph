from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field


class SiteArchivalDetails(BaseModel):
	archivedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="archivedBy", default=None,discriminator="odata_type", )
	archivedDateTime: Optional[datetime] = Field(alias="archivedDateTime", default=None,)
	archiveStatus: Optional[SiteArchiveStatus | str] = Field(alias="archiveStatus", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .site_archive_status import SiteArchiveStatus
