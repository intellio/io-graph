from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHuntingQueryResults(BaseModel):
	results: list[SecurityHuntingRowResult] = Field(alias="results",)
	schema: list[SecuritySinglePropertySchema] = Field(alias="schema",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_hunting_row_result import SecurityHuntingRowResult
from .security_single_property_schema import SecuritySinglePropertySchema

