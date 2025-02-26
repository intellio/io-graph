from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityIntelligenceProfileCountryOrRegionOfOriginCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityIntelligenceProfileCountryOrRegionOfOrigin] = Field(alias="value",)

from .security_intelligence_profile_country_or_region_of_origin import SecurityIntelligenceProfileCountryOrRegionOfOrigin

