from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityIntelligenceProfile(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	aliases: list[Optional[str]] = Field(alias="aliases",)
	countriesOrRegionsOfOrigin: list[SecurityIntelligenceProfileCountryOrRegionOfOrigin] = Field(alias="countriesOrRegionsOfOrigin",)
	description: Optional[SecurityFormattedContent] = Field(default=None,alias="description",)
	firstActiveDateTime: Optional[datetime] = Field(default=None,alias="firstActiveDateTime",)
	kind: Optional[SecurityIntelligenceProfileKind] = Field(default=None,alias="kind",)
	summary: Optional[SecurityFormattedContent] = Field(default=None,alias="summary",)
	targets: list[Optional[str]] = Field(alias="targets",)
	title: Optional[str] = Field(default=None,alias="title",)
	tradecraft: Optional[SecurityFormattedContent] = Field(default=None,alias="tradecraft",)
	indicators: list[SecurityIntelligenceProfileIndicator] = Field(alias="indicators",)

from .security_intelligence_profile_country_or_region_of_origin import SecurityIntelligenceProfileCountryOrRegionOfOrigin
from .security_formatted_content import SecurityFormattedContent
from .security_intelligence_profile_kind import SecurityIntelligenceProfileKind
from .security_formatted_content import SecurityFormattedContent
from .security_formatted_content import SecurityFormattedContent
from .security_intelligence_profile_indicator import SecurityIntelligenceProfileIndicator

