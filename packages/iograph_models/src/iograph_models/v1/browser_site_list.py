from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class BrowserSiteList(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.browserSiteList"] = Field(alias="@odata.type", default="#microsoft.graph.browserSiteList")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	publishedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="publishedBy", default=None,discriminator="odata_type", )
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime", default=None,)
	revision: Optional[str] = Field(alias="revision", default=None,)
	status: Optional[BrowserSiteListStatus | str] = Field(alias="status", default=None,)
	sharedCookies: Optional[list[BrowserSharedCookie]] = Field(alias="sharedCookies", default=None,)
	sites: Optional[list[BrowserSite]] = Field(alias="sites", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .browser_site_list_status import BrowserSiteListStatus
from .browser_shared_cookie import BrowserSharedCookie
from .browser_site import BrowserSite
