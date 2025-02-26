from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermStoreStore(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	defaultLanguageTag: Optional[str] = Field(default=None,alias="defaultLanguageTag",)
	languageTags: list[str] = Field(alias="languageTags",)
	groups: list[TermStoreGroup] = Field(alias="groups",)
	sets: list[TermStoreSet] = Field(alias="sets",)

from .term_store_group import TermStoreGroup
from .term_store_set import TermStoreSet

