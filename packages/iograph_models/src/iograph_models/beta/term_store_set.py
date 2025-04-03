from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TermStoreSet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.termStore.set"] = Field(alias="@odata.type", default="#microsoft.graph.termStore.set")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	localizedNames: Optional[list[TermStoreLocalizedName]] = Field(alias="localizedNames", default=None,)
	properties: Optional[list[KeyValue]] = Field(alias="properties", default=None,)
	children: Optional[list[TermStoreTerm]] = Field(alias="children", default=None,)
	parentGroup: Optional[TermStoreGroup] = Field(alias="parentGroup", default=None,)
	relations: Optional[list[TermStoreRelation]] = Field(alias="relations", default=None,)
	terms: Optional[list[TermStoreTerm]] = Field(alias="terms", default=None,)

from .term_store_localized_name import TermStoreLocalizedName
from .key_value import KeyValue
from .term_store_term import TermStoreTerm
from .term_store_group import TermStoreGroup
from .term_store_relation import TermStoreRelation
