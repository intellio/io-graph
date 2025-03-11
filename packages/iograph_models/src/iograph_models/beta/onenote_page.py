from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OnenotePage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	self: Optional[str] = Field(alias="self",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	content: Optional[str] = Field(alias="content",default=None,)
	contentUrl: Optional[str] = Field(alias="contentUrl",default=None,)
	createdByAppId: Optional[str] = Field(alias="createdByAppId",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	level: Optional[int] = Field(alias="level",default=None,)
	links: Optional[PageLinks] = Field(alias="links",default=None,)
	order: Optional[int] = Field(alias="order",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	userTags: Optional[list[str]] = Field(alias="userTags",default=None,)
	parentNotebook: Optional[Notebook] = Field(alias="parentNotebook",default=None,)
	parentSection: Optional[OnenoteSection] = Field(alias="parentSection",default=None,)

from .page_links import PageLinks
from .notebook import Notebook
from .onenote_section import OnenoteSection

