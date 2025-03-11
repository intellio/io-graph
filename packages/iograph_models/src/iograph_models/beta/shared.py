from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Shared(BaseModel):
	owner: SerializeAsAny[Optional[IdentitySet]] = Field(alias="owner",default=None,)
	scope: Optional[str] = Field(alias="scope",default=None,)
	sharedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="sharedBy",default=None,)
	sharedDateTime: Optional[datetime] = Field(alias="sharedDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet

