from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ItemPublication(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.itemPublication"] = Field(alias="@odata.type", default="#microsoft.graph.itemPublication")
	allowedAudiences: Optional[AllowedAudiences | str] = Field(alias="allowedAudiences", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	inference: Optional[InferenceData] = Field(alias="inference", default=None,)
	isSearchable: Optional[bool] = Field(alias="isSearchable", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	source: Optional[PersonDataSources] = Field(alias="source", default=None,)
	sources: Optional[list[ProfileSourceAnnotation]] = Field(alias="sources", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	publishedDate: Optional[str] = Field(alias="publishedDate", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	thumbnailUrl: Optional[str] = Field(alias="thumbnailUrl", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)

from .allowed_audiences import AllowedAudiences
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .inference_data import InferenceData
from .person_data_sources import PersonDataSources
from .profile_source_annotation import ProfileSourceAnnotation
