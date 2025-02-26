from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CopyNotebookModel(BaseModel):
	createdBy: Optional[str] = Field(default=None,alias="createdBy",)
	createdByIdentity: Optional[IdentitySet] = Field(default=None,alias="createdByIdentity",)
	createdTime: Optional[datetime] = Field(default=None,alias="createdTime",)
	id: Optional[str] = Field(default=None,alias="id",)
	isDefault: Optional[bool] = Field(default=None,alias="isDefault",)
	isShared: Optional[bool] = Field(default=None,alias="isShared",)
	lastModifiedBy: Optional[str] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedByIdentity: Optional[IdentitySet] = Field(default=None,alias="lastModifiedByIdentity",)
	lastModifiedTime: Optional[datetime] = Field(default=None,alias="lastModifiedTime",)
	links: Optional[NotebookLinks] = Field(default=None,alias="links",)
	name: Optional[str] = Field(default=None,alias="name",)
	sectionGroupsUrl: Optional[str] = Field(default=None,alias="sectionGroupsUrl",)
	sectionsUrl: Optional[str] = Field(default=None,alias="sectionsUrl",)
	self: Optional[str] = Field(default=None,alias="self",)
	userRole: Optional[OnenoteUserRole] = Field(default=None,alias="userRole",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .notebook_links import NotebookLinks
from .onenote_user_role import OnenoteUserRole

