from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SharedDriveItem(BaseModel):
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
	owner: Optional[IdentitySet] = Field(default=None,alias="owner",)
	driveItem: Optional[DriveItem] = Field(default=None,alias="driveItem",)
	items: Optional[list[DriveItem]] = Field(default=None,alias="items",)
	list: Optional[List] = Field(default=None,alias="list",)
	listItem: Optional[ListItem] = Field(default=None,alias="listItem",)
	permission: Optional[Permission] = Field(default=None,alias="permission",)
	root: Optional[DriveItem] = Field(default=None,alias="root",)
	site: Optional[Site] = Field(default=None,alias="site",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .identity_set import IdentitySet
from .drive_item import DriveItem
from .drive_item import DriveItem
from .list import List
from .list_item import ListItem
from .permission import Permission
from .drive_item import DriveItem
from .site import Site

