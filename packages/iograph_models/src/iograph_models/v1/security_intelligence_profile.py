from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityIntelligenceProfile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	aliases: Optional[list[str]] = Field(alias="aliases",default=None,)
	countriesOrRegionsOfOrigin: Optional[list[SecurityIntelligenceProfileCountryOrRegionOfOrigin]] = Field(alias="countriesOrRegionsOfOrigin",default=None,)
	description: Optional[SecurityFormattedContent] = Field(alias="description",default=None,)
	firstActiveDateTime: Optional[datetime] = Field(alias="firstActiveDateTime",default=None,)
	kind: Optional[SecurityIntelligenceProfileKind | str] = Field(alias="kind",default=None,)
	summary: Optional[SecurityFormattedContent] = Field(alias="summary",default=None,)
	targets: Optional[list[str]] = Field(alias="targets",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	tradecraft: Optional[SecurityFormattedContent] = Field(alias="tradecraft",default=None,)
	indicators: Optional[list[SecurityIntelligenceProfileIndicator]] = Field(alias="indicators",default=None,)

from .security_intelligence_profile_country_or_region_of_origin import SecurityIntelligenceProfileCountryOrRegionOfOrigin
from .security_formatted_content import SecurityFormattedContent
from .security_intelligence_profile_kind import SecurityIntelligenceProfileKind
from .security_formatted_content import SecurityFormattedContent
from .security_formatted_content import SecurityFormattedContent
from .security_intelligence_profile_indicator import SecurityIntelligenceProfileIndicator

