from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SharedDriveItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sharedDriveItem"] = Field(alias="@odata.type", default="#microsoft.graph.sharedDriveItem")
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	eTag: Optional[str] = Field(alias="eTag", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	parentReference: Optional[ItemReference] = Field(alias="parentReference", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	createdByUser: Optional[User] = Field(alias="createdByUser", default=None,)
	lastModifiedByUser: Optional[User] = Field(alias="lastModifiedByUser", default=None,)
	owner: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="owner", default=None,discriminator="odata_type", )
	driveItem: Optional[DriveItem] = Field(alias="driveItem", default=None,)
	items: Optional[list[DriveItem]] = Field(alias="items", default=None,)
	list: Optional[List] = Field(alias="list", default=None,)
	listItem: Optional[ListItem] = Field(alias="listItem", default=None,)
	permission: Optional[Permission] = Field(alias="permission", default=None,)
	root: Optional[DriveItem] = Field(alias="root", default=None,)
	site: Optional[Site] = Field(alias="site", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .item_reference import ItemReference
from .user import User
from .drive_item import DriveItem
from .list import List
from .list_item import ListItem
from .permission import Permission
from .site import Site
