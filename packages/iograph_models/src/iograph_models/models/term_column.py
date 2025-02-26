from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TermColumn(BaseModel):
	allowMultipleValues: Optional[bool] = Field(default=None,alias="allowMultipleValues",)
	showFullyQualifiedName: Optional[bool] = Field(default=None,alias="showFullyQualifiedName",)
	parentTerm: Optional[TermStoreTerm] = Field(default=None,alias="parentTerm",)
	termSet: Optional[TermStoreSet] = Field(default=None,alias="termSet",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .term_store_term import TermStoreTerm
from .term_store_set import TermStoreSet

