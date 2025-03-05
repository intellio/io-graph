from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Notebook(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	self: Optional[str] = Field(default=None,alias="self",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	isDefault: Optional[bool] = Field(default=None,alias="isDefault",)
	isShared: Optional[bool] = Field(default=None,alias="isShared",)
	links: Optional[NotebookLinks] = Field(default=None,alias="links",)
	sectionGroupsUrl: Optional[str] = Field(default=None,alias="sectionGroupsUrl",)
	sectionsUrl: Optional[str] = Field(default=None,alias="sectionsUrl",)
	userRole: Optional[OnenoteUserRole] = Field(default=None,alias="userRole",)
	sectionGroups: Optional[list[SectionGroup]] = Field(default=None,alias="sectionGroups",)
	sections: Optional[list[OnenoteSection]] = Field(default=None,alias="sections",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .notebook_links import NotebookLinks
from .onenote_user_role import OnenoteUserRole
from .section_group import SectionGroup
from .onenote_section import OnenoteSection

