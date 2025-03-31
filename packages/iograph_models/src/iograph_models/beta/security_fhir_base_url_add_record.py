from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityFhirBaseUrlAddRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.fhirBaseUrlAddRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.fhirBaseUrlAddRecord")

