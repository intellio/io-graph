from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OnenoteSection(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	self: Optional[str] = Field(alias="self",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault",default=None,)
	links: Optional[SectionLinks] = Field(alias="links",default=None,)
	pagesUrl: Optional[str] = Field(alias="pagesUrl",default=None,)
	pages: Optional[list[OnenotePage]] = Field(alias="pages",default=None,)
	parentNotebook: Optional[Notebook] = Field(alias="parentNotebook",default=None,)
	parentSectionGroup: Optional[SectionGroup] = Field(alias="parentSectionGroup",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .section_links import SectionLinks
from .onenote_page import OnenotePage
from .notebook import Notebook
from .section_group import SectionGroup

