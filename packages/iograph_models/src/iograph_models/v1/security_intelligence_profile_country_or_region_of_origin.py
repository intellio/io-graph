from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityIntelligenceProfileCountryOrRegionOfOrigin(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	label: Optional[str] = Field(alias="label", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

