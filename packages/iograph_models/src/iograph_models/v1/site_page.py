from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SitePage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	eTag: Optional[str] = Field(alias="eTag", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	parentReference: Optional[ItemReference] = Field(alias="parentReference", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	createdByUser: Optional[User] = Field(alias="createdByUser", default=None,)
	lastModifiedByUser: Optional[User] = Field(alias="lastModifiedByUser", default=None,)
	pageLayout: Optional[PageLayoutType | str] = Field(alias="pageLayout", default=None,)
	publishingState: Optional[PublicationFacet] = Field(alias="publishingState", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	promotionKind: Optional[PagePromotionType | str] = Field(alias="promotionKind", default=None,)
	reactions: Optional[ReactionsFacet] = Field(alias="reactions", default=None,)
	showComments: Optional[bool] = Field(alias="showComments", default=None,)
	showRecommendedPages: Optional[bool] = Field(alias="showRecommendedPages", default=None,)
	thumbnailWebUrl: Optional[str] = Field(alias="thumbnailWebUrl", default=None,)
	titleArea: Optional[TitleArea] = Field(alias="titleArea", default=None,)
	canvasLayout: Optional[CanvasLayout] = Field(alias="canvasLayout", default=None,)
	webParts: Optional[list[Annotated[Union[StandardWebPart, TextWebPart]],Field(discriminator="odata_type")]]] = Field(alias="webParts", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .page_layout_type import PageLayoutType
from .publication_facet import PublicationFacet
from .page_promotion_type import PagePromotionType
from .reactions_facet import ReactionsFacet
from .title_area import TitleArea
from .canvas_layout import CanvasLayout
from .standard_web_part import StandardWebPart
from .text_web_part import TextWebPart

