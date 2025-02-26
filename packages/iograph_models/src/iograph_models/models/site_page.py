from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SitePage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	eTag: Optional[str] = Field(default=None,alias="eTag",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	parentReference: Optional[ItemReference] = Field(default=None,alias="parentReference",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	createdByUser: Optional[User] = Field(default=None,alias="createdByUser",)
	lastModifiedByUser: Optional[User] = Field(default=None,alias="lastModifiedByUser",)
	pageLayout: Optional[PageLayoutType] = Field(default=None,alias="pageLayout",)
	publishingState: Optional[PublicationFacet] = Field(default=None,alias="publishingState",)
	title: Optional[str] = Field(default=None,alias="title",)
	promotionKind: Optional[PagePromotionType] = Field(default=None,alias="promotionKind",)
	reactions: Optional[ReactionsFacet] = Field(default=None,alias="reactions",)
	showComments: Optional[bool] = Field(default=None,alias="showComments",)
	showRecommendedPages: Optional[bool] = Field(default=None,alias="showRecommendedPages",)
	thumbnailWebUrl: Optional[str] = Field(default=None,alias="thumbnailWebUrl",)
	titleArea: Optional[TitleArea] = Field(default=None,alias="titleArea",)
	canvasLayout: Optional[CanvasLayout] = Field(default=None,alias="canvasLayout",)
	webParts: list[WebPart] = Field(alias="webParts",)

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

