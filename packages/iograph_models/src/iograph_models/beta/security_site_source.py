from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecuritySiteSource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.siteSource"] = Field(alias="@odata.type", default="#microsoft.graph.security.siteSource")
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	holdStatus: Optional[SecurityDataSourceHoldStatus | str] = Field(alias="holdStatus", default=None,)
	site: Optional[Site] = Field(alias="site", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .security_data_source_hold_status import SecurityDataSourceHoldStatus
from .site import Site
