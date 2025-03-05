from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TermColumn(BaseModel):
	allowMultipleValues: Optional[bool] = Field(alias="allowMultipleValues",default=None,)
	showFullyQualifiedName: Optional[bool] = Field(alias="showFullyQualifiedName",default=None,)
	parentTerm: Optional[TermStoreTerm] = Field(alias="parentTerm",default=None,)
	termSet: Optional[TermStoreSet] = Field(alias="termSet",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .term_store_term import TermStoreTerm
from .term_store_set import TermStoreSet

