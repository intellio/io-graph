from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class RecycleBin(BaseModel):
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
	settings: Optional[RecycleBinSettings] = Field(default=None,alias="settings",)
	items: Optional[list[RecycleBinItem]] = Field(default=None,alias="items",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User
from .recycle_bin_settings import RecycleBinSettings
from .recycle_bin_item import RecycleBinItem

