from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Drive(BaseModel):
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
	driveType: Optional[str] = Field(alias="driveType",default=None,)
	owner: SerializeAsAny[Optional[IdentitySet]] = Field(alias="owner",default=None,)
	quota: Optional[Quota] = Field(alias="quota",default=None,)
	sharePointIds: Optional[SharepointIds] = Field(alias="sharePointIds",default=None,)
	system: Optional[SystemFacet] = Field(alias="system",default=None,)
	bundles: Optional[list[DriveItem]] = Field(alias="bundles",default=None,)
	following: Optional[list[DriveItem]] = Field(alias="following",default=None,)
	items: Optional[list[DriveItem]] = Field(alias="items",default=None,)
	list: Optional[List] = Field(alias="list",default=None,)
	root: Optional[DriveItem] = Field(alias="root",default=None,)
	special: Optional[list[DriveItem]] = Field(alias="special",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .identity_set import IdentitySet
from .quota import Quota
from .sharepoint_ids import SharepointIds
from .system_facet import SystemFacet
from .drive_item import DriveItem
from .drive_item import DriveItem
from .drive_item import DriveItem
from .list import List
from .drive_item import DriveItem
from .drive_item import DriveItem

