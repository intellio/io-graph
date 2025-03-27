from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BrowserSharedCookieHistory(BaseModel):
	comment: Optional[str] = Field(alias="comment", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	hostOnly: Optional[bool] = Field(alias="hostOnly", default=None,)
	hostOrDomain: Optional[str] = Field(alias="hostOrDomain", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	path: Optional[str] = Field(alias="path", default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime", default=None,)
	sourceEnvironment: Optional[BrowserSharedCookieSourceEnvironment | str] = Field(alias="sourceEnvironment", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment

