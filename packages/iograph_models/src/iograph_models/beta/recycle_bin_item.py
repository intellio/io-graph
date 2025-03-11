from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RecycleBinItem(BaseModel):
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
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	deletedFromLocation: Optional[str] = Field(alias="deletedFromLocation",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .item_reference import ItemReference
from .user import User
from .user import User

