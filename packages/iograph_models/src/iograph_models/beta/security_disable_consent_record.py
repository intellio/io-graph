from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDisableConsentRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.disableConsentRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.disableConsentRecord")

