from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TermStoreRelation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.termStore.relation"] = Field(alias="@odata.type", default="#microsoft.graph.termStore.relation")
	relationship: Optional[TermStoreRelationType | str] = Field(alias="relationship", default=None,)
	fromTerm: Optional[TermStoreTerm] = Field(alias="fromTerm", default=None,)
	set: Optional[TermStoreSet] = Field(alias="set", default=None,)
	toTerm: Optional[TermStoreTerm] = Field(alias="toTerm", default=None,)

from .term_store_relation_type import TermStoreRelationType
from .term_store_term import TermStoreTerm
from .term_store_set import TermStoreSet
