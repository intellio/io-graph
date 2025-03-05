from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchIdentitySet(BaseModel):
	application: Optional[SearchIdentity] = Field(default=None,alias="application",)
	device: Optional[SearchIdentity] = Field(default=None,alias="device",)
	user: Optional[SearchIdentity] = Field(default=None,alias="user",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .search_identity import SearchIdentity
from .search_identity import SearchIdentity
from .search_identity import SearchIdentity

