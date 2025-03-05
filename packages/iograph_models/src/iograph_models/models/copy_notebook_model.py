from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CopyNotebookModel(BaseModel):
	createdBy: Optional[str] = Field(alias="createdBy",default=None,)
	createdByIdentity: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdByIdentity",default=None,)
	createdTime: Optional[datetime] = Field(alias="createdTime",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault",default=None,)
	isShared: Optional[bool] = Field(alias="isShared",default=None,)
	lastModifiedBy: Optional[str] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedByIdentity: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedByIdentity",default=None,)
	lastModifiedTime: Optional[datetime] = Field(alias="lastModifiedTime",default=None,)
	links: Optional[NotebookLinks] = Field(alias="links",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	sectionGroupsUrl: Optional[str] = Field(alias="sectionGroupsUrl",default=None,)
	sectionsUrl: Optional[str] = Field(alias="sectionsUrl",default=None,)
	self: Optional[str] = Field(alias="self",default=None,)
	userRole: Optional[str | OnenoteUserRole] = Field(alias="userRole",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .notebook_links import NotebookLinks
from .onenote_user_role import OnenoteUserRole

