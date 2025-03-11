from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PageTemplate(BaseModel):
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
	pageLayout: Optional[PageLayoutType | str] = Field(alias="pageLayout",default=None,)
	publishingState: Optional[PublicationFacet] = Field(alias="publishingState",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
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
from .title_area import TitleArea
from .canvas_layout import CanvasLayout
from .web_part import WebPart

