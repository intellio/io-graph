from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryReviewTag(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	childSelectability: Optional[SecurityChildSelectability] = Field(default=None,alias="childSelectability",)
	childTags: Optional[list[SecurityEdiscoveryReviewTag]] = Field(default=None,alias="childTags",)
	parent: Optional[SecurityEdiscoveryReviewTag] = Field(default=None,alias="parent",)

from .identity_set import IdentitySet
from .security_child_selectability import SecurityChildSelectability

