from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EdiscoveryLegalHold(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.ediscovery.legalHold"] = Field(alias="@odata.type",)
	contentQuery: Optional[str] = Field(alias="contentQuery", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	errors: Optional[list[str]] = Field(alias="errors", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	status: Optional[EdiscoveryLegalHoldStatus | str] = Field(alias="status", default=None,)
	siteSources: Optional[list[EdiscoverySiteSource]] = Field(alias="siteSources", default=None,)
	unifiedGroupSources: Optional[list[EdiscoveryUnifiedGroupSource]] = Field(alias="unifiedGroupSources", default=None,)
	userSources: Optional[list[EdiscoveryUserSource]] = Field(alias="userSources", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .ediscovery_legal_hold_status import EdiscoveryLegalHoldStatus
from .ediscovery_site_source import EdiscoverySiteSource
from .ediscovery_unified_group_source import EdiscoveryUnifiedGroupSource
from .ediscovery_user_source import EdiscoveryUserSource
