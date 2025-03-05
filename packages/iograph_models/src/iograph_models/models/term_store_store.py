from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TermStoreStore(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	defaultLanguageTag: Optional[str] = Field(default=None,alias="defaultLanguageTag",)
	languageTags: Optional[list[str]] = Field(default=None,alias="languageTags",)
	groups: Optional[list[TermStoreGroup]] = Field(default=None,alias="groups",)
	sets: Optional[list[TermStoreSet]] = Field(default=None,alias="sets",)

from .term_store_group import TermStoreGroup
from .term_store_set import TermStoreSet

