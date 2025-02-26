from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Drive(BaseModel):
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
	driveType: Optional[str] = Field(default=None,alias="driveType",)
	owner: Optional[IdentitySet] = Field(default=None,alias="owner",)
	quota: Optional[Quota] = Field(default=None,alias="quota",)
	sharePointIds: Optional[SharepointIds] = Field(default=None,alias="sharePointIds",)
	system: Optional[SystemFacet] = Field(default=None,alias="system",)
	bundles: list[DriveItem] = Field(alias="bundles",)
	following: list[DriveItem] = Field(alias="following",)
	items: list[DriveItem] = Field(alias="items",)
	list: Optional[List] = Field(default=None,alias="list",)
	root: Optional[DriveItem] = Field(default=None,alias="root",)
	special: list[DriveItem] = Field(alias="special",)

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

