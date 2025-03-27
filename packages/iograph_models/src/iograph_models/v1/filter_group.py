from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FilterGroup(BaseModel):
	clauses: Optional[list[FilterClause]] = Field(alias="clauses", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .filter_clause import FilterClause

