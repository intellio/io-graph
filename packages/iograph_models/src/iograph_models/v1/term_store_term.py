from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TermStoreTerm(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.termStore.term"] = Field(alias="@odata.type", default="#microsoft.graph.termStore.term")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	descriptions: Optional[list[TermStoreLocalizedDescription]] = Field(alias="descriptions", default=None,)
	labels: Optional[list[TermStoreLocalizedLabel]] = Field(alias="labels", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	properties: Optional[list[KeyValue]] = Field(alias="properties", default=None,)
	children: Optional[list[TermStoreTerm]] = Field(alias="children", default=None,)
	relations: Optional[list[TermStoreRelation]] = Field(alias="relations", default=None,)
	set: Optional[TermStoreSet] = Field(alias="set", default=None,)

from .term_store_localized_description import TermStoreLocalizedDescription
from .term_store_localized_label import TermStoreLocalizedLabel
from .key_value import KeyValue
from .term_store_relation import TermStoreRelation
from .term_store_set import TermStoreSet
