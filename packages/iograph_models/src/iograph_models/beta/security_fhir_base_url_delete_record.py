from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFhirBaseUrlDeleteRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.fhirBaseUrlDeleteRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.fhirBaseUrlDeleteRecord")


