from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIntelligenceProfile(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	aliases: Optional[list[str]] = Field(default=None,alias="aliases",)
	countriesOrRegionsOfOrigin: Optional[list[SecurityIntelligenceProfileCountryOrRegionOfOrigin]] = Field(default=None,alias="countriesOrRegionsOfOrigin",)
	description: Optional[SecurityFormattedContent] = Field(default=None,alias="description",)
	firstActiveDateTime: Optional[datetime] = Field(default=None,alias="firstActiveDateTime",)
	kind: Optional[SecurityIntelligenceProfileKind] = Field(default=None,alias="kind",)
	summary: Optional[SecurityFormattedContent] = Field(default=None,alias="summary",)
	targets: Optional[list[str]] = Field(default=None,alias="targets",)
	title: Optional[str] = Field(default=None,alias="title",)
	tradecraft: Optional[SecurityFormattedContent] = Field(default=None,alias="tradecraft",)
	indicators: Optional[list[SecurityIntelligenceProfileIndicator]] = Field(default=None,alias="indicators",)

from .security_intelligence_profile_country_or_region_of_origin import SecurityIntelligenceProfileCountryOrRegionOfOrigin
from .security_formatted_content import SecurityFormattedContent
from .security_intelligence_profile_kind import SecurityIntelligenceProfileKind
from .security_formatted_content import SecurityFormattedContent
from .security_formatted_content import SecurityFormattedContent
from .security_intelligence_profile_indicator import SecurityIntelligenceProfileIndicator

