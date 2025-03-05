from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryReviewTag(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	childSelectability: Optional[SecurityChildSelectability | str] = Field(alias="childSelectability",default=None,)
	childTags: Optional[list[SecurityEdiscoveryReviewTag]] = Field(alias="childTags",default=None,)
	parent: Optional[SecurityEdiscoveryReviewTag] = Field(alias="parent",default=None,)

from .identity_set import IdentitySet
from .security_child_selectability import SecurityChildSelectability

