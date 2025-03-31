from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ItemRetentionLabel(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.itemRetentionLabel"] = Field(alias="@odata.type",)
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
