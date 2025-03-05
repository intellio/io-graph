from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OnenoteSection(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	self: Optional[str] = Field(default=None,alias="self",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	isDefault: Optional[bool] = Field(default=None,alias="isDefault",)
	links: Optional[SectionLinks] = Field(default=None,alias="links",)
	pagesUrl: Optional[str] = Field(default=None,alias="pagesUrl",)
	pages: Optional[list[OnenotePage]] = Field(default=None,alias="pages",)
	parentNotebook: Optional[Notebook] = Field(default=None,alias="parentNotebook",)
	parentSectionGroup: Optional[SectionGroup] = Field(default=None,alias="parentSectionGroup",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .section_links import SectionLinks
from .onenote_page import OnenotePage
from .notebook import Notebook
from .section_group import SectionGroup

