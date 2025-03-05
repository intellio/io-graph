from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TermStoreRelation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	relationship: Optional[TermStoreRelationType] = Field(default=None,alias="relationship",)
	fromTerm: Optional[TermStoreTerm] = Field(default=None,alias="fromTerm",)
	set: Optional[TermStoreSet] = Field(default=None,alias="set",)
	toTerm: Optional[TermStoreTerm] = Field(default=None,alias="toTerm",)

from .term_store_relation_type import TermStoreRelationType
from .term_store_term import TermStoreTerm
from .term_store_set import TermStoreSet
from .term_store_term import TermStoreTerm

