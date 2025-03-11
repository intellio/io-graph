from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SharedDriveItem(BaseModel):
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
	owner: SerializeAsAny[Optional[IdentitySet]] = Field(alias="owner",default=None,)
	driveItem: Optional[DriveItem] = Field(alias="driveItem",default=None,)
	items: Optional[list[DriveItem]] = Field(alias="items",default=None,)
	list: Optional[List] = Field(alias="list",default=None,)
	listItem: Optional[ListItem] = Field(alias="listItem",default=None,)
	permission: Optional[Permission] = Field(alias="permission",default=None,)
	root: Optional[DriveItem] = Field(alias="root",default=None,)
	site: Optional[Site] = Field(alias="site",default=None,)

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

