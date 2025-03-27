from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BrowserSiteHistory(BaseModel):
	allowRedirect: Optional[bool] = Field(alias="allowRedirect", default=None,)
	comment: Optional[str] = Field(alias="comment", default=None,)
	compatibilityMode: Optional[BrowserSiteCompatibilityMode | str] = Field(alias="compatibilityMode", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	mergeType: Optional[BrowserSiteMergeType | str] = Field(alias="mergeType", default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime", default=None,)
	targetEnvironment: Optional[BrowserSiteTargetEnvironment | str] = Field(alias="targetEnvironment", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .browser_site_merge_type import BrowserSiteMergeType
from .browser_site_target_environment import BrowserSiteTargetEnvironment

