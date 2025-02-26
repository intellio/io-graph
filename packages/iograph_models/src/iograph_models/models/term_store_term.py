from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TermStoreTerm(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	descriptions: list[TermStoreLocalizedDescription] = Field(alias="descriptions",)
	labels: list[TermStoreLocalizedLabel] = Field(alias="labels",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	properties: list[KeyValue] = Field(alias="properties",)
	children: list[TermStoreTerm] = Field(alias="children",)
	relations: list[TermStoreRelation] = Field(alias="relations",)
	set: Optional[TermStoreSet] = Field(default=None,alias="set",)

from .term_store_localized_description import TermStoreLocalizedDescription
from .term_store_localized_label import TermStoreLocalizedLabel
from .key_value import KeyValue
from .term_store_relation import TermStoreRelation
from .term_store_set import TermStoreSet

