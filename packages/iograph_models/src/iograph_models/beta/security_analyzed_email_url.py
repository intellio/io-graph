from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityAnalyzedEmailUrl(BaseModel):
	detectionMethod: Optional[str] = Field(alias="detectionMethod", default=None,)
	detonationDetails: Optional[SecurityDetonationDetails] = Field(alias="detonationDetails", default=None,)
	tenantAllowBlockListDetailInfo: Optional[str] = Field(alias="tenantAllowBlockListDetailInfo", default=None,)
	threatType: Optional[SecurityThreatType | str] = Field(alias="threatType", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_detonation_details import SecurityDetonationDetails
from .security_threat_type import SecurityThreatType
