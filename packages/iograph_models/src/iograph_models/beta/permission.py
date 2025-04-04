from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class Permission(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.permission"] = Field(alias="@odata.type", default="#microsoft.graph.permission")
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	grantedTo: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="grantedTo", default=None,discriminator="odata_type", )
	grantedToIdentities: Optional[list[Annotated[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet],Field(discriminator="odata_type")]]] = Field(alias="grantedToIdentities", default=None,)
	grantedToIdentitiesV2: Optional[list[SharePointIdentitySet]] = Field(alias="grantedToIdentitiesV2", default=None,)
	grantedToV2: Optional[SharePointIdentitySet] = Field(alias="grantedToV2", default=None,)
	hasPassword: Optional[bool] = Field(alias="hasPassword", default=None,)
	inheritedFrom: Optional[ItemReference] = Field(alias="inheritedFrom", default=None,)
	invitation: Optional[SharingInvitation] = Field(alias="invitation", default=None,)
	link: Optional[SharingLink] = Field(alias="link", default=None,)
	roles: Optional[list[str]] = Field(alias="roles", default=None,)
	shareId: Optional[str] = Field(alias="shareId", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .item_reference import ItemReference
from .sharing_invitation import SharingInvitation
from .sharing_link import SharingLink
