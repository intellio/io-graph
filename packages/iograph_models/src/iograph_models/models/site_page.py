from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SitePage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	eTag: Optional[str] = Field(alias="eTag",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	parentReference: Optional[ItemReference] = Field(alias="parentReference",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	createdByUser: Optional[User] = Field(alias="createdByUser",default=None,)
	lastModifiedByUser: Optional[User] = Field(alias="lastModifiedByUser",default=None,)
	pageLayout: Optional[str | PageLayoutType] = Field(alias="pageLayout",default=None,)
	publishingState: Optional[PublicationFacet] = Field(alias="publishingState",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	promotionKind: Optional[str | PagePromotionType] = Field(alias="promotionKind",default=None,)
	reactions: Optional[ReactionsFacet] = Field(alias="reactions",default=None,)
	showComments: Optional[bool] = Field(alias="showComments",default=None,)
	showRecommendedPages: Optional[bool] = Field(alias="showRecommendedPages",default=None,)
	thumbnailWebUrl: Optional[str] = Field(alias="thumbnailWebUrl",default=None,)
	titleArea: Optional[TitleArea] = Field(alias="titleArea",default=None,)
	canvasLayout: Optional[CanvasLayout] = Field(alias="canvasLayout",default=None,)
	webParts: SerializeAsAny[Optional[list[WebPart]]] = Field(alias="webParts",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .page_layout_type import PageLayoutType
from .publication_facet import PublicationFacet
from .page_promotion_type import PagePromotionType
from .reactions_facet import ReactionsFacet
from .title_area import TitleArea
from .canvas_layout import CanvasLayout
from .web_part import WebPart

