from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityFhirBaseUrlUpdateRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.fhirBaseUrlUpdateRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.fhirBaseUrlUpdateRecord")

