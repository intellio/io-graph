from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class BrowserSite(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.browserSite"] = Field(alias="@odata.type",)
	allowRedirect: Optional[bool] = Field(alias="allowRedirect", default=None,)
	comment: Optional[str] = Field(alias="comment", default=None,)
	compatibilityMode: Optional[BrowserSiteCompatibilityMode | str] = Field(alias="compatibilityMode", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	history: Optional[list[BrowserSiteHistory]] = Field(alias="history", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	mergeType: Optional[BrowserSiteMergeType | str] = Field(alias="mergeType", default=None,)
	status: Optional[BrowserSiteStatus | str] = Field(alias="status", default=None,)
	targetEnvironment: Optional[BrowserSiteTargetEnvironment | str] = Field(alias="targetEnvironment", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)

from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
from .browser_site_history import BrowserSiteHistory
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .browser_site_merge_type import BrowserSiteMergeType
from .browser_site_status import BrowserSiteStatus
from .browser_site_target_environment import BrowserSiteTargetEnvironment
