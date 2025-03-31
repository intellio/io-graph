from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field


class CopyNotebookModel(BaseModel):
	createdBy: Optional[str] = Field(alias="createdBy", default=None,)
	createdByIdentity: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdByIdentity", default=None,discriminator="odata_type", )
	createdTime: Optional[datetime] = Field(alias="createdTime", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	isShared: Optional[bool] = Field(alias="isShared", default=None,)
	lastModifiedBy: Optional[str] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedByIdentity: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedByIdentity", default=None,discriminator="odata_type", )
	lastModifiedTime: Optional[datetime] = Field(alias="lastModifiedTime", default=None,)
	links: Optional[NotebookLinks] = Field(alias="links", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	sectionGroupsUrl: Optional[str] = Field(alias="sectionGroupsUrl", default=None,)
	sectionsUrl: Optional[str] = Field(alias="sectionsUrl", default=None,)
	self: Optional[str] = Field(alias="self", default=None,)
	userRole: Optional[OnenoteUserRole | str] = Field(alias="userRole", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .notebook_links import NotebookLinks
from .onenote_user_role import OnenoteUserRole
