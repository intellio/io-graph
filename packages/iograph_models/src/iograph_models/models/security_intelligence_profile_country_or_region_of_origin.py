from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIntelligenceProfileCountryOrRegionOfOrigin(BaseModel):
	code: Optional[str] = Field(default=None,alias="code",)
	label: Optional[str] = Field(default=None,alias="label",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


