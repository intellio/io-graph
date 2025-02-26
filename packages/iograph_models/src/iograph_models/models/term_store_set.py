from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TermStoreSet(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	localizedNames: list[TermStoreLocalizedName] = Field(alias="localizedNames",)
	properties: list[KeyValue] = Field(alias="properties",)
	children: list[TermStoreTerm] = Field(alias="children",)
	parentGroup: Optional[TermStoreGroup] = Field(default=None,alias="parentGroup",)
	relations: list[TermStoreRelation] = Field(alias="relations",)
	terms: list[TermStoreTerm] = Field(alias="terms",)

from .term_store_localized_name import TermStoreLocalizedName
from .key_value import KeyValue
from .term_store_term import TermStoreTerm
from .term_store_group import TermStoreGroup
from .term_store_relation import TermStoreRelation
from .term_store_term import TermStoreTerm

