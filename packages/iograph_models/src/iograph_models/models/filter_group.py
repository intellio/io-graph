from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FilterGroup(BaseModel):
	clauses: list[FilterClause] = Field(alias="clauses",)
	name: Optional[str] = Field(default=None,alias="name",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .filter_clause import FilterClause

