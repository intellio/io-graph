from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Shared(BaseModel):
	owner: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="owner",)
	scope: Optional[str] = Field(default=None,alias="scope",)
	sharedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="sharedBy",)
	sharedDateTime: Optional[datetime] = Field(default=None,alias="sharedDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet

