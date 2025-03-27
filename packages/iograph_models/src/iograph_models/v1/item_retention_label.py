from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ItemRetentionLabel(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	isLabelAppliedExplicitly: Optional[bool] = Field(alias="isLabelAppliedExplicitly", default=None,)
	labelAppliedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="labelAppliedBy", default=None,discriminator="odata_type", )
	labelAppliedDateTime: Optional[datetime] = Field(alias="labelAppliedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	retentionSettings: Optional[RetentionLabelSettings] = Field(alias="retentionSettings", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .retention_label_settings import RetentionLabelSettings

