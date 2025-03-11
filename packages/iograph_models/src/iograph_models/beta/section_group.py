from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SectionGroup(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	self: Optional[str] = Field(alias="self",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	sectionGroupsUrl: Optional[str] = Field(alias="sectionGroupsUrl",default=None,)
	sectionsUrl: Optional[str] = Field(alias="sectionsUrl",default=None,)
	parentNotebook: Optional[Notebook] = Field(alias="parentNotebook",default=None,)
	parentSectionGroup: Optional[SectionGroup] = Field(alias="parentSectionGroup",default=None,)
	sectionGroups: Optional[list[SectionGroup]] = Field(alias="sectionGroups",default=None,)
	sections: Optional[list[OnenoteSection]] = Field(alias="sections",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .notebook import Notebook
from .onenote_section import OnenoteSection

