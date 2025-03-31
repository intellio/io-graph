from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHuntingQueryResults(BaseModel):
	results: Optional[list[SecurityHuntingRowResult]] = Field(alias="results", default=None,)
	schema_: Optional[list[SecuritySinglePropertySchema]] = Field(alias="schema", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_hunting_row_result import SecurityHuntingRowResult
from .security_single_property_schema import SecuritySinglePropertySchema
