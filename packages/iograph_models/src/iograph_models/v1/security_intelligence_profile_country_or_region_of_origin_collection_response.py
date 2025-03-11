from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIntelligenceProfileCountryOrRegionOfOriginCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SecurityIntelligenceProfileCountryOrRegionOfOrigin]] = Field(alias="value",default=None,)

from .security_intelligence_profile_country_or_region_of_origin import SecurityIntelligenceProfileCountryOrRegionOfOrigin

