from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FilterGroup(BaseModel):
	clauses: Optional[list[FilterClause]] = Field(default=None,alias="clauses",)
	name: Optional[str] = Field(default=None,alias="name",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .filter_clause import FilterClause

