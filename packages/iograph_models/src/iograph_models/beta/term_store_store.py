from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TermStoreStore(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.termStore.store"] = Field(alias="@odata.type",)
	defaultLanguageTag: Optional[str] = Field(alias="defaultLanguageTag", default=None,)
	languageTags: Optional[list[str]] = Field(alias="languageTags", default=None,)
	groups: Optional[list[TermStoreGroup]] = Field(alias="groups", default=None,)
	sets: Optional[list[TermStoreSet]] = Field(alias="sets", default=None,)

from .term_store_group import TermStoreGroup
from .term_store_set import TermStoreSet
