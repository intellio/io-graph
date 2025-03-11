from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryTag(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	childSelectability: Optional[EdiscoveryChildSelectability | str] = Field(alias="childSelectability",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	childTags: Optional[list[EdiscoveryTag]] = Field(alias="childTags",default=None,)
	parent: Optional[EdiscoveryTag] = Field(alias="parent",default=None,)

from .ediscovery_child_selectability import EdiscoveryChildSelectability
from .identity_set import IdentitySet

