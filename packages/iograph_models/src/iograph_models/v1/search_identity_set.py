from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchIdentitySet(BaseModel):
	application: Optional[SearchIdentity] = Field(alias="application", default=None,)
	device: Optional[SearchIdentity] = Field(alias="device", default=None,)
	user: Optional[SearchIdentity] = Field(alias="user", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .search_identity import SearchIdentity
from .search_identity import SearchIdentity
from .search_identity import SearchIdentity

