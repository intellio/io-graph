from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TermStoreGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	parentSiteId: Optional[str] = Field(alias="parentSiteId", default=None,)
	scope: Optional[TermStoreTermGroupScope | str] = Field(alias="scope", default=None,)
	sets: Optional[list[TermStoreSet]] = Field(alias="sets", default=None,)

from .term_store_term_group_scope import TermStoreTermGroupScope
from .term_store_set import TermStoreSet

