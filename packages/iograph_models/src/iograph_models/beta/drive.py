from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Drive(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.drive"] = Field(alias="@odata.type", default="#microsoft.graph.drive")
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	eTag: Optional[str] = Field(alias="eTag", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	parentReference: Optional[ItemReference] = Field(alias="parentReference", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	createdByUser: Optional[User] = Field(alias="createdByUser", default=None,)
	lastModifiedByUser: Optional[User] = Field(alias="lastModifiedByUser", default=None,)
	driveType: Optional[str] = Field(alias="driveType", default=None,)
	owner: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="owner", default=None,discriminator="odata_type", )
	quota: Optional[Quota] = Field(alias="quota", default=None,)
	sharePointIds: Optional[SharepointIds] = Field(alias="sharePointIds", default=None,)
	system: Optional[SystemFacet] = Field(alias="system", default=None,)
	activities: Optional[list[ItemActivityOLD]] = Field(alias="activities", default=None,)
	bundles: Optional[list[DriveItem]] = Field(alias="bundles", default=None,)
	following: Optional[list[DriveItem]] = Field(alias="following", default=None,)
	items: Optional[list[DriveItem]] = Field(alias="items", default=None,)
	list: Optional[List] = Field(alias="list", default=None,)
	root: Optional[DriveItem] = Field(alias="root", default=None,)
	special: Optional[list[DriveItem]] = Field(alias="special", default=None,)

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
from .item_reference import ItemReference
from .user import User
from .user import User
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .quota import Quota
from .sharepoint_ids import SharepointIds
from .system_facet import SystemFacet
from .item_activity_o_l_d import ItemActivityOLD
from .drive_item import DriveItem
from .drive_item import DriveItem
from .drive_item import DriveItem
from .list import List
from .drive_item import DriveItem
from .drive_item import DriveItem

