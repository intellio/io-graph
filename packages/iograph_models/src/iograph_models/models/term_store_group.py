from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TermStoreGroup(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	parentSiteId: Optional[str] = Field(default=None,alias="parentSiteId",)
	scope: Optional[TermStoreTermGroupScope] = Field(default=None,alias="scope",)
	sets: list[TermStoreSet] = Field(alias="sets",)

from .term_store_term_group_scope import TermStoreTermGroupScope
from .term_store_set import TermStoreSet

