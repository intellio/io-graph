from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OnenotePage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	self: Optional[str] = Field(default=None,alias="self",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	content: Optional[str] = Field(default=None,alias="content",)
	contentUrl: Optional[str] = Field(default=None,alias="contentUrl",)
	createdByAppId: Optional[str] = Field(default=None,alias="createdByAppId",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	level: Optional[int] = Field(default=None,alias="level",)
	links: Optional[PageLinks] = Field(default=None,alias="links",)
	order: Optional[int] = Field(default=None,alias="order",)
	title: Optional[str] = Field(default=None,alias="title",)
	userTags: Optional[list[str]] = Field(default=None,alias="userTags",)
	parentNotebook: Optional[Notebook] = Field(default=None,alias="parentNotebook",)
	parentSection: Optional[OnenoteSection] = Field(default=None,alias="parentSection",)

from .page_links import PageLinks
from .notebook import Notebook
from .onenote_section import OnenoteSection

