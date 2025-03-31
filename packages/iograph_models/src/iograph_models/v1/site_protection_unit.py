from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SiteProtectionUnit(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.siteProtectionUnit"] = Field(alias="@odata.type", default="#microsoft.graph.siteProtectionUnit")
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	error: Optional[PublicError] = Field(alias="error", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	policyId: Optional[str] = Field(alias="policyId", default=None,)
	status: Optional[ProtectionUnitStatus | str] = Field(alias="status", default=None,)
	siteId: Optional[str] = Field(alias="siteId", default=None,)
	siteName: Optional[str] = Field(alias="siteName", default=None,)
	siteWebUrl: Optional[str] = Field(alias="siteWebUrl", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .public_error import PublicError
from .protection_unit_status import ProtectionUnitStatus
