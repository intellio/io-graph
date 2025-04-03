from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class BrowserSharedCookie(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.browserSharedCookie"] = Field(alias="@odata.type", default="#microsoft.graph.browserSharedCookie")
	comment: Optional[str] = Field(alias="comment", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	history: Optional[list[BrowserSharedCookieHistory]] = Field(alias="history", default=None,)
	hostOnly: Optional[bool] = Field(alias="hostOnly", default=None,)
	hostOrDomain: Optional[str] = Field(alias="hostOrDomain", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	path: Optional[str] = Field(alias="path", default=None,)
	sourceEnvironment: Optional[BrowserSharedCookieSourceEnvironment | str] = Field(alias="sourceEnvironment", default=None,)
	status: Optional[BrowserSharedCookieStatus | str] = Field(alias="status", default=None,)

from .browser_shared_cookie_history import BrowserSharedCookieHistory
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment
from .browser_shared_cookie_status import BrowserSharedCookieStatus
