from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SectionGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sectionGroup"] = Field(alias="@odata.type", default="#microsoft.graph.sectionGroup")
	self: Optional[str] = Field(alias="self", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	sectionGroupsUrl: Optional[str] = Field(alias="sectionGroupsUrl", default=None,)
	sectionsUrl: Optional[str] = Field(alias="sectionsUrl", default=None,)
	parentNotebook: Optional[Notebook] = Field(alias="parentNotebook", default=None,)
	parentSectionGroup: Optional[SectionGroup] = Field(alias="parentSectionGroup", default=None,)
	sectionGroups: Optional[list[SectionGroup]] = Field(alias="sectionGroups", default=None,)
	sections: Optional[list[OnenoteSection]] = Field(alias="sections", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .notebook import Notebook
from .onenote_section import OnenoteSection
